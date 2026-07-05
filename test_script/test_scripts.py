from api_endpoints.apis import *
import pytest
from config.config_setup import *
from utils.json_helper import json_helper_tool
from utils.logger_helper import get_logger


logger = get_logger()


#-----------------------------------test function scripts -------------------------

def test_login(auth_setup):
    try:
        headers = auth_setup
        token = headers.get("Authorization")
        actual_jwt = token.split(" ")[1]
        assert actual_jwt != "None", "Login failed: no token returned"
        logger.info("test_login passed")
    except AssertionError as exc:
        logger.error("test_login failed: %s", exc)
        raise



@pytest.fixture(scope="module")
def created_employee(api_client):
    payload = json_helper_tool(CREATE_PAYLOAD)
    expected_emp_id = payload.get('employee_id')
    status_code, response_api = create_new_employee(api_client, payload)

    assert status_code == 201, f"Setup failed: expected 201 but got {status_code}. Response: {response_api.get('detail')}"
    assert response_api['success'] is True
    assert response_api['message'].strip() == 'Employee created successfully'
    assert response_api['data'] == payload, "Payload Not Same"

    emp_id = response_api['data'].get('employee_id')
    assert emp_id == expected_emp_id, f"ERROR: Expected employee ID {expected_emp_id}, but got {emp_id}"

    yield emp_id

    # Teardown: best-effort cleanup, runs even if a dependent test fails
    print(f"Cleaning up employee {emp_id}...")
    status_code, _ = delete_employee(api_client, emp_id)
    if status_code not in (200,404):  # 404 means it was already deleted
        print(f"WARNING: cleanup for {emp_id} returned unexpected status {status_code}")

def test_get_employees(api_client):
    status_code, response_api = get_all_employees(api_client)
    if status_code == 200:
        message = response_api['message']
        datas = response_api['data']
        print("Get All Data : ", datas)
        assert message.strip() == 'Employees fetched successfully', "Unexpected success message"
        assert len(datas) > 0, 'No data returned from DB'
        logger.info("test_get_employees passed")
    else:
        error_msg = response_api.get("detail")
        logger.error("test_get_employees failed: status_code=%s, error=%s", status_code, error_msg)
        pytest.fail(f"ERROR : Unexpected status code : {status_code} and Error Msg : {error_msg}")


def test_get_employee_by_id(api_client, created_employee):
    new_created_emp_id = created_employee
    status_code, response_api = get_employee_by_id(api_client, new_created_emp_id)

    print("Newly Created Employee: ", response_api)

    if status_code == 200:
        assert response_api['success'] is True, "API did not return success=True"
        assert response_api['data']['employee_id'] == new_created_emp_id, (
            f"Expected employee ID {new_created_emp_id}, but got {response_api['data']['employee_id']}"
        )
        assert response_api['message'].strip() == 'Employee fetched successfully', "Unexpected fetch message"
        logger.info("test_get_employee_by_id passed")
    else:
        msg = response_api.get("detail")
        logger.error("test_get_employee_by_id failed: status_code=%s, error=%s", status_code, msg)
        pytest.fail(f"ERROR : Unexpected status code : {status_code} and Error Msg : {msg}")
    


def test_update_employee(api_client, created_employee):
    new_created_emp_id = created_employee
    updated_payload = json_helper_tool(UPDATE_PAYLOAD)
    updated_payload['employee_id'] = new_created_emp_id
    print("Updated Payload : ", updated_payload)
    status_code, response_api = update_employee(api_client, new_created_emp_id, updated_payload)

    if status_code == 200:
        message = response_api.get('message')
        print(response_api)
        assert message.strip() == 'Employee updated successfully'
        logger.info("test_update_employee passed")
    else:
        logger.error("test_update_employee failed: status_code=%s, error=%s", status_code, response_api.get('detail'))
        pytest.fail(f"ERROR : Unexpected status code : {status_code} and Error Msg : {response_api.get('detail')}")



def test_delete_employee(api_client, created_employee):
    new_created_emp_id = created_employee
    status_code, response_api = delete_employee(api_client, new_created_emp_id)
    print(response_api)

    if status_code == 200:
        message = response_api.get('message')
        assert message.strip() == 'Employee deleted successfully', "Unexpected delete message"
        logger.info("test_delete_employee passed")
    else:
        logger.error("test_delete_employee failed: status_code=%s, error=%s", status_code, response_api.get('detail'))
        pytest.fail(f"ERROR : Unexpected status code : {status_code} and Error Msg : {response_api.get('detail')}")
