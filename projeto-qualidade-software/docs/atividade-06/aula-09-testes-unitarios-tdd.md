# Atividade PBL – Aula 9: Testes Unitários Automatizados e TDD – LocalEats

**Integrante:** Patric
**Contexto:** Evolução da abordagem de QA do sistema LocalEats de testes manuais para automação no código utilizando a prática de TDD.

---

## 🔹 1. Funcionalidade Escolhida

**🚚 3. Cálculo de taxa de entrega**

* **O que faz:** Calcula o valor da entrega com base na distância em quilômetros.
* **Problema que resolve:** Padroniza a cobrança de entrega, evitando erros manuais ou regras inconsistentes.
* **Importância:** Impacta diretamente o custo final do pedido para o cliente.
* **Regras de negócio:**
    * Distância até 3 km: taxa fixa de R$ 5,00.
    * Acima de 3 km: taxa fixa (R$ 5,00) + R$ 2,00 por quilômetro adicional.
    * Distância negativa: gera um erro.

---

## 🔹 2. Testes Unitários

```python
import pytest
from entrega import calcular_taxa_entrega

# 🟢 Cenário 1 (Happy Path)
# Nome descritivo: Deve cobrar taxa fixa para distâncias de até 3km
# Cenário testado: Valida se a função retorna a taxa base de R$ 5,00 para entregas curtas.
# Dados de entrada: distancia = 2.5
# Resultado esperado: Retornar 5.0
def test_deve_cobrar_taxa_fixa_para_distancias_ate_3km():
    # Arrange
    distancia = 2.5
    # Act
    resultado = calcular_taxa_entrega(distancia)
    # Assert
    assert resultado == 5.0

# 🟢 Cenário 2 (Happy Path)
# Nome descritivo: Deve cobrar taxa proporcional para distâncias acima de 3km
# Cenário testado: Valida o acréscimo de R$ 2,00 por km extra após os 3km iniciais.
# Dados de entrada: distancia = 5.0
# Resultado esperado: Retornar 9.0 (5.0 da base + 2 * 2.0 dos kms extras)
def test_deve_cobrar_taxa_proporcional_para_distancias_acima_de_3km():
    # Arrange
    distancia = 5.0
    # Act
    resultado = calcular_taxa_entrega(distancia)
    # Assert
    assert resultado == 9.0

# 🔴 Cenário 3 (Edge Case / Erro)
# Nome descritivo: Deve gerar erro ao receber uma distância negativa
# Cenário testado: Valida se o sistema bloqueia tentativas de distâncias impossíveis.
# Dados de entrada: distancia = -1.0
# Resultado esperado: Levantar ValueError
def test_deve_gerar_erro_para_distancia_negativa():
    # Arrange
    distancia = -1.0
    # Act & Assert
    with pytest.raises(ValueError, match="Distância inválida"):
        calcular_taxa_entrega(distancia)