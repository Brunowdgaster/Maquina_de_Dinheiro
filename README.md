# <span style="color:Green"> Maquina_de_Dinheiro</span>
## <span style="color:Blue"> Boot de Investimento</span>
 
 A ideia se resume a um boot capaz de realizar o máximo de transações de investimento day trade com a maior eficiência possível. Isso por meio de uma IA que analisa constantemente os dados financeiros de várias empresas.

<span style="font-size: 14px; color: red;">O código por trás da IA ainda está incompleto: </span>  
 A ideia atual é dividida em duas partes:
 A primeira parte é criar um código que analisando os dados ao longo prazo, de uma ação, para ter uma noção da variação diária, para se poder tentar prever dados de comportamento 'genéricos'(mais abrangentes com relação ao tempo) de uma ação. Exemplo: qual vai ser seu valor de fechamento de uma ação no final do dia ou ao decorrer do mês;
 A segunda parte é pegar fazer uma junção desses dados com a análise de comportamento da variação dos dados a curto prazo (variações em min), que embora sejam mais complexos de se obter a grande escala, eles fornecem uma análise mais precisa e adequado para transações day trade. Dois adendos importantes nessa etapa é que além de eu estar planejando um sistema de Banco de dados para se ter acesso a dados antigos (+ que 5 dias), essa etapa ´será executada constantemente sem parar, pois, quanto mais recente se obtém os dados dessa análise mais precisos eles serão na precisão.
 
<span style="font-size: 16px; color: yellow;">A Lógica Final: </span>
tendo esse esquema de predição, a lógica é simples o boot irá rodar uma lista das empresas day trade valorizando as mais baratas e antigas, ele prevê (por meio análise da IA) se essa ação tende a crescer em um curto período previsto, considerando uma margem de erro, se sim, o boot irá comprar essa ação e vende-lá no pico previsto, antes da queda. Também ainda quero ver se é possível mexer com a certeza da IA para também adiciona-la no cálculo da predição