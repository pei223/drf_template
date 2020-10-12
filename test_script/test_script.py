from accessor import *

if __name__ == "__main__":
    user1 = {
        "username": "hoge",
        "email": "hoge@hoge.hoge",
        "password": "hogehoge"
    }
    user2 = {
        "username": "newuser",
        "email": "address@sample.com",
        "password": "yourpassword"
    }
    user_delete = {
        "username": "delete",
        "email": "delete@sample.com",
        "password": "deletedelete"
    }

    signup(**user1)
    signup(**user2)
    signup(**user_delete)

    get_blog_list()

    auth_token1 = login(user1["email"], user1["password"])
    auth_token2 = login(user2["email"], user2["password"])
    auth_token_del = login(user_delete["email"], user_delete["password"])


    get_user_info(auth_token1)
    get_user_info(auth_token2)
    get_user_info(auth_token_del)


    delete_user(auth_token_del)
    # register_blog(token=auth_token, title="hoge", description="hoge aaaaaaaaaaaaaaa")
    # register_blog(token=auth_token, title="test1", description="aaaaaaaaaaaaaaa")
    # register_blog(token=auth_token, title="test2", description="aaaaaaaaaaaaaaa")
    # register_blog(token=auth_token, title="aaaaaaaaatestbbbbbbbbbb", description="aaaaaaaaaaaaaaa")
    # print(search_blog("test"))
    # print(get_blog_list())
    # print(update_blog(auth_token, 10, title="update title", description="test description"))
    # print(find_blog(1))
    # register_comment(1, "hoge name", "test comment")
    # register_comment(1, "aaa", "test comment")
    # print(comments_of_blog(1))
