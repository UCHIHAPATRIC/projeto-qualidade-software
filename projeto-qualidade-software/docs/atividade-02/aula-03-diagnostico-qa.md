# Diagnóstico de Qualidade – Startup Local Eats

**Estudante:** Patric Morales Taborda  
**Disciplina:** Qualidade de Software  
**Atividade:** PBL – Diagnóstico Organizacional de QA  

---

## 1. Diagnóstico da Situação Atual

A startup **Local Eats** enfrenta um cenário de "caos operacional" típico de crescimentos acelerados sem processos de validação. A análise do contexto revela falhas críticas de **Confiabilidade** e **Adequação Funcional**.

* **Identificação de Papéis Atuais:** Provavelmente a equipe conta apenas com Desenvolvedores e um Gerente de Produto, sem uma figura dedicada à qualidade.
* **Responsabilidade Atual:** A qualidade é tratada de forma reativa e nebulosa; não há um "dono" do processo de teste, o que permite que erros graves (como pedidos duplicados) cheguem ao usuário final.
* **Impactos Negativos:** Quando as responsabilidades não estão claras, ocorre o "efeito espectador" (todos acham que o outro testou), gerando retrabalho, perda de credibilidade com os lojistas e frustração dos clientes.
* **Conclusão:** A qualidade deve ser uma **responsabilidade compartilhada** por toda a equipe, com o QA atuando como facilitador e estrategista, e não apenas como um "executor de testes" ao final do processo.

## 2. Papéis da Equipe

Para profissionalizar o desenvolvimento, proponho a seguinte estrutura de papéis:

| Nome do Papel | Principais Responsabilidades | Relação com a Qualidade |
| :--- | :--- | :--- |
| **QA / Analista de Qualidade** | Planejar testes, gerir o ciclo de vida de bugs e validar critérios de aceite. | Atua como a voz do usuário e garante que o processo de QA seja seguido. |
| **Desenvolvedor** | Escrever código limpo, realizar testes unitários e de integração. | Garante a qualidade técnica na base da pirâmide de testes (previne o bug na origem). |
| **Analista de Sistemas** | Refinar requisitos, definir regras de negócio e validar protótipos. | Garante que o que está sendo construído resolve o problema certo (Qualidade de Requisito). |
| **DevOps** | Automatizar o pipeline de deploy (CI/CD) e monitorar a saúde da produção. | Garante que o sistema esteja disponível e que a entrega seja estável e segura. |

## 3. Responsabilidades relacionadas à qualidade

Abaixo, defino as atividades essenciais e seus respectivos responsáveis:

* **Revisar requisitos e regras de negócio:** Analista de Sistemas e QA.
* **Testar funcionalidades (Manual e Automático):** QA e Desenvolvedor.
* **Registrar e acompanhar defeitos (Bugs):** Toda a equipe (liderada pelo QA).
* **Validar funcionalidades antes da entrega (Homologação):** QA e Analista de Sistemas.
* **Implementar e monitorar testes unitários:** Desenvolvedor.

## 4. Práticas de QA Sugeridas

Como consultoria, recomendo a adoção imediata destas 4 práticas:

1.  **Registro e Acompanhamento de Bugs:** Utilização de uma ferramenta centralizada (ex: GitHub Issues) para documentar erros com passos para reprodução e severidade.
2.  **Revisão de Funcionalidades (Definition of Done):** Nenhuma tarefa é considerada pronta sem passar por um checklist de qualidade pré-definido.
3.  **Testes de Regressão Críticos:** Antes de qualquer deploy, validar o fluxo principal: Login -> Busca -> Pedido -> Pagamento.
4.  **Testes Exploratórios:** Sessões semanais de uso livre do sistema para identificar comportamentos inesperados que não foram previstos nos casos de teste.

## 5. Anúncios de Contratação

### Vaga 1: Analista de Qualidade de Software (QA)
**Empresa:** Local Eats | **Local:** Porto Alegre – RS (Híbrido)

**Sobre a vaga:**
Buscamos um QA para liderar a cultura de testes na Local Eats. Você será responsável por garantir que nossos clientes consigam pedir sua comida favorita sem falhas no sistema.

**Principais Responsabilidades:**
* Planejar e executar testes em aplicações Web e Mobile.
* Documentar e rastrear bugs críticos (como duplicidade de pedidos).
* Colaborar na definição de critérios de aceite para novas funcionalidades.

**Requisitos:**
* **Obrigatórios:** Conhecimento em metodologias de teste de software; Boa comunicação e senso crítico.
* **Desejáveis:** Experiência com Postman/Insomnia; Noções de automação de testes.
* **Certificações:** ISTQB-CTFL (Desejável).

---

### Vaga 2: Desenvolvedor(a) Backend Junior/Pleno
**Empresa:** Local Eats | **Local:** Remoto

**Sobre a vaga:**
Procuramos um desenvolvedor preocupado com a robustez e a lógica do sistema. Sua missão é construir APIs seguras e eficientes.

**Principais Responsabilidades:**
* Desenvolver funcionalidades seguindo padrões de código limpo.
* Escrever e manter testes unitários para as regras de negócio.
* Resolver problemas de concorrência e integridade de dados.

**Requisitos:**
* **Obrigatórios:** Lógica de programação sólida; Experiência com Node.js, Python ou C#; SQL.
* **Desejáveis:** Conhecimento em Docker e CI/CD; Experiência em sistemas de alta demanda.