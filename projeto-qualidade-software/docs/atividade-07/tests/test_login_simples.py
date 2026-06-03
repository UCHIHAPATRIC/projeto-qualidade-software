import pytest
from playwright.sync_api import Page, expect

def test_login_com_sucesso(page: Page):
    # 1. Acesso (indo direto para a página que o Codegen mapeou)
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    
    # 2. Interação (Usando os seletores exatos que descobrimos no Codegen)
    page.get_by_role("textbox", name="teste@teste.com").fill("teste@email.com")
    page.get_by_role("textbox", name="Sua senha secreta").fill("123456")
    
    # 3. Clica no botão de entrar específico do formulário de login
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()

    # 4. Validação
    # Aguarda a mensagem de Bem-vindo aparecer para confirmar o sucesso
    expect(page.get_by_text("Bem-vindo")).to_be_visible()