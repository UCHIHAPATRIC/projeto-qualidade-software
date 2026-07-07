# Atividade PBL – Aula 17: Integração Contínua, Qualidade Automatizada e Defeitos – LocalEats

**Integrante:** Patric Morales Taborda

**Contexto:** Evolução do ciclo de vida de desenvolvimento do LocalEats. Transição de testes rodados localmente para um fluxo de Integração Contínua (CI) na nuvem, utilizando GitHub Actions. O objetivo é garantir que nenhuma alteração quebre o sistema antes de chegar à produção (Vercel), além de rastrear funcionalidades e bugs formalmente via GitHub Issues.

---

## 🔹 1. Repositório da Atividade

O repositório foi criado especificamente para isolar o ambiente de pipeline de Integração Contínua e execução automatizada.

| Item | Descrição |
| :--- | :--- |
| **Nome do repositório** | `localeats-ci-qa` |
| **Link do repositório** | `https://github.com/UCHIHAPATRIC/localeats-ci-qa` |

**Estrutura de diretórios utilizada:**

```text
localeats-ci-qa/
├── .github/
│   └── workflows/
│       └── ci-pipeline.yml
├── src/
│   └── app_busca.py
├── tests/
│   └── test_busca.py
└── README.md
```

---

## 🔹 2. Planejamento da Funcionalidade

A demanda foi mapeada e registrada no repositório antes do início do desenvolvimento.

| Item | Descrição |
| :--- | :--- |
| **Título da Issue** | `Feature: Busca de Restaurantes por Categoria` |
| **Objetivo da funcionalidade** | Permitir que o usuário filtre a lista de restaurantes digitando um tipo de culinária, retornando apenas os locais correspondentes à categoria pesquisada. |
| **Link da Issue** | `https://github.com/UCHIHAPATRIC/localeats-ci-qa/issues/1` |

---

## 🔹 3. Teste Automatizado

Foi criado um teste unitário focado na regra de negócio da busca para garantir que o filtro funcione corretamente em memória.

| Item | Descrição |
| :--- | :--- |
| **Tipo de teste** | Unitário (Pytest) |
| **Objetivo do teste** | Validar se a função de busca retorna os restaurantes corretos ao buscar um termo válido e se retorna uma lista vazia para termos inexistentes. |
| **Link para o arquivo** | `https://github.com/UCHIHAPATRIC/localeats-ci-qa/blob/main/tests/test_busca.py` |

**Código do teste criado:**

```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app_busca import buscar_restaurante

def test_busca_categoria_valida():
    restaurantes = ["Sushi Bar (Japonesa)", "Pizzaria Roma (Italiana)"]
    resultado = buscar_restaurante(restaurantes, "Japonesa")
    assert len(resultado) == 1
    assert resultado[0] == "Sushi Bar (Japonesa)"

def test_busca_categoria_invalida():
    restaurantes = ["Sushi Bar", "Pizzaria Roma"]
    resultado = buscar_restaurante(restaurantes, "Marciana")
    assert len(resultado) == 0
```

---

## 🔹 4. Pipeline de Integração Contínua

Foi configurado um Workflow para instalar as dependências e rodar o Pytest a cada novo *Push* na branch principal, barrando códigos quebrados.

| Item | Descrição |
| :--- | :--- |
| **Nome do workflow** | `CI - LocalEats Quality Check` |
| **Evento que dispara** | `push` na branch `main` |
| **Link para o arquivo** | `https://github.com/UCHIHAPATRIC/localeats-ci-qa/blob/main/.github/workflows/ci-pipeline.yml` |
| **Link de uma execução** | `https://github.com/UCHIHAPATRIC/localeats-ci-qa/actions` |

**Código do workflow (`.github/workflows/ci-pipeline.yml`):**

```yaml
name: CI - LocalEats Quality Check

on:
  push:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout do código
      uses: actions/checkout@v3

    - name: Configurar Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Instalar dependências
      run: |
        python -m pip install --upgrade pip
        pip install pytest

    - name: Executar testes automatizados
      run: |
        pytest tests/
```

---

## 🔹 5. Indicadores de Qualidade

Resultados extraídos diretamente da aba *Actions* após a execução bem-sucedida do workflow configurado.

| Indicador | Valor |
| :--- | :--- |
| **Quantidade de testes executados** | 2 |
| **Quantidade de testes aprovados** | 2 |
| **Quantidade de testes com falha** | 0 |
| **Status final do pipeline** | `Success` (Aprovado ✅) |

---

## 🔹 6. Registro de Defeito

Abaixo está o mapeamento formal de um erro simulado no processo, registrado via aba *Issues* do repositório.

| Item | Descrição |
| :--- | :--- |
| **Título do defeito** | `Bug: Busca falha ao usar letras minúsculas` |
| **Severidade** | Média |
| **Link da Issue** | `https://github.com/UCHIHAPATRIC/localeats-ci-qa/issues/2` |

**Qual foi o defeito, como foi identificado e como foi corrigido:**
O defeito consistia em não retornar nenhum restaurante quando o usuário digitava uma categoria sem respeitar letras maiúsculas (ex: "japonesa" em vez de "Japonesa"). Ele foi identificado durante testes exploratórios de validação de limite. A correção foi implementada aplicando a propriedade `.lower()` tanto no termo pesquisado quanto nos itens da base de dados antes de realizar a comparação na função `buscar_restaurante`.