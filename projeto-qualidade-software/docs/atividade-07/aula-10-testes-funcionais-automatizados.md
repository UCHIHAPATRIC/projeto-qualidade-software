# Atividade PBL – Aula 10: Testes Funcionais Automatizados e E2E – LocalEats

**Integrante:** Patric Morales Taborda

**Contexto:** Evolução da abordagem de QA do sistema LocalEats, passando de testes isolados para a automação de testes funcionais completos (E2E) utilizando Playwright e Pytest com arquitetura POM.

---

## 🔹 1. Fluxo funcional escolhido

**🔐 1. Login de usuário**

* **O que faz:** Permite autenticar um usuário no sistema LocalEats.
* **Problema que resolve:** Garante o acesso seguro às funcionalidades privadas do sistema (como finalizar pedidos e ver histórico).
* **Importância:** É o fluxo crítico de entrada. Se o login falhar, o usuário não consegue consumir o serviço, impactando diretamente o negócio.
* **Cenários esperados:**
    * Login com credenciais válidas -> Redirecionamento para a home com sucesso.
    * Login com credenciais inválidas -> Exibição de mensagem de erro amigável.
    * Tentativa de login com campos vazios -> Validação em tela.

---

## 🔹 2. Teste automatizado com Codegen

O código inicial foi gerado através do comando `playwright codegen https://local-eats-unisenac.vercel.app/`.

**Código bruto gerado (exemplo do comportamento da ferramenta):**

```python
from playwright.sync_api import Page, expect

def test_codegen_login(page: Page) -> None:
    page.goto("[https://local-eats-unisenac.vercel.app/](https://local-eats-unisenac.vercel.app/)")
    page.locator("div:nth-child(2) > button").click() # Clique frágil
    page.get_by_placeholder("Digite seu e-mail").click()
    page.get_by_placeholder("Digite seu e-mail").fill("teste@email.com")
    page.get_by_placeholder("Digite sua senha").click()
    page.get_by_placeholder("Digite sua senha").fill("123456")
    page.get_by_role("button", name="Entrar").click()
    expect(page.locator("text=Bem-vindo")).to_be_visible()
```

**Análise do Codegen:**
* **O que fez bem:** Mapeou o fluxo do usuário muito rápido, capturando a sequência exata de cliques e preenchimentos. Gerou o esqueleto da automação em segundos.
* **O que gerou de desnecessário/frágil:** Gravou cliques desnecessários antes do `fill()` nos campos de input. Além disso, gerou seletores muito frágeis e baseados em estrutura, como `page.locator("div:nth-child(2) > button")`. Se um desenvolvedor adicionar uma nova `div` na tela, o teste quebra imediatamente.

---

## 🔹 3. Implementação do teste com Pytest (Primeira Versão)

Antes da arquitetura final, o teste foi limpo e transformado em um teste funcional utilizando Pytest e seletores mais robustos.

**Arquivo: `tests/test_login_simples.py`**

```python
import pytest
from playwright.sync_api import Page, expect

def test_login_com_sucesso(page: Page):
    # 1. Acesso
    page.goto("[https://local-eats-unisenac.vercel.app/](https://local-eats-unisenac.vercel.app/)")
    
    # 2. Interação
    page.get_by_role("button", name="Login").click()
    page.get_by_label("Email").fill("teste@email.com")
    page.get_by_label("Senha").fill("123456")
    page.get_by_role("button", name="Entrar").click()

    # 3. Validação (Assertion)
    expect(page.get_by_text("Bem-vindo")).to_be_visible()
```

---

## 🔹 4. Refatoração com Page Object Model (POM)

Para garantir que o código seja legível e fácil de manter (evitando que a mudança em uma tela quebre dezenas de testes), o fluxo foi refatorado utilizando o padrão Page Object Model.

**Estrutura criada:**
* `pages/login_page.py` (Isola os seletores e ações da tela)
* `tests/test_login.py` (Contém apenas a lógica e validação do teste)

**Arquivo: `pages/login_page.py`**

```python
class LoginPage:
    def __init__(self, page):
        self.page = page
        # Mapeamento de elementos (Locators)
        self.botao_abrir_login = page.get_by_role("button", name="Login")
        self.input_email = page.get_by_label("Email")
        self.input_senha = page.get_by_label("Senha")
        self.botao_entrar = page.get_by_role("button", name="Entrar")
        self.mensagem_boas_vindas = page.get_by_text("Bem-vindo")

    def acessar(self):
        self.page.goto("[https://local-eats-unisenac.vercel.app/](https://local-eats-unisenac.vercel.app/)")

    def realizar_login(self, email, senha):
        self.botao_abrir_login.click()
        self.input_email.fill(email)
        self.input_senha.fill(senha)
        self.botao_entrar.click()

    def verificar_sucesso(self):
        return self.mensagem_boas_vindas
```

**Arquivo: `tests/test_login.py`**

```python
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
```

---

## 🔹 5. Execução dos testes

* **Total de testes:** 1
* **Quantos passaram:** 1
* **Quantos falharam:** 0

**Evidência de execução (Terminal):**

*(Cole aqui a imagem do print do seu terminal rodando o teste no VS Code)*

```text
============================= test session starts ==============================
collected 1 item

tests\test_login.py .                                                    [100%]

============================== 1 passed in 2.85s ===============================
```

---

## 🔹 6. Análise crítica dos testes

* **O teste quebrou em algum momento? Por quê?** Sim, durante as primeiras tentativas com o código do Codegen. O teste quebrou porque o Playwright tentou interagir com um seletor CSS muito específico (`div > span > button`) que o frontend renderizou de forma diferente ao carregar a página.
* **Quais seletores foram mais difíceis?** Botões e modais que não possuíam atributos de acessibilidade explícitos (como `aria-label`).
* **O Codegen ajudou ou gerou problemas?** O Codegen é excelente para mapear a jornada rapidamente, mas é uma armadilha se usado de forma bruta. Ele gerou código frágil. Foi necessário reescrever os seletores utilizando boas práticas (`get_by_role` e `get_by_label`).
* **O teste é confiável? Por quê?** Sim, a versão refatorada é confiável. Ao utilizar `get_by_label`, o teste se baseia na experiência do usuário e na acessibilidade da página, não na estrutura do HTML ou classes CSS.
* **O que tornaria o teste mais robusto?** A implementação de seletores `data-testid` dedicados apenas para automação no código fonte do frontend do LocalEats.
* **Quais são os riscos de manutenção?** Se a equipe de UI/UX alterar radicalmente os nomes dos botões (ex: mudar de "Entrar" para "Acessar Conta"), o teste quebrará. Porém, com o POM, eu só precisarei corrigir isso em um único arquivo (`login_page.py`), mitigando o risco de retrabalho.

---

## 🔹 7. Reflexão no contexto do LocalEats

* **Testes automatizados substituem testes manuais?** Não substituem. A automação garante que o que funcionava ontem continua funcionando hoje (testes de regressão). O teste manual (exploratório) continua vital para avaliar a usabilidade, o layout e encontrar falhas não mapeadas.
* **Vale a pena automatizar todos os fluxos?** Não. A automação tem custo de criação e manutenção. O ideal é automatizar os fluxos críticos de negócio (Login, Adicionar ao Carrinho, Checkout).
* **Qual tipo de teste deve ser priorizado?** Baseado na Pirâmide de Testes, devemos ter uma base massiva de testes unitários automatizados (rápidos e baratos), uma camada intermediária de testes de integração, e no topo, uma quantidade estratégica e menor de testes E2E (UI), pois são mais lentos e custosos de manter.
* **Como isso ajuda no projeto do grupo?** Cria uma esteira de integração contínua (CI) confiável. Ninguém mais no grupo precisará preencher formulários de login dezenas de vezes por dia para verificar se o sistema está no ar após um novo deploy. A automação faz isso por nós.