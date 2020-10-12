from typing import Dict
from django.test import TestCase
from .accessor import *
from rest_framework.test import APIClient, APITestCase
from .utils import *


class TestBlogComment(APITestCase):
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
        ]

        self.test_comments = [
            {
                "blog_id": 1,
                "name": "hogehoge",
                "comment": "test comment"
            },
            {
                "blog_id": 2,
                "name": "hogehoge",
                "comment": "test comment"
            },
            {
                "blog_id": 2,
                "name": "hogehoge",
                "comment": "test comment"
            },
            {
                "blog_id": 2,
                "name": "hogehoge",
                "comment": "test comment"
            },
            {
                "blog_id": 1,
                "name": "hogehoge",
                "comment": "test comment"
            }
        ]

        self.client = APIClient()

    def _register_blogs(self):
        register_users(self.client, [self.user1, self.user2, ])
        for i, test_datum in enumerate(self.test_data):
            user = self.user1 if i % 2 == 0 else self.user2
            set_auth_token(self.client, user)
            self.client.post("/api/blog/", data=test_datum)

    def _register_comments(self):
        for comment in self.test_comments:
            self.client.post("/api/comment/", data=comment)

    def test_01_register(self):
        output_test_function(self.test_01_register)
        register_users(self.client, [self.user1, self.user2, ])
        self._register_blogs()

        res = self.client.post("/api/comment/", data=self.test_comments[0])
        assert res.status_code < 300, f"Register comment: \n[{res.status_code}]: {res.data}"

        set_auth_token(self.client, self.user2)
        res = self.client.post("/api/comment/", data=self.test_comments[2])
        assert res.status_code < 300, f"Register comment: \n[{res.status_code}]: {res.data}"

    def test_02_register_comment_of_invalid_blog(self):
        output_test_function(self.test_02_register_comment_of_invalid_blog)

        self._register_blogs()

        res = self.client.post("/api/comment/", data={"blog_id": 999, "name": "aaa", "comment": "hoge"})
        assert res.status_code >= 300, f"Register invalid comment: \n[{res.status_code}]: {res.data}"

    def test_03_comment_list_of_blog(self):
        output_test_function(self.test_03_comment_list_of_blog)
        self._register_blogs()
        self._register_comments()
        res = self.client.get("/api/comment/", data={"blog_id": 1})
        assert res.status_code < 300 and len(res.data) == 2, f"Comment list: \n[{res.status_code}]: {res.data}"

        res = self.client.get("/api/comment/", data={"blog_id": 2})
        assert res.status_code < 300 and len(res.data) == 3, f"Comment list: \n[{res.status_code}]: {res.data}"

    # def test_04_invalid_search(self):
    #     output_test_function(self.test_04_invalid_search)
    #     self._register_blogs()
    #     self._register_comments()
    #     res = self.client.get("/api/comment/", data={"id": 1})
    #     assert res.status_code < 300 and len(res.data) == 1, f"Blog list: \n[{res.status_code}]: {res.data}"
    #
    # def test_05_update(self):
    #     output_test_function(self.test_05_update)
    #     self._register_blogs()
    #     res = self.client.get("/api/blog/", data={"title": "test"})
    #     assert res.status_code < 300 and len(res.data) == 2, f"Blog search1: \n[{res.status_code}]: {res.data}"
    #     res = self.client.get("/api/blog/", data={"title": "testtest"})
    #     assert res.status_code < 300 and len(res.data) == 0, f"Blog search2: \n[{res.status_code}]: {res.data}"
    #
    # def test_06_delete(self):
    #     output_test_function(self.test_06_delete)
    #     self._register_blogs()
    #     res = self.client.get("/api/blog/", data={"author": 1})
    #     assert res.status_code < 300 and len(res.data) == 3, f"Blog search1: \n[{res.status_code}]: {res.data}"
    #     res = self.client.get("/api/blog/", data={"author": 2})
    #     assert res.status_code < 300 and len(res.data) == 2, f"Blog search2: \n[{res.status_code}]: {res.data}"
