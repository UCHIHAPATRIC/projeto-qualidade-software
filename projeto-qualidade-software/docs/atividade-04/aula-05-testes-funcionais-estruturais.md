# Testes Funcionais vs Estruturais – LocalEats

**Estudante:** Patric Morales Taborda  
**Disciplina:** Qualidade de Software  

---

## 1. Escolha da Funcionalidade

**Funcionalidade Selecionada:** Busca de Restaurantes  

* **O que a funcionalidade faz:** Permite que o usuário encontre estabelecimentos gastronômicos filtrando por critérios específicos como tipo de culinária (ex: Italiana, Japonesa), localização atual ou por bairro, e faixa de preço (barato, médio, luxo).
* **O que o usuário espera dela:** Resultados precisos e rápidos. O usuário espera que, ao filtrar por "Pizzaria" no "Centro", o sistema não mostre uma hamburgueria na Zona Sul ou retorne uma lista vazia quando existem locais disponíveis.

---

## 2. Testes Caixa-Preta (Visão do Usuário)

Nesta abordagem, testamos a funcionalidade através da interface, sem considerar o código interno, focando apenas em entradas e saídas.

* **Entradas possíveis:**
    * Texto livre no campo de busca (ex: "Sushi", "Burger").
    * Seleção de filtros via botões/checkboxes (ex: Faixa de preço "$$").
    * Uso da geolocalização do dispositivo.
* **Comportamentos esperados:**
    * Exibição de uma lista de cards de restaurantes que correspondam exatamente aos filtros aplicados.
    * Mensagem amigável de "Nenhum resultado encontrado" caso a busca não tenha correspondência.
* **Situações de erro (Testes de exceção):**
    * Inserir caracteres especiais ou campos vazios na busca.
    * Tentar buscar em uma localização onde o GPS está desativado.
    * Verificar se o sistema "limpa" os filtros corretamente ao iniciar uma nova pesquisa.

---

## 3. Testes Caixa-Branca (Visão do Sistema)

Aqui, focamos na estrutura lógica do código. Imaginamos como os algoritmos de busca e as consultas ao banco de dados foram implementados.

* **Possíveis estruturas lógicas e decisões:**
    * **Validações de Input:** Verificação se a string de busca não é nula ou perigosa (SQL Injection).
    * **Condicionais (If/Else):** Regras internas como `if (rating > 4.5) { destacar_restaurante() }` ou filtros de preço que selecionam faixas de valores no banco de dados.
    * **Laços de repetição (Loops):** Como o sistema percorre a lista de resultados retornada pelo banco para renderizar na tela.
* **Situações a serem testadas no código:**
    * Verificar se a consulta SQL/NoSQL está filtrando corretamente as chaves estrangeiras de categorias.
    * Testar o tratamento de erros quando o banco de dados demora a responder (timeout).
    * Validar se variáveis de memória estão sendo limpas após cada busca para evitar vazamento de memória e lentidão.

---

## 4. Comparação entre as Abordagens

| Característica | Teste Caixa-Preta (Funcional) | Teste Caixa-Branca (Estrutural) |
| :--- | :--- | :--- |
| **Foco principal** | Requisitos, experiência do usuário e saídas. | Lógica interna, fluxo de dados e caminhos de código. |
| **Quem geralmente faz** | QA, Analista de Testes ou Usuário Final. | Desenvolvedor ou QA com perfil técnico. |
| **Tipos de erros encontrados** | Funcionalidades faltando, erros de interface e falhas de usabilidade. | Caminhos lógicos não testados, erros de sintaxe, brechas de segurança e loops infinitos. |

---

## 5. Reflexão no contexto do LocalEats

No cenário atual da LocalEats, a abordagem de **Testes Caixa-Preta** parece ser a mais urgente para identificar por que o usuário está recebendo resultados incorretos, pois foca diretamente na dor do cliente. No entanto, para resolver os problemas de **lentidão em horários de pico**, a abordagem de **Testes Caixa-Branca** é indispensável para analisar a eficiência dos algoritmos e das conexões com o banco de dados.

**Conclusão:** Apenas uma abordagem não seria suficiente. Se usarmos apenas a Caixa-Preta, saberemos *que* o sistema está errado, mas não saberemos *por que* (lógica ruim ou erro de banco). Se usarmos apenas a Caixa-Branca, teremos um código tecnicamente perfeito, mas que pode não ser o que o usuário realmente precisa ou deseja. A integração das duas é o que garante a qualidade total.