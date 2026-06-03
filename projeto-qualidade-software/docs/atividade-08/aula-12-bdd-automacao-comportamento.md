# Atividade PBL – Aula 12: BDD e Automação Orientada a Comportamento – LocalEats

**Integrante:** Patric Morales Taborda

**Contexto:** Evolução da garantia de qualidade (QA) do sistema LocalEats. A transição da automação puramente técnica para a Automação Orientada a Comportamento (BDD) utilizando Gherkin, pytest-bdd e Playwright.

---

## 🔹 1. Fluxo funcional escolhido

**🔎 1. Busca de restaurantes**

* **O que faz:** Permite que o usuário pesquise ativamente por restaurantes ou tipos de culinária específicos.
* **Problema que resolve:** Elimina a necessidade de o usuário rolar por listagens infinitas, facilitando a descoberta rápida e direta.
* **Importância:** É um fluxo central para a conversão e retenção do usuário. Se a busca falhar, o usuário abandona a plataforma.
* **Cenários esperados:**
    * Busca válida retorna os *cards* de restaurantes correspondentes.
    * Busca por termo inexistente não retorna elementos e/ou exibe mensagem de lista vazia.

---

## 🔹 2. Escrita dos cenários BDD

Abaixo estão os cenários de negócio traduzidos para a sintaxe Gherkin, documentando o comportamento esperado de forma ubíqua (compreensível para Negócios, QA e Desenvolvimento).

**Arquivo:** `features/busca_restaurantes.feature`

```gherkin
Feature: Busca de restaurantes
  Como um usuário do LocalEats
  Quero poder buscar restaurantes por nome
  Para encontrar rapidamente opções de refeição que me agradam

  Scenario: Busca por um restaurante existente
    Given que o usuário está na página inicial do LocalEats
    When o usuário pesquisa por um restaurante válido
    Then o sistema deve exibir os restaurantes correspondentes na listagem

  Scenario: Busca por um restaurante inexistente
    Given que o usuário está na página inicial do LocalEats
    When o usuário pesquisa por um restaurante que não existe
    Then o sistema não deve exibir nenhum card de restaurante
```

---

## 🔹 3. Implementação da automação com pytest-bdd

Os passos de negócio foram mapeados para ações reais de interface utilizando o Playwright.

**Arquivo:** `tests/test_busca_bdd.py`

```python
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect

scenarios('../features/busca_restaurantes.feature')

@given('que o usuário está na página inicial do LocalEats')
def acessar_pagina_inicial(page: Page):
    page.goto('[https://local-eats-unisenac.vercel.app/](https://local-eats-unisenac.vercel.app/)')

@when('o usuário pesquisa por um restaurante válido')
def pesquisar_restaurante_valido(page: Page):
    busca_input = page.locator("input[type='search'], input[placeholder*='Buscar']")
    busca_input.fill("Pizza")
    page.keyboard.press("Enter")

@when('o usuário pesquisa por um restaurante que não existe')
def pesquisar_restaurante_invalido(page: Page):
    busca_input = page.locator("input[type='search'], input[placeholder*='Buscar']")
    busca_input.fill("Comida de Marte")
    page.keyboard.press("Enter")

@then('o sistema deve exibir os restaurantes correspondentes na listagem')
def validar_busca_sucesso(page: Page):
    expect(page.locator(".card, .restaurant-card").first).to_be_visible()

@then('o sistema não deve exibir nenhum card de restaurante')
def validar_busca_vazia(page: Page):
    expect(page.locator(".card, .restaurant-card")).to_have_count(0)
```

---

## 🔹 4. Organização do projeto

O projeto foi organizado separando estritamente os requisitos de negócio da implementação técnica:

```text
projeto/
│
├── features/
│   └── busca_restaurantes.feature     # Regras de negócio legíveis
├── tests/
│   └── test_busca_bdd.py              # Implementação da automação técnica
└── pytest.ini                         # Configuração de caminhos do runner
```

---

## 🔹 5. Execução dos testes

* **Total de cenários:** 2
* **Quantos passaram:** 2
* **Quantos falharam:** 0

**Evidência da execução:**

*(Print do terminal anexado abaixo)*
![Evidencia BDD](evidencia-bdd.png)

---

## 🔹 6. Análise crítica

* **O cenário escrito ficou compreensível?** Sim. Utilizar Gherkin obrigou a remoção de termos técnicos (como "clicar no botão id #btn-search") e focou no objetivo da ação. Uma pessoa de fora da TI conseguiria ler e validar se a regra está correta.
* **O teste automatizado ficou legível?** Muito mais limpo. O uso de decoradores (`@given`, `@when`, `@then`) cria uma ponte perfeita entre o texto em português e a função Python, modularizando as responsabilidades.
* **O BDD ajudou a entender o comportamento?** Sim, forçou a equipe a pensar no "Porquê" e no "O Quê" antes de pensar no "Como" automatizar.
* **Quais dificuldades surgiram?** O maior desafio inicial foi mapear corretamente o caminho do arquivo `.feature` dentro do `.py` e garantir que o texto do decorador fosse uma cópia idêntica do escrito no Gherkin. Letras maiúsculas ou espaços extras causam erros de Step não encontrado.
* **Os seletores foram frágeis? O teste ficou dependente da interface?** A camada técnica (Python/Playwright) continua dependente do HTML. Se a classe do card mudar de `.card` para `.item-box`, o teste falha. No entanto, o **cenário de negócio** não é frágil; ele continua intocável.
* **O que tornaria o teste mais robusto?** Combinar BDD com o padrão Page Object Model (POM) já construído na atividade anterior. Os "Steps" do BDD apenas chamariam os métodos das páginas POM, isolando totalmente a manutenção de seletores.

---

## 🔹 7. Reflexão no contexto do LocalEats

* **BDD melhora a comunicação entre a equipe?** Absolutamente. Ele atua como uma linguagem ubíqua. O "Product Owner" pode escrever a *Feature*, o QA automatiza e o Desenvolvedor constrói a tela baseada no mesmo documento.
* **Todo teste deve ser escrito em BDD?** Não. Testes muito granulares (como validação de limite de caracteres de um campo, ou testes unitários de cálculo de carrinho) não geram valor em BDD. Apenas fluxos que representam regras de negócio importantes.
* **Quando vale a pena usar BDD?** Quando há ambiguidade nos requisitos ou quando a equipe precisa validar fluxos críticos de aceitação do usuário de ponta a ponta (E2E).
* **Como isso ajuda no projeto do grupo?** Cria uma "documentação viva" do LocalEats. Saberemos exatamente quais funcionalidades a aplicação entrega hoje, validadas automaticamente, sem precisar de documentações no Word que ficam rapidamente desatualizadas.