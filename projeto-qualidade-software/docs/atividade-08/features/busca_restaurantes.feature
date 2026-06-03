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