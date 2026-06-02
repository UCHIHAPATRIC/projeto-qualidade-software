# Atividade PBL – Aula 9: Testes Unitários Automatizados e TDD – LocalEats

**Integrante:** Patric Morales Taborda

**Contexto:** Evolução da abordagem de QA do sistema LocalEats de testes manuais para automação com TDD.

---

## 🔹 1. Funcionalidade Escolhida

**🚚 3. Cálculo de taxa de entrega**

* **O que faz:** Calcula o valor da entrega do LocalEats com base na distância em quilômetros entre o restaurante e o cliente.
* **Problema que resolve:** Padroniza a cobrança de entrega, evitando valores arbitrários que prejudiquem o cliente ou o restaurante.
* **Importância:** Impacta diretamente o custo final do pedido e a decisão de compra do usuário no aplicativo.
* **Regras de negócio estabelecidas:**
    * Distância até 3 km $\rightarrow$ taxa fixa de R$ 5,00.
    * Acima de 3 km $\rightarrow$ taxa fixa (R$ 5,00) + R$ 2,00 por quilômetro adicional.
    * Distância negativa $\rightarrow$ gera um erro (`ValueError`).

---

## 🔹 2. Testes Unitários

Abaixo estão os 3 cenários de teste exigidos (2 *Happy Path* e 1 *Edge Case/Erro*), escritos em Python utilizando a biblioteca `pytest`.

```python
import pytest
from entrega import calcular_taxa_entrega

# 🟢 Cenário 1 (Happy Path)
# Nome descritivo: Deve cobrar taxa fixa para distâncias de até 3km
# Cenário testado: Valida se a função retorna a taxa base de R$ 5,00 
# para pedidos muito próximos.
# Dados de entrada: distancia = 2.5
# Resultado esperado: Retornar 5.0
def test_deve_cobrar_taxa_fixa_para_distancias_ate_3km():
    # Arrange (preparação)
    distancia = 2.5

    # Act (execução)
    resultado = calcular_taxa_entrega(distancia)

    # Assert (validação)
    assert resultado == 5.0


# 🟢 Cenário 2 (Happy Path)
# Nome descritivo: Deve cobrar taxa proporcional para distâncias acima de 3km
# Cenário testado: Valida o acréscimo de R$ 2,00 por km extra após os 3km iniciais.
# Dados de entrada: distancia = 5.0
# Resultado esperado: Retornar 9.0 (5.0 + 2 * 2.0)
def test_deve_cobrar_taxa_proporcional_para_distancias_acima_de_3km():
    # Arrange
    distancia = 5.0

    # Act
    resultado = calcular_taxa_entrega(distancia)

    # Assert
    assert resultado == 9.0


# 🔴 Cenário 3 (Edge Case / Erro)
# Nome descritivo: Deve gerar erro ao receber uma distância negativa
# Cenário testado: Valida se o sistema bloqueia tentativas de fraudar a rota
# com distâncias impossíveis.
# Dados de entrada: distancia = -1.5
# Resultado esperado: Levantar ValueError com mensagem específica
def test_deve_gerar_erro_para_distancia_negativa():
    # Arrange
    distancia = -1.5

    # Act & Assert
    with pytest.raises(ValueError, match="A distância não pode ser negativa"):
        calcular_taxa_entrega(distancia)