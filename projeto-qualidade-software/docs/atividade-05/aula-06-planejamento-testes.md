# Planejamento e Execução de Testes – LocalEats

**Estudante:** Patric Morales Taborda  
**Disciplina:** Qualidade de Software  

---

## 1. Plano de Testes

**Objetivo**
Validar a confiabilidade das funções principais da plataforma LocalEats, garantindo que o usuário consiga buscar estabelecimentos e gerenciar seus favoritos sem erros de lógica ou inconsistências de dados.

**Escopo**
* **O que será testado:** Fluxo de busca por tipo de culinária, visualização de detalhes do restaurante e funcionalidade de favoritar.
* **O que não será testado:** Processamento de pagamentos reais e integração com APIs externas de mapas (geolocalização avançada).

**Funcionalidades Selecionadas**
* Busca de Restaurantes
* Visualização de Detalhes
* Favoritos

**Estratégia de Testes**
Serão realizados testes funcionais manuais através da interface web, focando na jornada do usuário e na validação dos resultados exibidos na tela.

**Responsáveis**
* Patric Morales Taborda: Planejamento, escrita dos casos de teste e execução.

---

## 2. Casos de Teste

**CT01 - Busca por culinária com sucesso**
* **ID:** CT01
* **Cenário:** Happy Path
* **Dado que** estou na página inicial do LocalEats
* **Quando** eu digito "Italiana" no campo de busca e clico em pesquisar
* **Então** o sistema apresenta apenas os restaurantes que possuem a tag de culinária italiana.

**CT02 - Visualizar detalhes do restaurante com sucesso**
* **ID:** CT02
* **Cenário:** Happy Path
* **Dado que** realizei uma busca e os resultados aparecem na tela
* **Quando** eu clico no card de um restaurante específico
* **Então** o sistema apresenta a página de detalhes contendo o cardápio e as avaliações.

**CT03 - Adicionar restaurante aos favoritos com sucesso**
* **ID:** CT03
* **Cenário:** Happy Path
* **Dado que** estou na página de detalhes de um restaurante
* **Quando** eu clico no ícone de favoritar (coração)
* **Então** o sistema adiciona o restaurante à minha lista de favoritos.

**CT04 - Busca por termo inexistente**
* **ID:** CT04
* **Cenário:** Erro
* **Dado que** estou na página de busca
* **Quando** eu digito um termo inexistente como "Xyz123" e pesquiso
* **Então** o sistema apresenta a mensagem de que nenhum restaurante foi encontrado.

**CT05 - Tentar favoritar sem estar logado**
* **ID:** CT05
* **Cenário:** Erro
* **Dado que** estou na página de detalhes como visitante
* **Quando** eu clico no ícone de favoritar
* **Então** o sistema impede a ação e solicita que eu faça login para continuar.

---

## 3. Execução dos Testes

**Resultado CT01:** Falhou
* **Evidência:** Ao pesquisar por culinária italiana, o sistema trouxe pizzarias misturadas com hamburguerias que não tinham a tag correta.

**Resultado CT02:** Passou
* **Evidência:** A página de detalhes carregou todas as fotos e o texto do menu conforme esperado.

**Resultado CT03:** Falhou
* **Evidência:** O ícone mudou de cor na hora, mas ao atualizar a página, o restaurante sumiu da lista de favoritos.

**Resultado CT04:** Passou
* **Evidência:** O sistema exibiu corretamente o aviso de que não havia resultados para o termo digitado.

**Resultado CT05:** Falhou
* **Evidência:** O sistema não exibiu nenhuma mensagem de erro ou pedido de login; o botão simplesmente não respondeu.

---

## 4. Análise dos Resultados

Foram executados 5 testes no total, sendo que 2 passaram e 3 falharam. Os principais problemas encontrados estão ligados à lógica de filtragem do banco de dados, que não está sendo precisa, e à persistência de dados no perfil do usuário. Além disso, a falta de feedback visual em cenários de erro (como no CT05) mostra que o sistema precisa melhorar muito a comunicação com o usuário quando algo não sai como planejado.

---

## 5. Reflexão no contexto do LocalEats

O plano de testes ajudou muito a organizar o raciocínio, pois antes eu testava de forma aleatória e acabava esquecendo de validar os cenários de erro. Durante a execução, percebi que o maior gargalo não é apenas visual, mas sim na integração das informações; os dados parecem se perder entre uma tela e outra. Para as próximas etapas, eu melhoraria o processo incluindo testes de estresse, para ver se essa inconsistência nos resultados da busca piora quando muitos usuários tentam pesquisar ao mesmo tempo.