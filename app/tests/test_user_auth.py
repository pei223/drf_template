from typing import Dict
from .accessor import *
from rest_framework.test import APIClient, APITestCase
from .utils import *


class TestUserAuth(APITestCase):
    def setUp(self):
        self.exist_user1 = {
            "username": "hoge",
            "email": "hoge@hoge.hoge",
            "password": "hogehoge",
        }
        self.user_delete = {
            "username": "delete",
            "email": "delete@sample.com",
            "password": "deletedelete",
        }
        self.user_unknown = {
            "username": "unknown",
            "email": "unknown@sample.com",
            "password": "unknownunknown",
        }
        self.client = APIClient()

    def _user_info_for_register(self, user_info: Dict):
        return {
            "username": user_info["username"],
            "email": user_info["email"],
            "password1": user_info["password"],
            "password2": user_info["password"],
        }

    def _login_value(self, user_info: Dict):
        return {
            "email": user_info["email"],
            "password": user_info["password"]
        }

    def test_01_signup(self):
        output_test_function(self.test_01_signup)
        response1 = self.client.post("/auth/registration/", data=self._user_info_for_register(self.exist_user1))
        response_del = self.client.post("/auth/registration/", data=self._user_info_for_register(self.user_delete))

        assert response1.status_code > 300, f"Exist Signup: \n[{response1.status_code}]: {response1.data}"
        assert response_del.status_code < 300, f"Signup: \n[{response_del.status_code}]: {response_del.data}"

    def test_02_login(self):
        output_test_function(self.test_02_login)

        register_users(self.client, [self.exist_user1, self.user_delete])

        res1 = self.client.post("/auth/login/", self._login_value(self.exist_user1))
        res2 = self.client.post("/auth/login/", self._login_value(self.user_delete))
        assert res1.status_code < 300, f"User info: \n[{res1.status_code}]: {res1.data}"
        assert res2.status_code < 300, f"User info: \n[{res2.status_code}]: {res2.data}"

    def test_03_user_info(self):
        output_test_function(self.test_03_user_info)

        register_users(self.client, [self.exist_user1, self.user_delete])

        set_auth_token(self.client, self.exist_user1)
        res1 = self.client.get("/auth/user/")

        set_auth_token(self.client, self.user_delete)
        res_del = self.client.get("/auth/user/")

        assert res1.status_code < 300, f"User info: \n[{res1.status_code}]: {res1.data}"
        assert res_del.status_code < 300, f"User info: \n[{res_del.status_code}]: {res_del.data}"

    def test_09_delete(self):
        output_test_function(self.test_09_delete)

        register_users(self.client, [self.user_delete, ])
        set_auth_token(self.client, self.user_delete)

        response = self.client.post("/auth/destroy/")

        assert response.status_code < 300, f"Delete user: \n[{response.status_code}]: {response.data}"

        response = self.client.post("/auth/login/", self._login_value(self.user_delete))
        assert response.status_code >= 300, f"Not exists user: \n[{response.status_code}]: {response.data}"
