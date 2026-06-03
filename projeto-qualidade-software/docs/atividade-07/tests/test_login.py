#python -m pytest tests/test_login.py -v --headed
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_login_com_sucesso_pom(page):
    # Setup
    login_page = LoginPage(page)
    
    # Execução
    login_page.acessar()
    login_page.realizar_login("teste@email.com", "123456")

    # Asserção
    expect(login_page.verificar_sucesso()).to_be_visible()