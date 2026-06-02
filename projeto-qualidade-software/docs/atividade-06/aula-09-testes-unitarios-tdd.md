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
    * Distância até 3 km -> taxa fixa de R$ 5,00.
    * Acima de 3 km -> taxa fixa (R$ 5,00) + R$ 2,00 por quilômetro adicional.
    * Distância negativa -> gera um erro (`ValueError`).

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
    with pytest.raises(ValueError, match="Distância inválida"):
        calcular_taxa_entrega(distancia)
```

---

## 🔹 3. Aplicação do TDD

Abaixo está o ciclo TDD (Red -> Green -> Refactor) aplicado na construção da regra de negócio.

### 🔴 Red (Escrever o teste que falha)
Primeiro, criei os testes acima. A função principal existia apenas com um `pass`. O teste falhou porque a lógica não existia e nenhum valor ou erro era retornado.

```python
# Código inicial que causou a falha no teste
def calcular_taxa_entrega(distancia):
    pass
```

### 🟢 Green (Fazer o teste passar)
Implementei a lógica mais simples e direta possível, apenas usando condicionais básicas e números literais, focando exclusivamente em fazer os testes rodarem com sucesso ("ficarem verdes").

```python
# Código implementado apenas para os testes passarem
def calcular_taxa_entrega(distancia):
    if distancia < 0:
        raise ValueError("Distância inválida")
    if distancia <= 3:
        return 5.0
    if distancia > 3:
        return 5.0 + ((distancia - 3) * 2.0)
```

### 🔵 Refactor (Melhorar o código)
Com os testes garantindo que a regra matemática funciona, refatorei o código para deixá-lo mais profissional, removendo os "números mágicos" e melhorando a nomenclatura.

```python
# Código final após a refatoração
def calcular_taxa_entrega(distancia_km: float) -> float:
    TAXA_BASE = 5.0
    LIMITE_KM_BASE = 3.0
    TAXA_POR_KM_EXTRA = 2.0

    if distancia_km < 0:
        raise ValueError("Distância inválida")
    
    if distancia_km <= LIMITE_KM_BASE:
        return TAXA_BASE
        
    km_adicional = distancia_km - LIMITE_KM_BASE
    return TAXA_BASE + (km_adicional * TAXA_POR_KM_EXTRA)
```

---

## 🔹 4. Refatoração

**Melhorias e justificativas:**

* **Nomenclatura (Legibilidade):** A variável `distancia` virou `distancia_km` para deixar explícita a unidade de medida esperada. Adicionei tipagem de dados (`float`) para facilitar o entendimento.
* **Remoção de Duplicações e Números Mágicos:** Os valores 5.0, 3.0 e 2.0 estavam soltos no código. Eles foram substituídos por constantes (`TAXA_BASE`, `LIMITE_KM_BASE`, `TAXA_POR_KM_EXTRA`). Isso facilita muito a manutenção; se os valores mudarem amanhã, alteramos apenas as constantes num só lugar.
* **Fluxo simplificado:** O segundo `if` (`if distancia > 3:`) foi removido. Como o primeiro `if` já possui um `return` que encerra a função para distâncias menores, tudo que passa dele já é obrigatoriamente maior que 3km.

---

## 🔹 5. Execução dos Testes

* **Total de testes:** 3
* **Quantos passaram:** 3
* **Quantos falharam:** 0

**Evidência de execução do terminal:**

```text
============================= test session starts ==============================
collected 3 items

test_entrega.py ...                                                      [100%]

============================== 3 passed in 0.03s ===============================
```

---

## 🔹 6. Reflexão no contexto do LocalEats

* **Foi difícil escrever testes antes do código?** Um pouco no começo, pois inverte a lógica tradicional. Tive que pensar no "comportamento" que eu esperava e nos erros possíveis antes mesmo de pensar nos `if/else` da função.
* **O TDD ajudou no desenvolvimento?** Sim, ajudou a focar no essencial. Escrevi apenas o código estritamente necessário para atender à regra da taxa de entrega, sem complicar ou adicionar funções que não haviam sido pedidas.
* **Os testes aumentaram a confiança no código?** Muito. Durante a fase de Refatoração, mudar o nome das variáveis e trocar a estrutura da função foi seguro, porque se eu errasse a matemática, o teste me avisaria na hora.
* **O que melhorariam?** Poderíamos testar tipos de dados inválidos (como enviar uma "string" no lugar da distância) para garantir que o sistema não quebre, ou usar testes parametrizados para rodar várias distâncias diferentes de uma só vez.
* **Como isso ajuda no projeto do grupo?** Garante que a regra de negócio central não sofra regressões. Se outro desenvolvedor mexer no código de pedidos amanhã e acidentalmente alterar o valor da entrega, os testes automatizados vão falhar imediatamente no repositório, impedindo que o erro vá para produção.