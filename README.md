# API Test Automation Suite for Employee Management

This project is a practical API automation framework built in Python using pytest and requests. It tests a live employee-management REST API by validating authentication, employee retrieval, creation, update, and deletion flows.

> A compact but professional example of backend test automation, designed to be easy to read, maintain, and showcase to hiring managers or technical reviewers.

---

## What this project demonstrates

- Real API testing using HTTP requests and response validation
- Pytest-based automation with fixtures, parametrization, and assertions
- Reusable helper modules for JSON loading and logging
- Structured test design that is easy to read and extend

---

## Tech stack

- Python for test logic and scripting
- pytest as the test runner and assertion framework
- requests for sending HTTP requests to the API
- JSON files for test payloads and credentials
- Logging and report artifacts for test visibility

---

## Project structure

- [api_endpoints/apis.py](api_endpoints/apis.py): wrapper functions for login, GET, POST, PUT, and DELETE requests
- [conftest.py](conftest.py): pytest fixtures that create authenticated sessions for test execution
- [config/config_setup.py](config/config_setup.py): shared paths for payloads, credentials, and IDs
- [test_script/test_scripts.py](test_script/test_scripts.py): main test cases for the CRUD workflow
- [test_data](test_data): JSON files used as test data and sample credentials
- [utils](utils): helper modules for JSON and logging support
- [logs](logs) and [reports](reports): output files, logs, and reporting artifacts

---

## How the workflow works

1. Credentials are loaded from the test data folder.
2. Pytest fixtures authenticate users and create a reusable session with a Bearer token.
3. The tests call the API helper functions in [api_endpoints/apis.py](api_endpoints/apis.py).
4. Each test checks the response status code, success message, and payload content.
5. Logging captures important events and failures for easier debugging.

---

## Key pytest concepts used

Pytest is the core framework here because it makes test automation simple, readable, and scalable.

- Test discovery: pytest automatically finds test files such as those in [test_script](test_script).
- Assertions: test outcomes are validated using Python assert statements.
- Fixtures: reusable setup and teardown logic. In this project, fixtures create authentication headers and a shared requests session.
- Fixture scopes: the fixtures use module scope, which means setup work is reused across tests in the same module.
- Parametrization: the same test logic can run for multiple users by passing different credential sets. This improves coverage without duplicating code.
- Yield fixtures: the fixture lifecycle uses yield to perform cleanup after the test phase finishes.
- Reporting: pytest provides clear test summaries, and the project also stores reports in [reports](reports).

---

## Why fixtures matter here

Fixtures reduce repetition. Instead of repeating login logic in every test, the framework defines it once and uses it across the suite. This makes the tests cleaner, easier to maintain, and less fragile.

---

## Role of the requests library

The requests library is used to communicate with the API over HTTP.

- requests.Session() keeps the connection and headers organized for repeated calls
- session.post() sends login and create requests
- session.get() retrieves employee data
- session.put() updates an employee record
- session.delete() removes an employee record
- JSON payloads are passed directly using the json parameter, which makes API communication straightforward

---

## Test flow in this project

- The login test verifies that authentication returns a valid token.
- A setup fixture creates a new employee before the read/update/delete tests run.
- The suite then checks that the employee can be fetched, updated, and deleted successfully.
- Cleanup is handled after the test lifecycle so the environment stays as tidy as possible.

---

## How to run the tests

```bash
pytest -q
```

The project uses the configuration in [pytest.ini](pytest.ini) and writes detailed test output and logs to [logs](logs).

---

## Current status

The suite is a good example of API automation in practice. During execution, it showed some live-service issues such as duplicate employee IDs and token validation errors, which are common when testing against shared backend data. That makes this project a realistic demonstration of real-world API testing challenges.
