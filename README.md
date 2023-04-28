# Maquina_de_Dinheiro
 A ideia se resume a um boot capaz de realizar o máximo de transações de investimento day trade com a maior eficiência possivel. Isso por meio de uma IA que analisa constantemente os dados financeiros de várias empresas

O código por trás da IA ainda está incompleto:
 A idéia atual é dividida em duas partes:
 A primeira parte écriar um código que analisando os dados ao longo prazo, de uma ação, para ter um noção da variação diária, para se poder tentar prever dados  de comportamento 'génericos'(mais abrangentes com relação ao tempo) de uma ação. Exemplo: qual vai ser seu valor de fechamento de uma ação no final do dia ou ao  decorrer do mês;
 A segunda parte é pegar fazer uma junção desses dados com a analise de compotarmento da variação dos dados a curto prazo (variações em min), que embora sejam mais complexos de se obter a grande escala, eles fornecem uma analise mais precisa e adequado para transações day trade. Dois adendos importantes nessa etapa é que além de eu estár planejando um sistema de Banco de dados para se ter acesso a dados antigos (+ que 5 dias), eessa etapa ´será executada constantemente sem parar poís quanto mais recente se obtem os dados dessa analise mais precisos eles serão na precisão.
 
A lógica final: tendo esse esquema de predição a lógica é simples o boot irá rodar uma lista das empresas day trade valorizando as mais baratas e antigas, ele preve por essa analise da IA se essa ação tende a crecer em um periodo previsto, considerando uma margem de erro, ele ira comprar uma dessa ação vender no pico previsto, antes da queda. Também ainda quero ver se é possivel mexer com a certeza de uma IA para também adiciona-la no cálculoda da predição
