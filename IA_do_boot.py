
#MEXER DIRETAMENTE COM OS DADOS

#pip install pandas-datareader --upgrade
#pip install tensorflow
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import time

#IA
#pip install scikit-learn
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

#Plotar tabelas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#regitro de cada ia treinada com os dados gerais a longa escala
IAs_treinadas = {}

#mostrar tabelas

def conf_tabela_padrao():pass #ver depois estetico

def mostrar_vetor_tabelas(vetor_tabelas, vaetor_nomes): 
    #mostrar graficos
    fig, axs = plt.subplots(nrows=len(vetor_tabelas), figsize=(100, 30*len(vetor_tabelas)))
    #print(vetor_tabelas)
    
    for i, t in enumerate(vetor_tabelas):
        # adicionar um gráfico em cada subplot
        plt.title(f"{vaetor_nomes[i]} Preco Acao")
        plt.xlabel('Tempo')
        plt.ylabel(f"{vaetor_nomes[i]} Preco Acao")
        plt.grid(True)
    
        # Defina o intervalo entre os valores do eixo x como sendo de uma hora
        intervalo_horario = mdates.HourLocator(interval=1)
        axs[i].xaxis.set_major_locator(intervalo_horario)
        
        # Use o formato de hora para as marcas do eixo x
        formato_horario = mdates.DateFormatter('%H:%M')
        axs[i].xaxis.set_major_formatter(formato_horario)

        #ajustar y
        #axs[i].set_yticks(np.linspace(axs[i].get_ybound()[0], axs[i].get_ybound()[1], 10))

        axs[i].plot(t)
        
    # ajustar os espaçamentos e mostrar o gráfico
    plt.tight_layout()
    plt.show()




#Selecionar acoes com maior chance de crecimento hoje
def init_Selecao(lista_tabelas): 
    numero_maximo_de_tops = 10 #ainda tem que calcular com base nos limites
    top = []

    #executar IAyouTube para predezir hoje



    #metodo de selecao das acoes com maior variação positiva




    return top

#iniciar treino da IA com a base
def inicializacao_Selecao(lista_tabelas): pass
    
    

    #pegar litas e mostrar as acoes que terao mais crecimento no dia 


# Metodos IAs

def IA_youTube_Treino(grafico_Treino, codigo, previsao_quantidade, quatidade_valor_futuro):
#criar padrão IA treinada que cada multhread tera  seu próprio
    
    #Preparar Dados para IA ler facilmente
    normalizando = MinMaxScaler(feature_range=(0,1))
    dados_normalizados = normalizando.fit_transform(grafico_Treino.values.reshape(-1,1))

    #previsao_quantidade de valores indicado ser 60

    x_treinar, y_treinar = [], []
    #ir adicionando os periodos de previsãp
    for x in range(previsao_quantidade, len(dados_normalizados)):
        x_treinar.append(dados_normalizados[x-previsao_quantidade:x, 0])
        y_treinar.append(dados_normalizados[x, 0 ])
        
    x_treinar, y_treinar = np.array(x_treinar), np.array(y_treinar)
    x_treinar = np.reshape(x_treinar, (x_treinar.shape[0], x_treinar.shape[1], 1))


    #Construindo nosso modelo de rede neural
    modelo = Sequential()

    modelo.add(LSTM(units=50, return_sequences=True, input_shape=(x_treinar.shape[1], 1)))
    modelo.add(Dropout(0.2))#desligar 20% do conhecimento
    modelo.add(LSTM(units=50, return_sequences=True))
    modelo.add(Dropout(0.2))
    modelo.add(LSTM(units=50))#memorizar 50 valores passados ############################################################ver se n entra em conflito quando previsao_dias<50 
    modelo.add(Dropout(0.2))
    modelo.add(Dense(units = quatidade_valor_futuro)) #Prevendo o proximos quatidade_valor_futuro do valor da acao

    modelo.compile(optimizer = 'adam', loss = 'mean_squared_error')
    modelo.fit(x_treinar, y_treinar, epochs = 25, batch_size = 32)#treinar25 interações e receber 32 pacotes de informações

    IAs_treinadas[codigo] = modelo 



def IA_youTube_Teste(grafico_Treino, grafico_Teste, codigo, n_previsoes_a_frente):# grafico_Treino(usados no treino da ia) por que ele já estão definidos
#criar padrão IA treinada que cada multhread tera  seu próprio
###Testando a precisao do nosso modelo em dados existentes

    #preparando alguns dados para teste

    total_dados = pd.concat((grafico_Treino, grafico_Teste), axis = 0)

    dados_teste = grafico_Teste

    modelo_entrada = total_dados[len(total_dados) - len(dados_teste) - n_previsoes_a_frente:].values
    modelo_entrada = modelo_entrada.reshape(-1, 1)
    modelo_entrada = normalizando.transform(modelo_entrada)


    #Fazer previsoes nos valores de teste

    x_teste = []

    for x in range(n_previsoes_a_frente, len(modelo_entrada)):
        x_teste.append(modelo_entrada[x-n_previsoes_a_frente:x, 0])
        
    x_teste = np.array(x_teste)
    x_teste = np.reshape(x_teste, (x_teste.shape[0], x_teste.shape[1], 1))

    previsao_precos = IAs_treinadas[codigo].predict(x_teste)
    previsao_precos = normalizando.inverse_transform(previsao_precos) #voltamdo aoformato original para poder comparar graficamente

    #Representando Graficamente as Previsoes
    plt.plot(precos_reais, color ='red', label = f"Valor Real das acoes de {empresa}")
    plt.plot(previsao_precos, color="green", label = f"Previsao das acoes de {empresa}" )
    plt.title(f"{empresa} Preco Acao")
    plt.xlabel('Tempo')
    plt.ylabel(f"{empresa} Preco Acao")
    plt.legend()
    plt.show()

    
    
    
    #TEM QUE CRIAR METODO PARA ESE DAQUI
    #Prevendo os proximos dias

    #dados_reais =  [modelo_entrada[len(modelo_entrada) + 1 - n_previsoes_a_frente:len(modelo_entrada + 1), 0]]
   # dados_reais =  np.array(dados_reais)
    #dados_reais = np.reshape(dados_reais, (dados_reais.shape[0], dados_reais.shape[1], 1))

    #previsao = modelo.predict(dados_reais)
    #previsao = normalizando.inverse_transform(previsao)

    #print(f"Previsao para amanha: {previsao}")



def IA_youTube(grafico_Treino, grafico_Teste): ### AINDA PRECISO ENTENDER E ALTERAR
#pegar grafico ações eprever o futuro

    #Preparar Dados
    normalizando = MinMaxScaler(feature_range=(0,1))
    dados_normalizados = normalizando.fit_transform(dados['Close'].values.reshape(-1,1))

    previsao_dias = 60

    x_treinar, y_treinar = [], []

    for x in range(previsao_dias, len(dados_normalizados)):
        x_treinar.append(dados_normalizados[x-previsao_dias:x, 0])
        y_treinar.append(dados_normalizados[x, 0 ])
        
    x_treinar, y_treinar = np.array(x_treinar), np.array(y_treinar)
    x_treinar = np.reshape(x_treinar, (x_treinar.shape[0], x_treinar.shape[1], 1))


    #Construindo nosso modelo de rede neural
    modelo = Sequential()

    modelo.add(LSTM(units=50, return_sequences=True, input_shape=(x_treinar.shape[1], 1)))
    modelo.add(Dropout(0.2))
    modelo.add(LSTM(units=50, return_sequences=True))
    modelo.add(Dropout(0.2))
    modelo.add(LSTM(units=50))
    modelo.add(Dropout(0.2))
    modelo.add(Dense(units = 1)) #Prevendo o proximo valor da acao

    modelo.compile(optimizer = 'adam', loss = 'mean_squared_error')
    modelo.fit(x_treinar, y_treinar, epochs = 25, batch_size = 32)

    ###Testando a precisao do nosso modelo em dados existentes

    #preparando alguns dados para teste
    teste_inicio = dt.datetime(2020,1,1)
    teste_final = dt.datetime.now()

    dados_teste = yf.download(empresa, start=inicio, end=final)
    precos_reais = dados_teste['Close'].values

    total_dados = pd.concat((dados['Close'], dados_teste['Close']), axis = 0)

    modelo_entrada = total_dados[len(total_dados) - len(dados_teste) - previsao_dias:].values
    modelo_entrada = modelo_entrada.reshape(-1, 1)
    modelo_entrada = normalizando.transform(modelo_entrada)


    #Fazer previsoes nos valores de teste

    x_teste = []

    for x in range(previsao_dias, len(modelo_entrada)):
        x_teste.append(modelo_entrada[x-previsao_dias:x, 0])
        
    x_teste = np.array(x_teste)
    x_teste = np.reshape(x_teste, (x_teste.shape[0], x_teste.shape[1], 1))

    previsao_precos = modelo.predict(x_teste)
    previsao_precos = normalizando.inverse_transform(previsao_precos)

    #Representando Graficamente as Previsoes
    plt.plot(precos_reais, color ='red', label = f"Valor Real das acoes de {empresa}")
    plt.plot(previsao_precos, color="green", label = f"Previsao das acoes de {empresa}" )
    plt.title(f"{empresa} Preco Acao")
    plt.xlabel('Tempo')
    plt.ylabel(f"{empresa} Preco Acao")
    plt.legend()
    plt.show()

    #Prevendo os proximos dias

    dados_reais =  [modelo_entrada[len(modelo_entrada) + 1 - previsao_dias:len(modelo_entrada + 1), 0]]
    dados_reais =  np.array(dados_reais)
    dados_reais = np.reshape(dados_reais, (dados_reais.shape[0], dados_reais.shape[1], 1))

    previsao = modelo.predict(dados_reais)
    previsao = normalizando.inverse_transform(previsao)

    print(f"Previsao para amanha: {previsao}")


def IAnalise(Grafico_cotacao_recente, Grafico_otacao_Geral, Tabela_DRE_e_mais, Tempo_fechamento, saldo_atual):pass
    #compra






    #return: compra, vende, espera



#Checagem
def oi(): 
    print("eu estou legal")

def teste_aqui():pass #testar codigo 




print("Confere")