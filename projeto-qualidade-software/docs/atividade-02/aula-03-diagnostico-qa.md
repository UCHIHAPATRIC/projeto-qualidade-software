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

