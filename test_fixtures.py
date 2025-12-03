import pytest


@pytest.fixture
def login_page(browser):
    print("Страница ввода логина")
    pass



@pytest.fixture
def user():
    print("Юзверь")
    return "username", "password"


def test_login1(login_page, user):
    print("Логин1")
    username, password = user
    assert username == "username"
    assert password == "password"


def test_login(login_page, user):
    print("Логин2")
    username, password = user
    assert username == "username"
    assert password == "password"

