import os
import pytest
import requests

test_endpoint="/users/login"

base_url = os.environ.get('BASE_URL')
def test_try_login_with_wrong_credentiald():
    login = "testuser"
    password = "something"
    data = {
        "login_id": login,
        "password": password
    }
    response = requests.post(url=f'{base_url}{test_endpoint}',json=data)
    response_body = response.json()
    assert response.status_code==401
    assert response_body["message"] == "Enter a valid email or username and/or password."
    assert response_body["id"] == "api.user.login.invalid_credentials_email_username"
    


def test_try_login_in_deactivated_accont():
    login = os.environ.get('DEACTIVATED_USER_MAIL')
    password = os.environ.get('DEACTIVATED_USER_PASSWORD')
    data = {
        "login_id": login,
        "password": password
    }
    response = requests.post(url=f'{base_url}{test_endpoint}',json=data)
    response_body = response.json()
    assert response.status_code==401
    assert response_body["message"] == "Login failed because your account has been deactivated.  Please contact an administrator."
    assert response_body["id"] == "api.user.login.inactive.app_error"
    

def test_try_login_in_email_not_verified_accont():
    login = os.environ.get('NOT_ACTIVATED_USER_MAIL')
    password = os.environ.get('NOT_ACTIVATED_USER_PASSWORD')
    data = {
        "login_id": login,
        "password": password
    }
    response = requests.post(url=f'{base_url}{test_endpoint}',json=data)
    response_body = response.json()
    assert response.status_code==401
    assert response_body["message"] == "Login failed because email address has not been verified."
    assert response_body["id"] == "api.user.login.not_verified.app_error"

def test_try_login_inactive_auth_server():
    login = os.environ.get('ACTIVE_USER_MAIL')
    password = os.environ.get('ACTIVE_USER_PASSWORD')
    data = {
        "login_id": login,
        "password": password
    }
    response = requests.post(url=f'{base_url}{test_endpoint}',json=data)
    response_body = response.json()
    assert response.status_code==401
    assert response_body["message"] == "Enter a valid email or username and/or password."
    assert response_body["id"] == "api.user.login.invalid_credentials_email_username"
    