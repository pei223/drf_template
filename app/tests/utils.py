from typing import Dict, List
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


def output_test_function(func):
    print(f"{'-' * 30}\n{func.__name__}\n{'-' * 30}")


def set_auth_token(client: APIClient, user_info: Dict[str, str]):
    data = {
        "email": user_info["email"],
        "password": user_info["password"],
    }
    token = client.post("/auth/login/", data).data["key"]
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)


def register_users(client: APIClient, user_info_ls: List[Dict[str, str]]):
    for user_info in user_info_ls:
        data = {
            "username": user_info["username"],
            "email": user_info["email"],
            "password1": user_info["password"],
            "password2": user_info["password"],
        }
        client.post("/auth/registration/", data=data)
