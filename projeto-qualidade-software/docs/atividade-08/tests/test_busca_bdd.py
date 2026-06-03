from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect

# 1. Carrega o arquivo de comportamento (Feature)
scenarios('../features/busca_restaurantes.feature')

# 2. Definição dos Passos (Steps)
@given('que o usuário está na página inicial do LocalEats')
def acessar_pagina_inicial(page: Page):
    # Vai para o site
    page.goto('https://local-eats-unisenac.vercel.app/')
    
    # Faz o login para libertar a tela de pesquisa
    page.get_by_role("textbox", name="teste@teste.com").fill("teste@email.com")
    page.get_by_role("textbox", name="Sua senha secreta").fill("123456")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()

@when('o usuário pesquisa por um restaurante válido')
def pesquisar_restaurante_valido(page: Page):
    # Usando o seletor exato que você descobriu no Codegen
    busca_input = page.get_by_role("textbox", name="Buscar por culinária ou")
    busca_input.fill("Pizza")
    page.get_by_role("button", name="Buscar").click()

@when('o usuário pesquisa por um restaurante que não existe')
def pesquisar_restaurante_invalido(page: Page):
    busca_input = page.get_by_role("textbox", name="Buscar por culinária ou")
    busca_input.fill("Comida de Marte")
    page.get_by_role("button", name="Buscar").click()

@then('o sistema deve exibir os restaurantes correspondentes na listagem')
def validar_busca_sucesso(page: Page):
    # Valida que pelo menos um card ficou visível na tela
    expect(page.locator(".card, .restaurant-card").first).to_be_visible()

@then('o sistema não deve exibir nenhum card de restaurante')
def validar_busca_vazia(page: Page):
    # Valida que a tela não achou nenhum card
    expect(page.locator(".card, .restaurant-card")).to_have_count(0)