#python -m pytest tests/test_login.py -v --headed --slowmo 1000
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.input_email = page.get_by_role("textbox", name="teste@teste.com")
        self.input_senha = page.get_by_role("textbox", name="Sua senha secreta")
        self.botao_entrar = page.locator("#loginForm").get_by_role("button", name="Entrar")
        self.mensagem_boas_vindas = page.get_by_text("Bem-vindo")

    def acessar(self):
        self.page.goto("https://local-eats-unisenac.vercel.app/static/login.html")

    def realizar_login(self, email, senha):
        self.input_email.fill(email)
        self.input_senha.fill(senha)
        self.botao_entrar.click()

    def verificar_sucesso(self):
        return self.mensagem_boas_vindas