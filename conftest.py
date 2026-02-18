import pytest
from pages.login_page import LoginPage

@pytest.fixture
def page(page):
    page.goto("https://leogcarvalho.github.io/simulabank/login")
    return page

@pytest.fixture
def login_page(page):
    return LoginPage(page)