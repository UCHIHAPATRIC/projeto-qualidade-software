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