# Atividade PBL – Aula 9: Testes Unitários Automatizados e TDD – LocalEats

**Projeto:** LocalEats
**Módulo:** Qualidade de Software / Testes Automatizados

---

## 🔹 1. Funcionalidade Escolhida

**Funcionalidade:** 2. Aplicação de desconto percentual (Backend)

* **O que faz:** Aplica um desconto percentual sobre o valor total do pedido.
* **Problema que resolve:** Permite o funcionamento de promoções e campanhas de marketing no sistema sem gerar prejuízos por cálculos incorretos.
* **Importância:** Impacta diretamente o preço final cobrado do cliente e o faturamento do restaurante.
* **Regras de negócio:**
    1.  O desconto deve estar entre 0% e 100%.
    2.  O valor final do pedido não pode ser negativo.
    3.  Se o desconto for inválido (menor que 0 ou maior que 100), o sistema deve retornar um erro de validação.

---

## 🔹 2. Testes Unitários

Para garantir a qualidade dessa funcionalidade, foram planejados e implementados 3 testes utilizando o framework `pytest` em Python.

### Teste 1: Cenário de Sucesso (Happy Path) - Desconto Padrão
* **Nome descritivo:** `test_deve_aplicar_desconto_corretamente_dentro_do_limite`
* **Cenário testado:** Valida se a função calcula o valor final corretamente quando um desconto válido (ex: 10%) é aplicado.
* **Dados de entrada:** `valor_pedido = 100.0`, `percentual_desconto = 10`
* **Resultado esperado:** Retornar `90.0`. Não deve gerar erro.

```python
def test_deve_aplicar_desconto_corretamente_dentro_do_limite():
    # Arrange
    valor_pedido = 100.0
    percentual_desconto = 10

    # Act
    resultado = aplicar_desconto(valor_pedido, percentual_desconto)

    # Assert
    assert resultado == 90.0