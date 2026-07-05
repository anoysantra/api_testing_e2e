# config.py

import os



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CREATE_PAYLOAD = os.path.join(
    BASE_DIR,
    "test_data",
    "payload.json"
)

UPDATE_PAYLOAD = os.path.join(
    BASE_DIR,
    "test_data",
    "updated_payload.json"
)

CREDENTIALS = os.path.join(
    BASE_DIR,
    "test_data",
    "creds.json"
)

EMPLOYEE_IDS = os.path.join(BASE_DIR , "test_data" , "emp_id.json")
