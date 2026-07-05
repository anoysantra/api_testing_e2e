#scope:module
import pytest
from api_endpoints.apis import *
from utils.json_helper import *
from config.config_setup import *
import json
import requests


cred_data = json_helper_tool(CREDENTIALS)


parameter = []
for data in cred_data:
    username = data['username']
    password = data['password']
    parameter.append((username,password))

#@pytest.mark.parametrize("username, password" , parameter)
@pytest.fixture(scope = 'module' , params=parameter , ids=lambda p: p[0])
def auth_setup(request):
    username , password = request.param
    headers = login(username,password)
    return headers

@pytest.fixture(scope = 'module', autouse = True)
def api_client(auth_setup):
    auth_headers = auth_setup
    session = requests.Session()
    session.headers.update(auth_headers)
    yield session
    print("Closing Session...................")
    session.close()  # Cleanup after tests
