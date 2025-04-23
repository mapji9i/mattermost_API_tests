import os
import pytest
import requests


base_url = os.environ.get('BASE_URL')

test_endpoint="/posts"

token=os.environ.get('TEST_USER_TOKEN')

user_id=os.environ.get('TEST_USER_ID')

channel_id=os.environ.get('TEST_CHANNEL_ID')

test_endpoint=f'channels/{channel_id}/members'

headers= {"Authorization": "Bearer "+token }

user_ids=[ os.environ.get('TEST_USER_ID2'),
    os.environ.get('TEST_USER_ID3')]



def test_try_to_add_two_users():
    data={
          "user_ids": user_ids
    }
   
    response = requests.post(url=f'{base_url}{test_endpoint}',json=data, headers=headers)
    
    response_body = response.json()
    print(response_body)
 
    assert response.status_code==201
    assert response_body[0]["user_id"]==user_ids[0]
    assert response_body[1]["user_id"]==user_ids[1]

def test_try_to_delete_some_user():

    response = requests.delete(url=f'{base_url}{test_endpoint}/{user_ids[0]}',headers=headers)
    assert response.status_code==200
    response = requests.get(url=f'{base_url}{test_endpoint}',headers=headers)
    response_body = response.json()
    assert response.status_code==200
    assert len(response_body)==2
    assert response_body[1]["user_id"]==user_id
    assert response_body[0]["user_id"]==user_ids[1]
    