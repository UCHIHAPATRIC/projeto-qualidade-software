# Diagnóstico de Qualidade – Startup Local Eats

## 1. Diagnóstico da Situação Atual

Após análise do cenário da startup **Local Eats**, identificamos que a organização passa por um momento de transição crítica. A ausência de processos formais de qualidade está a impactar diretamente a operação e a confiança dos utilizadores.

* **Problemas Críticos:** Erros de lógica (pedidos duplicados) e falhas funcionais em produção.
* **Causa Raiz:** Inexistência de uma definição clara de "Pronto" (Definition of Done) e falta de validação de requisitos antes do desenvolvimento.
* **Responsabilidade da Qualidade:** Atualmente, a qualidade é tratada de forma reativa. É necessário migrar para um modelo de **Responsabilidade Compartilhada**, onde todos os membros da equipa são guardiões da entrega, embora existam papéis focados em orquestrar os testes.

## 2. Papéis da Equipa e Responsabilidades

Para estruturar a qualidade, propomos a seguinte organização:

| Nome do Papel | Principais Responsabilidades | Relação com a Qualidade |
| :--- | :--- | :--- |
| **QA / Analista de Qualidade** | Planear e executar testes, gerir o ciclo de vida de bugs e validar critérios de aceite. | Garante que o software atende às expectativas do utilizador final. |
| **Desenvolvedor** | Escrever código limpo, realizar testes unitários e de integração. | Responsável pela integridade técnica e por evitar que bugs básicos cheguem ao QA. |
| **Analista de Sistemas** | Refinar requisitos, definir regras de negócio e validar protótipos. | Garante a "Qualidade de Design", evitando que o sistema seja construído com lógica errada. |
| **DevOps** | Automatizar o pipeline de deploy (CI/CD) e monitorar a saúde do ambiente de produção. | Garante que a entrega seja estável e que o sistema tenha alta disponibilidade. |

## 3. Práticas Básicas de QA Recomendadas

Propomos a implementação imediata destas 4 práticas para estancar os erros em produção:

1.  **Revisão de Requisitos (Static Testing):** Antes do início do código, o QA e o Analista de Sistemas devem rever as regras de negócio para evitar erros como o de pedidos duplicados.
2.  **Gestão de Defeitos:** Centralizar todos os bugs encontrados numa ferramenta (ex: GitHub Issues) com passos para reproduzir e severidade definida.
3.  **Testes de Regressão Manual:** Antes de cada atualização (deploy), validar as funções críticas: login, realizar pedido e pagamento.
4.  **Critérios de Aceite:** Cada tarefa só pode ser considerada "concluída" se passar por uma lista de verificações pré-definida pela equipa.

## 4. Anúncios de Contratação

### Vaga 1: Analista de Qualidade de Software (QA)
**Empresa:** Local Eats  
**Local:** Porto Alegre – RS | **Modelo:** Híbrido

**Sobre a vaga:**
A Local Eats procura uma pessoa entusiasta de QA para implementar a cultura de testes na nossa plataforma. Atuarás em colaboração direta com os devs para reduzir bugs e melhorar a experiência do utilizador.

**Principais Responsabilidades:**
* Criar planos de teste para as plataformas Web e Mobile.
* Identificar, documentar e acompanhar a resolução de defeitos.
* Realizar testes exploratórios em novas funcionalidades.

**Requisitos:**
* **Obrigatórios:** Conhecimento em metodologias de teste de software; Boa capacidade analítica e de comunicação.
* **Desejáveis:** Experiência com ferramentas de gestão de bugs; Noções de SQL e APIs.
* **Desejável:** Certificação ISTQB-CTFL.

---

### Vaga 2: Desenvolvedor(a) Backend Junior/Pleno
**Empresa:** Local Eats  
**Local:** Remoto

**Sobre a vaga:**
Procuramos alguém apaixonado por resolver problemas complexos e que se preocupe com a qualidade do código produzido. A tua missão será garantir a robustez da nossa API de pedidos.

**Principais Responsabilidades:**
* Desenvolver novas funcionalidades seguindo boas práticas de arquitetura.
* Implementar testes unitários para as regras de negócio críticas.
* Colaborar na resolução de problemas de performance e concorrência.

**Requisitos:**
* **Obrigatórios:** Sólidos conhecimentos em lógica de programação; Experiência com linguagens como Node.js, Python ou C#; Conhecimento em bancos de dados relacionais.
* **Desejáveis:** Conhecimento em Docker e processos de CI/CD.