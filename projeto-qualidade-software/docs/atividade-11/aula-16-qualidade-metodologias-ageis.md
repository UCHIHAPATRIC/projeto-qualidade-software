# Atividade PBL – Aula 16: Qualidade em Metodologias Ágeis – LocalEats

**Integrante:** Patric Morales Taborda

---

## 🔹 1. Análise de Práticas Ágeis no Processo

Considerando o ciclo de vida do desenvolvimento atual do LocalEats, analisamos a aderência às principais práticas ágeis:

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
| :--- | :--- | :--- | :--- |
| **Planejamento iterativo** | Parcial | O desenvolvimento ocorre por demanda, com a escrita de cenários BDD antes da codificação, mas sem ciclos de tempo fixos (Sprints). | Sim. Organizar as demandas em iterações curtas e regulares (ex: ciclos de 2 semanas) para melhor previsibilidade. |
| **Priorização de funcionalidades** | Parcial | As *features* são selecionadas com base nas atividades do projeto, mas não há um *Product Backlog* formalmente ordenado por valor de negócio. | Sim. Aplicar técnicas de refinamento de backlog e focar na entrega de maior valor agregado primeiro (Lean). |
| **Entregas incrementais** | Sim | Funcionalidades aprovadas no Code Review são integradas e publicadas continuamente no ambiente de produção na Vercel. | Sim. Quebrar as histórias de usuário em pedaços ainda menores para aumentar a frequência de integrações. |
| **Feedback frequente** | Parcial | Ocorre feedback técnico assíncrono via *Pull Requests* no GitHub, mas falta alinhamento com a visão de negócio/usuário. | Sim. Estabelecer *Sprint Reviews* para validar a entrega com *stakeholders* antes de avançar. |
| **Trabalho colaborativo** | Sim | A equipe atua em conjunto nas revisões de código, garantindo que o conhecimento técnico não fique centralizado. | Sim. Introduzir sessões de *Pair Programming* (XP) para resoluções de arquitetura complexa. |
| **Controle visual das atividades** | Não | O acompanhamento das tarefas depende da comunicação descentralizada, sem um fluxo visual do status das atividades. | Sim. Implementar um quadro Kanban integrado ao repositório para espelhar o fluxo de valor. |
| **Melhoria contínua** | Parcial | Pontos de dor são discutidos informalmente quando ocorrem gargalos, mas sem um fórum dedicado para adaptação do processo. | Sim. Instituir a *Retrospectiva* periódica para debater o que funcionou e o que precisa ser ajustado. |

**Conclusão da Análise:**
O processo de desenvolvimento do LocalEats possui fortes alicerces em qualidade técnica e automação de testes (BDD/Playwright), além de uma cultura sólida de integração contínua e revisões de código. No entanto, as maiores oportunidades de melhoria residem na gestão do fluxo de trabalho. A ausência de rituais como retrospectivas, combinada com a falta de gestão visual (Kanban), torna o acompanhamento do projeto reativo. Ao abraçar metodologias ágeis como Scrum e Lean, a equipe poderá cadenciar suas entregas, reduzir desperdícios e evoluir seu processo não apenas na tecnologia, mas na eficiência da colaboração.

---

## 🔹 2. Propostas de Melhoria Ágil

Com base nas lacunas identificadas, as seguintes propostas buscam incorporar práticas de frameworks de mercado para elevar a maturidade ágil do time:

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
| :--- | :--- | :--- |
| **Implementar quadro visual de fluxo de trabalho (To Do, Doing, In Review, Done)** | Kanban | Dar total transparência e rastreabilidade ao status das tarefas, evitando duplicação de esforço e facilitando a identificação de gargalos. |
| **Limitar o Trabalho em Progresso (WIP - Work in Progress)** | Kanban / Lean | Reduzir a troca de contexto constante (*context switching*) e garantir que tarefas iniciadas sejam efetivamente terminadas antes de novas demandas entrarem no fluxo. |
| **Estabelecer reunião periódica de Retrospectiva** | Scrum | Criar um ambiente seguro para o time inspecionar e adaptar suas ferramentas, processos e interações, promovendo a melhoria contínua real. |
| **Adotar Programação em Par (Pair Programming) em tarefas críticas** | XP (*Extreme Programming*) | Aumentar a qualidade do código já no momento da escrita, reduzir bugs em lógicas complexas e compartilhar conhecimento técnico entre os membros da equipe. |

---

## 🔹 3. Definition of Ready (DoR)

A *Definition of Ready* (Definição de Preparo) estabelece os critérios obrigatórios que uma demanda (User Story/Tarefa) deve atender antes de poder ser puxada para desenvolvimento pela equipe, evitando bloqueios durante a codificação.

**Critérios de Preparo para o LocalEats:**
1. A funcionalidade proposta tem valor de negócio claro e foi priorizada.
2. Os critérios de aceitação foram discutidos e mapeados.
3. A funcionalidade já possui seus cenários de comportamento mapeados em sintaxe Gherkin (BDD).
4. Dependências externas (como protótipos de interface, acesso a APIs ou documentação extra) estão disponíveis e esclarecidas.
5. A estimativa de esforço ou complexidade técnica foi discutida entre os desenvolvedores responsáveis.

---

## 🔹 4. Definition of Done (DoD)

A *Definition of Done* (Definição de Pronto) garante que todos os membros da equipe tenham a mesma compreensão do que significa uma tarefa estar totalmente finalizada, garantindo que o alto padrão de qualidade de software seja mantido.

**Critérios de Conclusão para o LocalEats:**
1. O código-fonte foi escrito de forma limpa, seguindo os padrões de arquitetura do projeto.
2. A funcionalidade atende a todos os critérios de aceitação estipulados no Gherkin.
3. Os testes automatizados (unidade e/ou *end-to-end* com Playwright/pytest) foram criados e passaram com sucesso localmente.
4. O código foi submetido via *Pull Request* e aprovado por pelo menos um outro integrante da equipe (*Code Review*).
5. A funcionalidade foi integrada na *branch* principal e sofreu o *deploy* com sucesso no ambiente de produção na Vercel, sem apresentar regressões.