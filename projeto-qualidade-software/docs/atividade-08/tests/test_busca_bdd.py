from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect

# 1. Carrega o arquivo de comportamento (Feature)
scenarios('../features/busca_restaurantes.feature')


# 2. Definição dos Passos (Steps)

@given('que o usuário está na página inicial do LocalEats')
def acessar_pagina_inicial(page: Page):
    # Acessa direto a página de login para garantir
    page.goto('https://local-eats-unisenac.vercel.app/static/login.html')
    
    # Usa EXATAMENTE o usuário fake que o professor configurou no sistema
    page.get_by_role("textbox", name="teste@teste.com").fill("teste@email.com")
    page.get_by_role("textbox", name="Sua senha secreta").fill("123456")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()

@when('o usuário pesquisa por um restaurante válido')
def pesquisar_restaurante_valido(page: Page):
    # Usa o seletor mapeado pelo Codegen e busca por uma categoria existente (Japonesa)
    busca_input = page.get_by_role("textbox", name="Buscar por culinária ou")
    busca_input.fill("Japonesa")
    page.get_by_role("button", name="Buscar").click()


@when('o usuário pesquisa por um restaurante que não existe')
def pesquisar_restaurante_invalido(page: Page):
    # Busca por um termo sabidamente inexistente para validar o fluxo alternativo
    busca_input = page.get_by_role("textbox", name="Buscar por culinária ou")
    busca_input.fill("Comida de Marte")
    page.get_by_role("button", name="Buscar").click()


@then('o sistema deve exibir os restaurantes correspondentes na listagem')
def validar_busca_sucesso(page: Page):
    # Valida a presença de elementos que apontam para a página interna dos restaurantes
    expect(page.locator("a[href*='restaurant.html']").first).to_be_visible()


@then('o sistema não deve exibir nenhum card de restaurante')
def validar_busca_vazia(page: Page):
    # Garante que a contagem de links de restaurantes na listagem seja exatamente zero
    expect(page.locator("a[href*='restaurant.html']")).to_have_count(0)