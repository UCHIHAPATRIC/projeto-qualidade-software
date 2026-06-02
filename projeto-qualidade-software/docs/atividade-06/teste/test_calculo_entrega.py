import pytest
from calculo_entrega import calcular_taxa_entrega

# ==============================================================================
# Cenário 1: Sucesso (Happy Path) - Distância dentro do limite da taxa fixa
# ==============================================================================
# Nome descritivo:
# test_deve_cobrar_taxa_fixa_quando_distancia_menor_ou_igual_a_tres_km

# Cenário testado:
# Valida se a função retorna exatamente o valor fixo base (R$ 5.00) quando 
# a distância percorrida é de até 3 km.

# Dados de entrada: distancia = 2.5
# Resultado esperado: Retornar 5.00 (sem exceções)
def test_deve_cobrar_taxa_fixa_quando_distancia_menor_ou_igual_a_tres_km():
    distancia = 2.5
    resultado = calcular_taxa_entrega(distancia)
    assert resultado == 5.00


# ==============================================================================
# Cenário 2: Sucesso (Happy Path) - Distância no limite exato da taxa fixa
# ==============================================================================
# Nome descritivo:
# test_deve_cobrar_taxa_fixa_no_limite_exato_de_tres_km

# Cenário testado:
# Teste de borda (limite inclusivo) para garantir que o valor fixo é mantido 
# exatamente na marca de 3.0 km.

# Dados de entrada: distancia = 3.0
# Resultado esperado: Retornar 5.00
def test_deve_cobrar_taxa_fixa_no_limite_exato_de_tres_km():
    distancia = 3.0
    resultado = calcular_taxa_entrega(distancia)
    assert resultado == 5.00


# ==============================================================================
# Cenário 3: Sucesso (Happy Path) - Distância com valor adicional proporcional
# ==============================================================================
# Nome descritivo:
# test_deve_calcular_taxa_proporcional_para_distancia_acima_de_tres_km

# Cenário testado:
# Valida se a função adiciona corretamente R$ 1.50 por km excedente para 
# distâncias maiores que 3 km.

# Dados de entrada: distancia = 5.0 (2 km excedentes -> 2 * 1.50 = 3.00)
# Resultado esperado: Retornar 8.00 (5.00 base + 3.00 adicional)
def test_deve_calcular_taxa_proporcional_para_distancia_acima_de_tres_km():
    distancia = 5.0
    resultado = calcular_taxa_entrega(distancia)
    assert resultado == 8.00


# ==============================================================================
# Cenário 4: Erro/Borda - Distância com valor inválido (Negativo)
# ==============================================================================
# Nome descritivo:
# test_deve_lancar_erro_quando_distancia_for_negativa

# Cenário testado:
# Valida o comportamento do sistema diante de dados corrompidos ou incorretos,
# garantindo que uma exceção apropriada seja disparada.

# Dados de entrada: distancia = -1.5
# Resultado esperado: Levantar ValueError com a mensagem exata de erro.
def test_deve_lancar_erro_quando_distancia_for_negativa():
    distancia = -1.5
    with pytest.raises(ValueError) as exc_info:
        calcular_taxa_entrega(distancia)
    
    assert str(exc_info.value) == "A distância não pode ser negativa"