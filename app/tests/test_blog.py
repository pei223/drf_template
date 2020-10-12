from typing import Dict
from django.test import TestCase
from .accessor import *
from rest_framework.test import APIClient, APITestCase
from .utils import *


class TestBlog(APITestCase):
    def setUp(self):
        self.user1 = {
            "username": "hoge",
            "email": "hoge@hoge.hoge",
            "password": "hogehoge",
        }
        self.user2 = {
            "username": "fuga",
            "email": "fuga@fuga.fuga",
            "password": "fugafuga",
        }

        self.test_data = [
            {
                "title": "title 1",
                "description": "test description1"
            },
            {
                "title": "test1",
                "description": "Test description           test"
            },
            {
                "title": "hogehoge",
                "description": "hogehogehogehoge"
            },
            {
                "title": "test2",
                "description": "Test description"
            },
            {
                "title": "fuga",
                "description": "fugafuga"
            },
        ]

        self.client = APIClient()

    def _register_test_data(self):
        register_users(self.client, [self.user1, self.user2, ])
        for i, test_datum in enumerate(self.test_data):
            user = self.user1 if i % 2 == 0 else self.user2
            set_auth_token(self.client, user)
            self.client.post("/api/blog/", data=test_datum)

    def test_01_register(self):
        output_test_function(self.test_01_register)
        register_users(self.client, [self.user1, self.user2, ])

        res1 = self.client.post("/api/blog/", data=self.test_data[0])
        assert res1.status_code >= 300, f"Register blog1 Not login: \n[{res1.status_code}]: {res1.data}"

        set_auth_token(self.client, self.user1)
        res1 = self.client.post("/api/blog/", data=self.test_data[0])
        res2 = self.client.post("/api/blog/", data=self.test_data[1])
        assert res1.status_code < 300, f"Register blog1 User1: \n[{res1.status_code}]: {res1.data}"
        assert res2.status_code < 300, f"Register blog2 User1: \n[{res2.status_code}]: {res2.data}"

        set_auth_token(self.client, self.user2)
        res1 = self.client.post("/api/blog/", data=self.test_data[2])
        res2 = self.client.post("/api/blog/", data=self.test_data[3])
        assert res1.status_code < 300, f"Register blog1 User2: \n[{res1.status_code}]: {res1.data}"
        assert res2.status_code < 300, f"Register blog2 User2: \n[{res2.status_code}]: {res2.data}"

    def test_02_list(self):
        output_test_function(self.test_02_list)
        self._register_test_data()
        res = self.client.get("/api/blog/")
        assert res.status_code < 300 and len(res.data) == len(
            self.test_data), f"Blog list: \n[{res.status_code}]: {res.data}"

    def test_03_find(self):
        output_test_function(self.test_03_find)
        self._register_test_data()
        res = self.client.get("/api/blog/", data={"id": 1})
        assert res.status_code < 300 and len(res.data) == 1, f"Blog list: \n[{res.status_code}]: {res.data}"
        res = self.client.get("/api/blog/", data={"id": 3})
        assert res.status_code < 300 and len(res.data) == 1, f"Blog list: \n[{res.status_code}]: {res.data}"

    def test_04_keyword_search(self):
        output_test_function(self.test_04_keyword_search)
        self._register_test_data()
        res = self.client.get("/api/blog/", data={"title": "test"})
        assert res.status_code < 300 and len(res.data) == 2, f"Blog search1: \n[{res.status_code}]: {res.data}"
        res = self.client.get("/api/blog/", data={"title": "testtest"})
        assert res.status_code < 300 and len(res.data) == 0, f"Blog search2: \n[{res.status_code}]: {res.data}"

    def test_05_user_search(self):
        output_test_function(self.test_05_user_search)
        self._register_test_data()
        res = self.client.get("/api/blog/", data={"author": 1})
        assert res.status_code < 300 and len(res.data) == 3, f"Blog search1: \n[{res.status_code}]: {res.data}"
        res = self.client.get("/api/blog/", data={"author": 2})
        assert res.status_code < 300 and len(res.data) == 2, f"Blog search2: \n[{res.status_code}]: {res.data}"

    def test_06_update(self):
        output_test_function(self.test_06_update)
        self._register_test_data()
        set_auth_token(self.client, self.user1)
        blog_id = 1
        update_res = self.client.put(f"/api/blog/{blog_id}/", data={"title": "new title"})
        assert update_res.status_code < 300, f"Blog update1: \n[{update_res.status_code}]: {update_res.data}"
        res = self.client.get("/api/blog/", data={"id": blog_id})
        assert res.status_code < 300 and res.data[0][
            "title"] == "new title", f"Blog update1(find): \n[{res.status_code}]: {res.data}"

    def test_07_update_not_own_blog(self):
        output_test_function(self.test_07_update_not_own_blog)
        self._register_test_data()
        set_auth_token(self.client, self.user2)
        blog_id = 1
        update_res = self.client.put(f"/api/blog/{blog_id}/", data={"title": "new title"})
        assert update_res.status_code >= 300, f"Blog update2(other user): \n[{update_res.status_code}]: {update_res.data}"
        res = self.client.get("/api/blog/", data={"id": blog_id})
        assert res.status_code < 300 and res.data[0][
            "title"] == self.test_data[0]["title"], f"Blog update2(find): \n[{res.status_code}]: {res.data}"

    def test_08_delete(self):
        output_test_function(self.test_08_delete)
        self._register_test_data()
        set_auth_token(self.client, self.user2)
        blog_id = 2
        res = self.client.delete(f"/api/blog/{blog_id}/")
        assert res.status_code < 300, f"Blog delete: \n[{res.status_code}]: {res.data}"
        res = self.client.get("/api/blog/", data={"id": blog_id})
        assert res.status_code < 300 and len(res.data) == 0, f"Deleted blog search: \n[{res.status_code}]: {res.data}"

    def test_09_delete_not_own_blog(self):
        output_test_function(self.test_09_delete_not_own_blog)
        self._register_test_data()
        set_auth_token(self.client, self.user1)
        blog_id = 2
        res = self.client.delete(f"/api/blog/{blog_id}/")
        assert res.status_code >= 300, f"Blog delete(other): \n[{res.status_code}]: {res.data}"
        res = self.client.get("/api/blog/", data={"id": blog_id})
        assert res.status_code < 300 and len(
            res.data) == 1, f"Blog search(not deleted): \n[{res.status_code}]: {res.data}"
