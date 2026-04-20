# Diagnóstico de Qualidade – Startup Local Eats

**Estudante:** Patric Morales Taborda  
**Disciplina:** Qualidade de Software  
**Atividade:** PBL – Diagnóstico Organizacional de QA  

---

# Diagnóstico de Qualidade – Startup Local Eats

## 1. Diagnóstico da Situação Atual

### 1.1 Papéis atuais identificados

Com base na análise do cenário da startup, os papéis que provavelmente compõem a equipa atual são:

* **Desenvolvedores (Web e Mobile):** Responsáveis pela construção técnica do MVP. Devido ao prazo apertado, focam-se na entrega de código, acumulando funções de teste e implementação sem um processo formal.
* **Gerente de Produto (ou Proprietário da Startup):** Define as funcionalidades e prioriza o lançamento para eventos gastronómicos, focando-se mais no prazo de mercado do que na estabilidade técnica.
* **Analista de Sistemas / Requisitos:** Atua na tradução das necessidades dos comerciantes para a equipa técnica, mas a pressa na entrega sugere que o refinamento de cenários de exceção (como duplicidade de pedidos) não está a ser priorizado.

### 1.2 Quem é responsável pela qualidade hoje?

Atualmente, a responsabilidade pela qualidade na Local Eats é **difusa e reativa**. Na prática, acredita-se que ela esteja sendo tratada da seguinte forma:

* **Responsabilidade Informal dos Desenvolvedores:** Como não há um papel de QA definido, os próprios desenvolvedores acabam sendo os únicos a testar o que produzem. No entanto, esses testes costumam ser superficiais (apenas para ver se o código "roda"), sem uma visão crítica de regras de negócio.
* **O Usuário como "Testador":** Pela descrição dos problemas, fica claro que a qualidade só é verificada após o lançamento. O usuário final está agindo como o primeiro filtro de bugs, o que gera uma percepção negativa da marca.
* **Tratamento Reativo:** A qualidade não é prevenida, mas "reparada". A equipe só atua nos defeitos após as reclamações chegarem à direção, indicando a ausência de uma cultura de prevenção ou de processos de validação antes do deploy.

### 1.3 Problemas identificados

A ausência de uma estrutura organizacional voltada para a qualidade gera uma série de riscos técnicos e de negócio. Os principais problemas identificados são:

* **Efeito Espectador:** Como a responsabilidade não é de ninguém especificamente, os membros da equipe assumem que "alguém já deve ter testado", permitindo que erros óbvios cheguem à produção.
* **Falta de Critérios de Aceite:** Sem uma organização de QA, as funcionalidades são desenvolvidas sem uma definição clara de quando estão "prontas", o que causa problemas como pedidos duplicados e lógica de busca incorreta.
* **Ausência de Testes de Regressão:** Quando um desenvolvedor corrige um erro, não há um processo para garantir que essa correção não quebrou outras partes do sistema que estavam funcionando (ex: atualizações de página que fazem avaliações sumirem).
* **Sobrecarga da Equipe Técnica:** Os desenvolvedores gastam muito tempo corrigindo "incêndios" em produção (bugs urgentes), o que impede o progresso no desenvolvimento de novas funcionalidades planejadas.
* **Prejuízo à Reputação e Financeiro:** Erros em pedidos e inconsistências entre versões (web/mobile) geram frustração imediata, fazendo com que usuários e comerciantes abandonem a plataforma Local Eats.

### 1.4 Impactos desses problemas

A desorganização dos processos de qualidade gera consequências graves que afetam tanto a integridade técnica do sistema quanto a experiência de quem o utiliza. Os principais impactos são:

* **Para o Sistema (Integridade Técnica):**
    * **Instabilidade e Degradação:** O acúmulo de falhas não corrigidas (como crashes em modelos específicos de smartphone) torna o sistema instável, dificultando futuras manutenções e evoluções.
    * **Inconsistência de Dados:** Problemas como pedidos duplicados e o desaparecimento de avaliações indicam falhas na integridade do banco de dados, o que pode corromper o histórico de vendas e a reputação dos estabelecimentos.
    * **Perda de Sincronismo:** A falta de paridade entre as versões web e mobile gera um sistema "fragmentado", onde a regra de negócio aplicada em uma plataforma pode não funcionar na outra.

* **Para os Usuários (Clientes e Comerciantes):**
    * **Quebra de Confiança:** Para um sistema que lida com alimentação e pagamentos, erros como pedidos que não chegam ou cobranças duplicadas fazem com que o usuário perca a confiança na plataforma e a desinstale.
    * **Frustração e Má Experiência (UX):** Telas confusas e lentidão em horários de pico geram uma experiência negativa, levando o cliente a buscar alternativas em aplicativos concorrentes.
    * **Prejuízo Financeiro aos Lojistas:** Pedidos duplicados ou resultados incorretos de busca afetam diretamente o faturamento e a logística dos restaurantes locais, que são os principais parceiros do negócio.

    ### 1.5 A qualidade é responsabilidade de quem?

A qualidade de software deve ser entendida como uma **responsabilidade compartilhada por toda a equipe**, e não apenas uma tarefa isolada de um indivíduo ou departamento.

* **Visão de Equipe (Qualidade Intrínseca):** Para que o Local Eats seja bem-sucedido, a qualidade deve estar presente desde a concepção da ideia até o monitoramento em produção. Se a qualidade for vista como "problema de uma pessoa só" (do QA), os desenvolvedores tendem a se preocupar menos com a revisão do código, e os analistas podem negligenciar o detalhamento dos requisitos.
* **O Papel do Especialista em QA:** Embora todos sejam responsáveis, o papel do QA (Analista de Qualidade) é fundamental como um **facilitador**. Ele não é o "único que testa", mas sim quem define as estratégias, ferramentas e padrões de qualidade que a equipe deve seguir para evitar que o erro aconteça.
* **Cultura de Prevenção:** Quando a responsabilidade é compartilhada, o foco muda de "encontrar bugs" para "prevenir bugs". Isso significa que o desenvolvedor testa sua própria lógica, o analista revisa as regras de negócio e o QA valida a experiência final, garantindo que o sistema entregue valor real ao usuário.

---

## 2. Proposta de Organização da Qualidade

### 2.1 Definição de papéis da equipe

Para garantir que a Local Eats entregue um produto confiável, a equipe deve ser estruturada com os seguintes papéis e responsabilidades:

* **Analista de Qualidade (QA):**
    * **Principais responsabilidades:** Planejar e executar testes (manuais e automatizados), documentar bugs, definir planos de teste e validar se a funcionalidade atende aos requisitos antes do lançamento.
    * **Relação com a qualidade:** Atua como o guardião dos processos, garantindo que nenhum código chegue ao usuário sem passar por uma validação técnica e funcional rigorosa.

* **Desenvolvedor:**
    * **Principais responsabilidades:** Implementar as funcionalidades do sistema, realizar testes unitários e de integração, e corrigir os defeitos reportados pelo QA.
    * **Relação com a qualidade:** Responsável pela **qualidade intrínseca** do código. Deve garantir que o que foi construído é tecnicamente sólido e não gera regressões (quebras) em outras partes do sistema.

* **Analista de Sistemas:**
    * **Principais responsabilidades:** Levantar e detalhar os requisitos de negócio com os lojistas e clientes, criando documentações claras para a equipe técnica.
    * **Relação com a qualidade:** Garante a **qualidade de design/requisitos**. Se o requisito estiver bem escrito e sem ambiguidades, evita-se que a equipe desenvolva a funcionalidade errada (como o erro de pedidos duplicados).

* **DevOps:**
    * **Principais responsabilidades:** Gerenciar os ambientes de desenvolvimento e produção, automatizar o processo de deploy (entrega) e monitorar a performance do servidor em tempo real.
    * **Relação com a qualidade:** Garante a **qualidade de infraestrutura e disponibilidade**. Assegura que o sistema não fique lento em horários de pico e que as atualizações sejam feitas de forma segura, sem tirar o app do ar.

### 2.2 Descrição dos papéis

Abaixo estão detalhados os papéis propostos para a reestruturação da Local Eats:

| Papel | Responsabilidades principais | Relação com a qualidade |
| :--- | :--- | :--- |
| **QA / Analista de Qualidade** | Planejar e executar testes, gerir o ciclo de vida de bugs e validar critérios de aceite. | Atua como o filtro final, garantindo que o produto atenda às expectativas do usuário. |
| **Desenvolvedor** | Codificar funcionalidades, realizar testes unitários e de integração e corrigir defeitos. | Responsável pela qualidade técnica e por garantir que o código seja sólido e sem regressões. |
| **Analista de Sistemas** | Levantar requisitos, detalhar regras de negócio e validar fluxos com os stakeholders. | Garante a "Qualidade de Design", evitando erros de lógica antes mesmo do código começar. |
| **DevOps** | Automatizar o pipeline de deploy (CI/CD) e monitorar a performance da infraestrutura. | Assegura a qualidade de disponibilidade, garantindo que o sistema suporte picos de acesso. |

---

## 3. Práticas de QA Sugeridas

Para melhorar a estabilidade do sistema e a confiança dos usuários, sugiro a adoção das seguintes práticas de Qualidade de Software (QA):

1.  **Revisão de Requisitos (Static Testing):** Antes de iniciar a codificação de qualquer funcionalidade, o Analista e o QA devem revisar a regra de negócio. Isso evita erros de lógica, como o de pedidos duplicados, antes mesmo de se tornarem código.
2.  **Gestão Centralizada de Defeitos:** Utilizar uma ferramenta (ex: GitHub Issues) para registrar cada bug encontrado. Cada registro deve conter: passos para reproduzir, comportamento esperado, comportamento atual e o nível de severidade.
3.  **Testes de Fumaça (Smoke Tests):** Executar um roteiro rápido de testes manuais ou automatizados nas funções críticas (Login, Busca de Restaurante e Finalização de Pedido) sempre que uma nova versão for publicada, garantindo que o "coração" do app não pare de funcionar.
4.  **Testes Exploratórios:** Reservar um tempo para navegar livremente pelo sistema como se fosse um usuário final. Isso ajuda a identificar problemas de usabilidade, telas confusas e falhas em diferentes modelos de smartphone que não foram previstos nos planos de teste.
5.  **Criação de Critérios de Aceite:** Definir condições claras que uma tarefa deve cumprir para ser considerada "concluída" (Done). Por exemplo: "O sistema não deve permitir que o mesmo pedido seja processado duas vezes em menos de 1 minuto".

### 3.1 Lista de práticas

Para estruturar o processo de qualidade, estas são as práticas fundamentais recomendadas:

* **Registro e Acompanhamento de Bugs (GitHub Issues):** * **Responsável:** Toda a equipe (QA liderando a triagem).
    * **Impacto:** Garante que nenhum erro seja esquecido e permite priorizar o que é mais crítico para o negócio.
* **Testes de Fumaça (Smoke Tests):**
    * **Responsável:** QA e Desenvolvedores.
    * **Impacto:** Validação rápida das funções vitais (login e pedido) em cada nova versão, evitando que o app "pare" totalmente em produção.
* **Revisão de Requisitos (Static Testing):**
    * **Responsável:** Analista de Sistemas e QA.
    * **Impacto:** Identifica falhas de lógica (como a duplicidade de pedidos) antes do início do código, economizando tempo de desenvolvimento.
* **Testes Exploratórios em Diferentes Dispositivos:**
    * **Responsável:** QA.
    * **Impacto:** Melhora a portabilidade do sistema, garantindo que o app funcione bem em diversos modelos de smartphone, como relatado pelos usuários.
* **Definição de Critérios de Aceite (DoD):**
    * **Responsável:** Analista de Sistemas e QA.
    * **Impacto:** Alinha a expectativa entre o que foi pedido e o que foi entregue, reduzindo o retrabalho e a frustração da associação de comerciantes.

### 3.2 Explicação das práticas

Abaixo, descrevo brevemente como cada prática sugerida ajudará a estabilizar o sistema:

**Prática 1: Revisão de Requisitos (Static Testing)**
**Descrição:** Consiste em analisar as regras de negócio e a documentação antes do início da codificação. O objetivo é encontrar erros de lógica (como a falha que permite pedidos duplicados) ainda no papel. Corrigir um erro nesta fase é muito mais barato e rápido do que quando o código já foi escrito e enviado para produção.

**Prática 2: Testes de Fumaça (Smoke Tests)**
**Descrição:** É um conjunto rápido de testes que foca nas funcionalidades vitais do app, como fazer login, buscar um restaurante e finalizar um pagamento. Essa prática garante que as operações principais do Local Eats continuem funcionando após qualquer atualização, evitando que falhas críticas parem o sistema em horários de pico.

**Prática 3: Registro e Acompanhamento de Bugs**
**Descrição:** Trata-se da centralização de todos os problemas encontrados em uma ferramenta de gestão (como o GitHub Issues). Ao documentar os passos para reproduzir o erro e sua severidade, a equipe deixa de trabalhar no "caos" e passa a ter uma fila organizada de correções, garantindo que nenhum bug relatado pelo usuário seja esquecido.

---

## 4. Anúncios de Contratação

Abaixo estão os anúncios detalhados para as duas posições fundamentais na reestruturação da Local Eats:

### 4.1 Vaga 1 – Analista de Qualidade de Software (QA)

**Descrição da vaga**
Buscamos um profissional de QA para liderar a implementação de uma cultura de testes na Local Eats. Você atuará em colaboração com desenvolvedores e analistas para identificar riscos, planejar testes e garantir que as funcionalidades entregues (Web e Mobile) atendam aos requisitos de qualidade e estabilidade.

**Responsabilidades**
* Planejar e executar casos de teste funcionais e exploratórios.
* Identificar, registrar e monitorar a correção de defeitos (bugs).
* Apoiar a equipe na definição de critérios de aceite para novas funcionalidades.
* Realizar testes de regressão para garantir que novas atualizações não gerem falhas em funções antigas.

**Requisitos obrigatórios**
* Conhecimento sólido em metodologias de teste de software (caixa preta, fumaça, regressão).
* Capacidade analítica para documentar defeitos de forma clara e objetiva.
* Boa comunicação e proatividade para trabalhar em equipe.

**Requisitos desejáveis**
* Conhecimento em ferramentas de automação de testes (Cypress, Selenium ou similares).
* Experiência com testes de API (Postman ou Insomnia).
* Noções básicas de SQL para consulta em banco de dados.

**Certificações desejáveis**
* ISTQB – CTFL (Certified Tester Foundation Level).

---

### 4.2 Vaga 2 – Desenvolvedor Backend

**Descrição da vaga**
Estamos à procura de um Desenvolvedor Backend com foco em qualidade e robustez de código. Sua principal missão será garantir que a lógica de processamento de pedidos e buscas da Local Eats seja infalível, eliminando problemas de concorrência e inconsistência de dados.

**Responsabilidades**
* Desenvolver APIs escaláveis e seguras para as plataformas Web e Mobile.
* Implementar e manter testes unitários e de integração em todas as entregas.
* Investigar e corrigir falhas críticas de lógica (ex: pedidos duplicados).
* Colaborar com o time de QA para garantir a estabilidade do sistema em produção.

**Requisitos obrigatórios**
* Sólida experiência em lógica de programação e linguagens backend (Node.js, Python ou C#).
* Domínio de bancos de dados relacionais (SQL).
* Mentalidade voltada para a prevenção de erros e escrita de código limpo (Clean Code).

**Requisitos desejáveis**
* Conhecimento em infraestrutura e containers (Docker).
* Familiaridade com processos de CI/CD (integração e entrega contínua).
* Conhecimento em padrões de projeto (Design Patterns).

**Certificações desejáveis**
* Certificações de linguagem específica (ex: Microsoft Certified, Oracle Java) ou cursos avançados em Arquitetura de Software.

---

## Considerações Finais

### O que ficou de aprendizado
Essa atividade deixou claro que qualidade não é um "acréscimo" ao software, mas a base que sustenta o negócio. Analisar o caso da Local Eats me mostrou que a técnica (como a ISO 25010) só funciona quando existe um processo organizado por trás. Aprendi que é muito mais eficiente gastar tempo revisando requisitos e regras de negócio no início do que passar noites corrigindo bugs críticos em produção que poderiam ter sido evitados com uma conversa simples.

### Desafios de realizar o trabalho individualmente
O maior desafio de tocar esse diagnóstico sozinho foi a necessidade de "mudar de papel" constantemente. Tive que me policiar para não olhar para os problemas apenas como um desenvolvedor que quer entregar rápido, mas também como um analista de QA que precisa ser cético e um gerente que se preocupa com a reputação da marca. Conseguir enxergar o todo sem o debate com uma equipe exige um nível de autocrítica bem maior para não deixar passar detalhes importantes.

### O caminho para a evolução da startup
Para a Local Eats sair do modo reativo, o segredo é profissionalizar a validação. A principal melhoria é descentralizar a qualidade: parar de achar que "alguém vai testar" e passar a usar critérios claros do que é uma tarefa pronta. Com um profissional de QA liderando a estratégia e os desenvolvedores cuidando da base do código, a startup consegue parar de apenas "sobreviver" aos eventos e começa a entregar um produto que realmente passa confiança para os lojistas e usuários.