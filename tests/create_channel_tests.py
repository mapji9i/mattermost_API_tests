import os
import pytest
import requests



base_url = os.environ.get('BASE_URL')

test_endpoint="channels"

token=os.environ.get('TEST_USER_TOKEN')

user_id=os.environ.get('TEST_USER_ID')

headers= {"Authorization": "Bearer "+token }

team_id=os.environ.get('TEST_TEAM_ID')

test_channel_name="test_channel"

data = {
        "team_id": team_id,
        "name": test_channel_name,
        "display_name": "test_channel",
        "purpose": "test",
        "header": "my_channel",
        "type": "P"
    }


@pytest.fixture()
def resource():
    yield 
    delete_created_channel()

    
def test_try_create_channel():
    print(f'{base_url}{test_endpoint}')
    response = requests.post(url=f'{base_url}{test_endpoint}',json=data, headers=headers)
    
    response_body = response.json()
    pytest.created_channel_id=response_body["id"]

    assert response.status_code==201
    assert response_body["team_id"]==team_id
    assert response_body["display_name"]==data["display_name"]
    assert response_body["name"]==data["name"]
    assert response_body["purpose"]==data["purpose"]
    assert response_body["header"]==data["header"]

def test_try_create_existed_channel():
    
    response = requests.post(url=f'{base_url}{test_endpoint}',json=data, headers=headers)
    
    response_body = response.json()

    assert response.status_code==400
    assert response_body["id"]=="store.sql_channel.save_channel.exists.app_error"
    assert response_body["message"]=="A channel with that name already exists on the same team."

def delete_created_channel():
    response = requests.get(url=f'{base_url}{test_endpoint}',headers=headers)
    response_body = response.json()
    for i in range(len(response_body)):
        if(response_body[i]["name"]==test_channel_name):
            requests.delete(url=f'{base_url}{test_endpoint}/{response_body[i]["id"]}',headers=headers)
            break




    
