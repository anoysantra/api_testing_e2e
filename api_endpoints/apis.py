import requests

API_ENDPOINT = 'https://fastapi-endpoints-new.onrender.com/'

session = requests.Session()

def login(username,password):
    creds = {
        "username" : username,
        "password" : password
    }
    headers = {'Content-Type': 'application/json'}
    response = session.post(url = f'{API_ENDPOINT}/login', json = creds , headers = headers )
    response_data = response.json()
    token = response_data.get("access_token")

    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def get_all_employees(session):
    response = session.get(url = f'{API_ENDPOINT}/employees')
    return response.status_code, response.json()


def get_employee_by_id(session , emp_id : str):
    response = session.get(url = f'{API_ENDPOINT}/employees/{emp_id}')
    return response.status_code, response.json()


def create_new_employee(session , payload : dict):
    response = session.post(url = f'{API_ENDPOINT}/employees/' , json = payload)
    return response.status_code, response.json()


def update_employee(session, emp_id : str , updated_payload : dict):
    response = session.put(url = f'{API_ENDPOINT}/employees/{emp_id}' , json = updated_payload)
    return response.status_code , response.json()


def delete_employee(session, emp_id : str):
    response = session.delete(url = f'{API_ENDPOINT}/employees/{emp_id}')
    return response.status_code , response.json()
