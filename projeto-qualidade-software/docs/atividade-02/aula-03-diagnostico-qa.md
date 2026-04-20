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

