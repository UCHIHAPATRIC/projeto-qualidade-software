# Diagnóstico de Qualidade – Startup Local Eats

## 1. Diagnóstico da Situação Atual

Após análise técnica do cenário da startup **Local Eats**, identifiquei que a organização passa por um momento de transição crítica. A ausência de processos formais de qualidade está impactando diretamente a operação e a confiança dos usuários.

* **Problemas Críticos:** Erros de lógica (pedidos duplicados) e falhas funcionais graves em produção.
* **Causa Raiz:** Inexistência de uma definição clara de "Pronto" (Definition of Done) e falta de validação de requisitos antes do início do desenvolvimento.
* **Responsabilidade da Qualidade:** Atualmente, a qualidade é tratada de forma reativa. O objetivo deste diagnóstico é propor a migração para um modelo de **Responsabilidade Compartilhada**, onde a qualidade é integrada desde o início do ciclo de vida do software.

## 2. Papéis e Responsabilidades Propostos

Para estruturar a equipe de desenvolvimento da startup, proponho a definição dos seguintes papéis:

| Nome do Papel | Principais Responsabilidades | Relação com a Qualidade |
| :--- | :--- | :--- |
| **QA / Analista de Qualidade** | Planejar e executar testes, gerir o ciclo de vida de bugs e validar critérios de aceite. | Garante que o software atende às expectativas do usuário final e às regras de negócio. |
| **Desenvolvedor** | Escrever código limpo, realizar testes unitários e garantir a integração correta das funções. | Responsável pela integridade técnica e por evitar que bugs básicos cheguem ao ambiente de teste. |
| **Analista de Sistemas** | Refinar requisitos, definir regras de negócio e validar protótipos com stakeholders. | Garante a "Qualidade de Design", evitando que o sistema seja construído com lógica errada. |
| **DevOps** | Automatizar o pipeline de deploy (CI/CD) e monitorar a estabilidade do ambiente de produção. | Garante que a entrega seja estável e que o sistema tenha alta disponibilidade. |

## 3. Práticas Básicas de QA Recomendadas

Para estancar os erros em produção de imediato, recomendo a implementação das seguintes práticas:

1.  **Revisão Estática (Static Testing):** Antes do início da codificação, o Analista e o QA devem revisar os requisitos para evitar erros lógicos (como o caso dos pedidos duplicados).
2.  **Gestão Centralizada de Defeitos:** Utilizar o GitHub Issues para documentar cada erro encontrado, incluindo evidências, passos para reprodução e nível de severidade.
3.  **Testes de Regressão Manual:** Antes de qualquer atualização em produção, realizar um roteiro rápido de testes nas funções críticas (login, busca e finalização de pedido).
4.  **Definição de Critérios de Aceite:** Estabelecer condições claras que uma funcionalidade deve atender para ser considerada "concluída".

## 4. Anúncios de Contratação

### Vaga 1: Analista de Qualidade de Software (QA)
**Empresa:** Local Eats | **Local:** Porto Alegre – RS (Híbrido)

**Sobre a vaga:**
Buscamos um profissional para estruturar a cultura de QA na Local Eats. Você será o braço direito do desenvolvimento, garantindo que nossas entregas sejam sólidas e sem bugs para os nossos usuários e restaurantes parceiros.

**Principais Responsabilidades:**
* Planejar e executar planos de teste para Web e Mobile.
* Documentar defeitos e colaborar com os desenvolvedores na correção.
* Apoiar na definição de critérios de qualidade para as novas funcionalidades.

**Requisitos:**
* **Obrigatórios:** Conhecimento em metodologias de teste; Capacidade analítica para identificar falhas de lógica.
* **Desejáveis:** Experiência com testes de API (Postman/Insomnia); Noções de automação.
* **Diferencial:** Certificação ISTQB-CTFL.

---

### Vaga 2: Desenvolvedor(a) Backend Junior/Pleno
**Empresa:** Local Eats | **Local:** Remoto

**Sobre a vaga:**
Buscamos alguém que valorize código bem escrito e testado. Sua missão será garantir que a lógica por trás dos pedidos na Local Eats seja infalível e escalável.

**Principais Responsabilidades:**
* Desenvolver APIs robustas seguindo boas práticas de arquitetura.
* Implementar testes unitários para as regras de negócio.
* Investigar e resolver problemas de concorrência e persistência de dados.

**Requisitos:**
* **Obrigatórios:** Lógica de programação sólida; Experiência com linguagens modernas (Node.js, Python ou similar); SQL.
* **Desejáveis:** Conhecimento em Docker e processos de CI/CD.