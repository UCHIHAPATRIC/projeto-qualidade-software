# Diagnóstico de Qualidade – Startup Local Eats

**Estudante:** Patric Morales Taborda  
**Disciplina:** Qualidade de Software  
**Atividade:** PBL – Diagnóstico Organizacional de QA  

---

# Diagnóstico de Qualidade – Startup Local Eats

## 1. Diagnóstico da Situação Atual

### 1.1 Papéis atuais identificados

Com base na análise do cenário da startup, os papéis que provavelmente compõem a equipa atual são:
<<<<<<< HEAD
=======

* **Desenvolvedores (Web e Mobile):** Responsáveis pela construção técnica do MVP. Devido ao prazo apertado, focam-se na entrega de código, acumulando funções de teste e implementação sem um processo formal.
* **Gerente de Produto (ou Proprietário da Startup):** Define as funcionalidades e prioriza o lançamento para eventos gastronómicos, focando-se mais no prazo de mercado do que na estabilidade técnica.
* **Analista de Sistemas / Requisitos:** Atua na tradução das necessidades dos comerciantes para a equipa técnica, mas a pressa na entrega sugere que o refinamento de cenários de exceção (como duplicidade de pedidos) não está a ser priorizado.
>>>>>>> 851864d5927350c2dc77f0dbc620f152fd1f13a9

* **Desenvolvedores:** Responsáveis pela construção técnica do MVP. Devido ao prazo apertado, focam-se na entrega de código, acumulando funções de teste e implementação sem um processo formal.
* **Gerente de Produto:** Define as funcionalidades e prioriza o lançamento para eventos gastronómicos, focando-se mais no prazo de mercado do que na estabilidade técnica.
* **Analista de Sistemas:** Atua na tradução das necessidades dos comerciantes para a equipa técnica, mas a pressa na entrega sugere que o refinamento de cenários de exceção (como duplicidade de pedidos) não está a ser priorizado.

### 1.2 Quem é responsável pela qualidade hoje?

Atualmente, a responsabilidade pela qualidade na Local Eats é **difusa e reativa**. Na prática, acredita-se que ela esteja sendo tratada da seguinte forma:

* **Responsabilidade Informal dos Desenvolvedores:** Como não há um papel de QA definido, os próprios desenvolvedores acabam sendo os únicos a testar o que produzem. No entanto, esses testes costumam ser superficiais (apenas para ver se o código "roda"), sem uma visão crítica de regras de negócio.
* **O Usuário como "Testador":** Pela descrição dos problemas, fica claro que a qualidade só é verificada após o lançamento. O usuário final está agindo como o primeiro filtro de bugs, o que gera uma percepção negativa da marca.
* **Tratamento Reativo:** A qualidade não é prevenida, mas "reparada". A equipe só atua nos defeitos após as reclamações chegarem à direção, indicando a ausência de uma cultura de prevenção ou de processos de validação antes do deploy.

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