import os
import pytest
import requests

base_url = os.environ.get('BASE_URL')


token=os.environ.get('TEST_USER_TOKEN')

user_id=os.environ.get('TEST_USER_ID')

channel_id=os.environ.get('TEST_CHANNEL_ID')


headers= {
    "Authorization": "Bearer "+token 
}

def test_try_to_create_post():
    data={
          "channel_id": channel_id,
          "message": "Test_message"
    }
    response = requests.post(url=f'{base_url}posts',json=data, headers=headers)
    
    response_body = response.json()
    ##pytest.created_post_ids.append(response_body["id"])
    assert response.status_code==201
    assert response_body["message"]==data["message"]
    assert response_body["channel_id"]==data["channel_id"]
    assert response_body["user_id"]==user_id


def test_try_to_get_all_posts():

    response = requests.get(url=f'{base_url}/channels/{channel_id}/posts',headers=headers)
    
    response_body = response.json()

    assert response.status_code==200
    #Требуется глобальная переменная
    assert response_body["posts"]["6z3crc8jgjy9iyznuczz61ixir"]["message"]=="Test_message"
