import requests
from ..utils.decorator import debug_out_decorator

BASE_URL = "http://localhost:8000"


def login_header(token: str):
    return {
        "Authorization": f"Token {token}"
    }


@debug_out_decorator
def signup(username: str, email: str, password: str):
    url = f"{BASE_URL}/auth/registration/"
    data = {
        "username": username,
        "email": email,
        "password1": password,
        "password2": password,
    }
    return requests.post(url=url, data=data)


@debug_out_decorator
def login(email: str, password: str):
    url = f"{BASE_URL}/auth/login/"
    data = {
        "email": email,
        "password": password,
    }
    return requests.post(url=url, data=data)


@debug_out_decorator
def delete_user(token: str):
    url = f"{BASE_URL}/auth/destroy/"
    return requests.post(url=url, headers=login_header(token))


@debug_out_decorator
def get_user_info(token: str):
    url = f"{BASE_URL}/auth/user/"
    return requests.get(url=url, headers=login_header(token))


@debug_out_decorator
def register_blog(token: str, title: str, description: str):
    url = f"{BASE_URL}/api/blog/"
    return requests.post(url=url, data={"title": title, "description": description}, headers=login_header(token))


@debug_out_decorator
def get_blog_list():
    url = f"{BASE_URL}/api/blog/"
    return requests.get(url=url)


@debug_out_decorator
def delete_blog(token: str):
    url = f"{BASE_URL}/api/blog/"
    return requests.delete(url=url, headers=login_header(token))


@debug_out_decorator
def find_blog(blog_id: int):
    url = f"{BASE_URL}/api/blog/"
    return requests.get(url=url, params={"id": blog_id})


@debug_out_decorator
def search_blog(keyword: str):
    url = f"{BASE_URL}/api/blog/"
    return requests.get(url=url, params={"title": keyword})


@debug_out_decorator
def update_blog(token: str, blog_id: int, title: str, description: str):
    url = f"{BASE_URL}/api/blog/{blog_id}/"
    return requests.put(url=url, data={"title": title, "description": description}, headers=login_header(token))


@debug_out_decorator
def comments_of_blog(blog_id: int):
    url = f"{BASE_URL}/api/comment/"
    return requests.get(url=url, params={"blog_id": blog_id})


@debug_out_decorator
def register_comment(blog_id: int, name: str, comment: str):
    url = f"{BASE_URL}/api/comment/"
    return requests.post(url=url, data={"blog_id": blog_id, "name": name, "comment": comment})
