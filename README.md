# 1. Problema de negócio
    O projeto foi criado para ajudar um novo CEO Kleiton Guerra
    a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer
    utilizando dados!
    A empresa Zomato é uma marketplace de restaurantes. Ou seja, seu core business é facilitar 
    o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro 
    da plataforma da Culinary Jorney, que disponibiliza informações como:
    endereço, tipo de culinária servida, se possui reservas, se faz entregas e 
    também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.
    
# 2. Premissas assumidas para a análise
####      1. A análise foi realizada com dados baseados em localização e valores, sem data.
####      2. Marketplace foi o modelo de negócio assumido.
####      3. As principais visões do negócio foram: 
              => Visão geral do negócio; 
              => Visão do negócio por País;
              => Visão do negócio por Cidades;
              => Visão do negócio por Tipo de culinária;
    
# 3. Estratégia da solução
####    O painel estratégico foi desenvolvido utilizando as métricas para que o CEO fosse capaz de ter uma visão mais detalhada do negócio:
          1. Visão geral dos cadastros na plataforma.
          2. Visão por país.
          3. Visão por cidade.
          4. Visão por tipo de culinária.
    
####    Cada visão é representada pelo seguinte conjunto de métricas.
          1. Visão geral dos cadastros na platafoma
              a. Número total de restaurantes cadastrados.
              b. Número total de países cadastrados.
              c. Quantidade total de avaliações feitas na plataforma.
              d. Quantidade total de tipos de cozinha cadastrados.
              e. Mapa interativo mostrando a localização dos restaurantes, permitindo a consulta individualizada de cada um.
            
         2.  Visão por país.
              a. Número de restaurantes registrados por país.
              b. Número de cidades registradas por país.
              c. Média de avaliações feitas por país.
              d. Média de preço de refeição para duas pessoas.

         3. Visão por cidade.
              a. Top 10 cidades com mais restaurantes registrados.
              b. Top 7 cidades com restaurantes com média de avaliação acima de 4.
              c. Top 7 cidades com restaurantes com média de avaliação abaixo de 2,5.
              d. Top 10 cidades com tipos de culinárias mais variadas.

         4. Visão por tipo de culinária.
              a. Informa 5 restaurantes com as melhores médias.
              b. Mostra uma tabela com detalhes sobre os restaurantes.
              c. Top 10 de culinárias com as melhores médias de avaliação. 
              d. Top 10 de culinárias com as piores médias de avaliação.

# 4. Top 3 Insights de dados
    1. O mapa geral mostra que alguns mercados podem ser mais explorados, como o mercado europeu e o brasileiro, onde apenas algumas cidades possuem cadastro. 
        
    2. O número de avaliações não é diretamente proporcional ao número de restaurantes cadastrados por país. E a quantidade máxima de registros
    por cidade são 80 restaurantes. 
    
    3. Seria interessante verificar mais detalhadamente os restaurantes com avaliações abaixo de 2,5 para que não abandonem a plataforma, 
    e sim melhorem seu desempenho no serviço.

# 5. O produto final do projeto
    Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.
    O painel pode ser acessado através desse link: https://cjourneycompany.streamlit.app/Main_Page
    
# 6. Conclusão
    O projeto exibe um conjunto de gráficos e tabelas que permitem o CEO ter uma visão geral da empresa e movimentar o time para proximos
    passos estratégicos para melhorar a participação do marketplace no mercado. 
