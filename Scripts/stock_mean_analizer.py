#IMPORTS
import pandas as pd, pandas_datareader as wb,numpy as np
import seaborn as sns, matplotlib.pyplot as plt, matplotlib.dates as mdates


ticket_escolhido = input('Escolha um ticket do Yahoo Finance, por exemplo, BPAC11.SA: ')

def actual_price(ticket):
    df_ticker = wb.DataReader(f'{ticket}', data_source ='yahoo', start ='2018-01-01')

    #Adiciona a coluna date e substitui o index por números inteiros
    df_ticker.reset_index(inplace = True)

    #Fechamento - Preço e data de fechamento
    v_actual_date = df_ticker["Date"].iloc[-1].strftime('%d/%m/%y')
    v_actual_price = round(df_ticker["Adj Close"].iloc[-1], 2)

    #Médias
    df_mean_6m = df_ticker["Adj Close"].tail(180)
    v_mean_6m = round(df_mean_6m.mean(), 2)

    df_mean_12m = df_ticker["Adj Close"].tail(360)
    v_mean_12m = round(df_mean_12m.mean(), 2)

    df_mean_36m = df_ticker["Adj Close"].tail(1080)
    v_mean_36m = round(df_mean_36m.mean(), 2)

    df_mean_60m = df_ticker["Adj Close"].tail(1800)
    v_mean_60m = round(df_mean_60m.mean(), 2)

    list_mean = [v_mean_60m,v_mean_36m,v_mean_12m,v_mean_6m]
    df_mean = pd.DataFrame(list_mean)

    #Retorno percentual: Se trata de "preço_atual"/preço(t-1)
    df_return = pd.DataFrame(df_ticker["Adj Close"].pct_change())
    df_return["Date"] = df_ticker["Date"]
    df_return.set_index('Date',inplace=True, drop=True)
    mean_return = df_return.resample('W').mean()


    #Saída
    print(f'Último fechamento: {v_actual_date,v_actual_price}')
    print(f'Média de fechamento ajustado dos últimos 5 anos - 3 anos - 1 ano - 6 meses\n{list_mean}')

    #plt.plot(df_mean)
    x = ['média_5_anos', 'média_3_anos', 'média_1_ano', 'média_6_meses']
    plt.figure(figsize=(6, 6))
    plt.plot(x,list_mean,markersize=12,linestyle='solid', marker = ',')
    plt.xlabel("""Média dos últimos 'x' anos""", size = 8)
    plt.ylabel("Preço Médio", size = 8)
    plt.title(f'Movimento da média de preço (fechamento ajustado) ativo: {ticket}')
    for a, b in zip(x, list_mean):
        plt.text(a, b, str(b))
    plt.show()

    #plt.plot(Adjuste close in general)
    x = df_ticker["Date"]
    plt.figure(figsize=(6, 6))
    plt.plot(x, df_ticker["Adj Close"], markersize=12, linestyle='solid', marker =',')
    #plt.xlabel()
    dtFmt = mdates.DateFormatter('%Y') #Selecionando o formato da data
    plt.gca().xaxis.set_major_formatter(dtFmt) #Ajustando a data no eixo  X
    plt.ylabel("Preço Ajustado", size = 8)
    plt.title(f'Movimento do preço defechamento ajustado ativo: {ticket}')
    plt.show()

    # plt.plot(returns_mena_weekly)
    df_return.plot.hist(bins=30)
    plt.title(f'Comportamento da média semanal dos retornos do ativo {ticket}')
    plt.show()

if __name__ == '__main__':
    actual_price(ticket_escolhido)



