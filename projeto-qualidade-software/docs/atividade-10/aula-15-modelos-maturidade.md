# Atividade PBL – Aula 15: Modelos de Maturidade – LocalEats

**Integrante:** Patric Morales Taborda

---

## 🔹 1. Diagnóstico de Maturidade

Avaliação do processo da equipe com base nos critérios de maturidade organizacional:

| Critério | Sim | Parcial | Não |
| :--- | :---: | :---: | :---: |
| Os requisitos são documentados? | **X** | | |
| Existe controle de mudanças? | **X** | | |
| Há atividades de teste definidas? | **X** | | |
| Os defeitos são registrados? | | **X** | |
| O processo de desenvolvimento é conhecido por toda a equipe? | **X** | | |
| As tarefas são planejadas e acompanhadas regularmente? | | **X** | |
| Existe padronização para implementação de funcionalidades? | **X** | | |
| Os testes são executados antes da entrega das funcionalidades? | **X** | | |
| Há revisão de código ou validação por outro integrante da equipe? | **X** | | |
| A equipe utiliza ferramentas para gerenciamento das atividades? | | **X** | |
| Os artefatos do projeto (requisitos, testes, código) são organizados e versionados? | **X** | | |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | | **X** | |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? | | **X** | |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | | **X** |

### Classificação do Processo:
**Classificação:** Gerenciado (Equivalente ao Nível 2 do CMMI / Nível G do MPS.BR)

**Justificativa:** O processo da equipe ultrapassou o nível "Inicial" (ad-hoc), pois já existem práticas fundamentais de gestão de configuração (uso ativo de Git/GitHub), validação de requisitos (escrita de cenários BDD em Gherkin) e testes automatizados antes do deploy (Playwright). As entregas na Vercel são precedidas por revisões de código, demonstrando controle básico do projeto. No entanto, o processo foi classificado como "Gerenciado" e não "Definido" (Nível 3) porque ainda há lacunas na padronização institucional, rastreabilidade ponta a ponta e rituais de melhoria contínua. É um processo reativo e funcional, mas que depende muito da disciplina técnica individual, carecendo de métricas e indicadores consolidados para gerenciar o projeto quantitativamente no futuro.

---

## 🔹 2. Identificação de Lacunas

Com base no diagnóstico, listamos os principais gargalos e pontos de falha que impedem o processo de alcançar níveis mais altos de maturidade:

| Lacuna | Impacto |
| :--- | :--- |
| **Execução manual de testes locais** | Sem um pipeline de CI/CD, os testes dependem do comando manual no terminal, aumentando o risco de código falho ser mesclado (merged) por esquecimento humano. |
| **Ausência de métricas de qualidade** | Sem indicadores (ex: % de cobertura de testes, tempo de ciclo, densidade de defeitos), é impossível medir de forma objetiva se a qualidade do software está melhorando ou piorando. |
| **Falta de rastreabilidade documentada** | A conexão entre o requisito inicial (ideia), a tarefa no quadro e o script de teste não é rastreável de forma fluida, dificultando auditorias ou a identificação de cenários esquecidos. |

---

## 🔹 3. Propostas de Melhoria

Para evoluir a maturidade do processo da equipe em direção aos níveis Definido e Quantitativamente Gerenciado, propomos as seguintes ações de curto e médio prazo:

| Melhoria | Benefício |
| :--- | :--- |
| **Implementar pipeline de Integração Contínua (CI)** | Automatizar a execução dos testes via *GitHub Actions* em todo Pull Request criado. Benefício: Bloqueia integrações que quebrem o sistema, elevando a confiabilidade do processo. |
| **Adotar ferramentas de medição estática** | Integrar um gerador de relatórios (como *pytest-cov*) para medir o percentual de código coberto pelos testes. Benefício: Gera indicadores reais para guiar a equipe e formalizar as métricas do projeto. |
| **Estruturar gestão ágil atrelada ao repositório** | Utilizar o *GitHub Projects* ou ferramenta similar para vincular cada *Issue* (defeito/feature) ao seu respectivo código e cenário BDD. Benefício: Garante a rastreabilidade total do ciclo de vida do requisito. |