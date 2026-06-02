import pytest
from entrega import calcular_taxa_entrega

def test_deve_cobrar_taxa_fixa_para_distancias_ate_3km():
    distancia = 2.5
    resultado = calcular_taxa_entrega(distancia)
    assert resultado == 5.0

def test_deve_cobrar_taxa_proporcional_para_distancias_acima_de_3km():
    distancia = 5.0
    resultado = calcular_taxa_entrega(distancia)
    assert resultado == 9.0

def test_deve_gerar_erro_para_distancia_negativa():
    distancia = -1.5
    with pytest.raises(ValueError, match="Distância inválida"):
        calcular_taxa_entrega(distancia)