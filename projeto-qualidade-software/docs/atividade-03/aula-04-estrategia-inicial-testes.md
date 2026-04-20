# Estratégia Inicial de Testes – LocalEats

**Estudante:** Patric Morales Taborda  
**Disciplina:** Qualidade de Software  

---

## 1. Funcionalidades Principais

Para esta estratégia inicial, selecionei as funcionalidades vitais para a operação do sistema:

1.  **Busca de Restaurantes:** Filtragem por culinária, localização e preço.
2.  **Visualização de Cardápios e Avaliações:** Exibição de itens, fotos e feedbacks de outros usuários.
3.  **Gerenciamento de Favoritos:** Ação de salvar e recuperar estabelecimentos preferidos.
4.  **Sistema de Recomendações:** Sugestões personalizadas com base no perfil do usuário.
5.  **Cadastro e Autenticação (Login):** Acesso seguro à conta e aos dados do usuário.

---

## 2. Níveis de Teste

Abaixo, defino como cada nível de teste será aplicado nas funcionalidades principais para garantir a cobertura total:

### Busca de Restaurantes
* **Teste Unitário:** Validar a lógica do algoritmo de filtro (ex: se o filtro "Japonesa" retorna apenas objetos do tipo "Sushi/Japonesa").
* **Teste de Integração:** Garantir que a aplicação consiga consultar a API de busca e receber o JSON com os dados corretamente.
* **Teste de Sistema:** Testar o fluxo completo na interface: digitar "Pizza" e verificar se os cards de pizzarias aparecem na tela.
* **Teste de Aceitação:** O usuário final consegue encontrar uma pizzaria aberta em um raio de 5km com preço acessível.

### Visualização de Cardápios e Avaliações
* **Teste Unitário:** Validar se a função de cálculo da média de estrelas das avaliações está correta.
* **Teste de Integração:** Verificar se a integração com o banco de dados de imagens (fotos dos pratos) está funcionando.
* **Teste de Sistema:** Validar se, ao clicar em um restaurante, todas as abas (Menu, Fotos, Reviews) carregam sem erros.
* **Teste de Aceitação:** O usuário consegue ler os preços e ver as fotos antes de decidir onde comer.

### Sistema de Recomendações
* **Teste Unitário:** Testar as funções matemáticas que classificam a preferência do usuário (pesos e tags).
* **Teste de Integração:** Validar a comunicação entre o banco de dados de histórico de pedidos e o motor de recomendação.
* **Teste de Sistema:** Verificar se a seção "Recomendados para Você" é exibida na Home após o login.
* **Teste de Aceitação:** O usuário sente que as recomendações são relevantes para o seu gosto pessoal.

---

## 3. Prioridades e Riscos

**Funcionalidade Crítica:** Busca de Restaurantes e Autenticação (Login).

* **Justificativa:** Se o usuário não consegue logar, ele nem entra no ecossistema. Se ele entra mas a busca retorna resultados incorretos (ou falha), o sistema perde sua função principal. O risco aqui é a **perda imediata de usuários** e a desvalorização da marca. Erros na busca são "bugs de negócio" graves que geram frustração instantânea.

---

## 4. Pirâmide de Testes

Para a LocalEats, a distribuição de esforços seguirá o padrão de eficiência:

1.  **Base (Testes Unitários):** Onde concentraremos a **maior quantidade**. Eles são rápidos, baratos e identificam erros de lógica (como os pedidos duplicados) antes que eles cheguem à interface.
2.  **Meio (Testes de Integração):** Quantidade intermediária. Focaremos em garantir que o App se comunique bem com o Servidor e Banco de Dados, essencial para resolver a "inconsistência entre web e mobile".
3.  **Topo (Testes de Sistema/E2E):** **Menor quantidade**. São testes lentos e caros. Focaremos apenas nos fluxos críticos (Caminho Feliz), como o processo de favoritar e buscar.

**Justificativa:** Investir na base da pirâmide garante que o sistema seja robusto por dentro, permitindo que a equipe de desenvolvimento da startup tenha ciclos de entrega mais rápidos com menos "quebras" inesperadas.

---

## 5. Testes em Produção

**O sistema deveria usar testes em produção?** Sim, com cautela.

* **Situações sugeridas:** Monitoramento sintético e *Canary Releases*.
* **Justificativa:** Como um dos problemas principais é a **lentidão em horários de pico**, apenas testes em ambiente de homologação (sem tráfego real) podem não ser suficientes. Usar testes em produção permite monitorar a performance com usuários reais e detectar latências em tempo real, permitindo que o time DevOps aja antes que o sistema caia totalmente durante um grande evento gastronômico.

---

## Conclusão da Estratégia
Esta estratégia foca em estabilizar o "coração" da LocalEats. Ao priorizar testes unitários e focar nos riscos de busca e performance, conseguimos dar à associação de comerciantes a segurança técnica que eles exigem para continuar a parceria.