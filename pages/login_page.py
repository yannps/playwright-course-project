from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Usuário:")
        self.password_input = page.get_by_role("textbox", name="Senha:")
        self.login_button = page.get_by_role("button", name="Entrar")

    def login(self, user, password):
        self.username_input.fill(user)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_login_successful(self):
        expect(self.page.get_by_role("heading", name="Bem-vindo ao SimulaBank!")).to_be_visible()