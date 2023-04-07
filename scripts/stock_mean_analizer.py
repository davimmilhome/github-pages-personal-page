#IMPORTS
import pandas as pd, pandas_datareader as wb,numpy as np
import seaborn as sns, matplotlib.pyplot as plt, matplotlib.dates as mdates, exceptions as ex

import yfinance as yf
yf.pdr_override()

#Results Df

l_final_indicators = ['Ticker',
                    'Adj_Close',
                    'Mean_5Y',
                    'Mean_3Y',
                    'Mean_1y',
                    'Mean_6m',
                    'STD'
                    ]
df_result = pd.DataFrame(columns=l_final_indicators)


#Importando Ibovespa
#ibov = wb.DataReader('^BVSP', data_source = 'yahoo', start='2018-01-01')
#ibov.rename(columns = {'Adj Close': 'IBOV'}, inplace=True)
#ibov = ibov.drop(ibov.columns[[0,1,2,3,4]],axis=1)
#ibov_return = ibov.pct_change()
#ibov_return_acm=(1+ibov_return).cumprod()

def analyze_type():

    global comparation

    comparation = input('Selecione o tipo de análise:\nAnálise única - digite 0\nComparação de ativos - digite 1\n')
    
    while comparation not in ['0','1']:
        raise ex.InputError('Opção Inválida')

def ticker_chose():

    global ticker

    ticker = input('Escolha um ticker do Yahoo Finance, por exemplo, BPAC11.SA: ')

def actual_price():

    global df_result

    if comparation == '0':
        pass
    elif compartition == '1':
        pass

    ticker_chose()

    df = wb.get_data_yahoo(f'{ticker}', start ='2018-01-01')
    #df_ticker = yf.download(f'{ticker}', start ='2018-01-01')
    #df_ticker = wb.DataReader(f'{ticker}', data_source ='yahoo', start ='2018-01-01')
    #Adiciona a coluna date e substitui o index por números inteiros
    df_ticker.reset_index(inplace = True)

    #Fechamento - Preço e data de fechamento
    v_actual_date = df_ticker["Date"].iloc[-1].strftime('%d/%m/%y')
    v_close_price = round(df_ticker["Adj Close"].iloc[-1], 2)

    #Médias
    #Média 6 meses
    df_mean6m = df_ticker["Adj Close"].tail(180)
    v_mean6m = round(df_mean6m.mean(), 2)
    #Média 12 meses
    df_mean12m = df_ticker["Adj Close"].tail(360)
    v_mean12m = round(df_mean12m.mean(), 2)
    #Média 36 meses
    df_mean36m = df_ticker["Adj Close"].tail(1080)
    v_mean36m = round(df_mean36m.mean(), 2)
    #Média 60 meses
    df_mean60m = df_ticker["Adj Close"].tail(1800)
    v_mean60m = round(df_mean60m.mean(), 2)
    #Média definindo DF com a média
    list_mean = [v_mean60m, v_mean36m, v_mean12m, v_mean6m]
    df_mean = pd.DataFrame(list_mean)

    #Retorno percentual: Se trata de "preço_atual"/preço(t-1)
    df_return = pd.DataFrame(df_ticker["Adj Close"].pct_change())
    df_return["Date"] = df_ticker["Date"]
    df_return.set_index('Date',inplace=True, drop=True)
    #tirando a média dos retornos, periodicidade semanal
    mean_return = df_return.resample('W').mean()

    #std proxy volatility
    #std weekly returns
    std_ticket = round(float(df_return.std()),4)
    #std window_mean as a proxy to volatiliy
    return_meann_std = df_return.rolling(window=30).std()

    #Retorno acumulado
    return_acm = (1+df_return).cumprod()
    actual_return_acm = (round(return_acm.iloc[-1], 2))
#########################################################################################################################################
    #result_df_INSERT
    l_results = [ticker,v_close_price, df_mean6m, df_mean12m, df_mean36m, df_mean60m, std_ticket]
    df_result.loc[-1] = l_results
    #Saída
    print(f'Último fechamento: {v_actual_date, v_close_price}')
    print(f'Média de fechamento ajustado dos últimos 5 anos - 3 anos - 1 ano - 6 meses\n{list_mean}')
####################################################################################################################################
    #plt.plot(df_mean)
    x = ['média_5_anos', 'média_3_anos', 'média_1_ano', 'média_6_meses']
    plt.figure(figsize=(6, 6))
    plt.plot(x,list_mean,markersize=12,linestyle='solid', marker = ',')
    plt.xlabel("""Média dos últimos 'x' anos""", size = 8)
    plt.ylabel("Preço Médio", size = 8)
    plt.title(f'Movimento da média de preço (fechamento ajustado) ativo: {ticker}')
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
    plt.title(f'Movimento do preço defechamento ajustado ativo: {ticker}')
    plt.show()

    # plt.plot(returns_mean_weekly)
    df_return.plot.hist(bins=30)
    plt.title(f'Comportamento da média semanal dos retornos do ativo {ticker}')
    plt.show()

    # plt.plot(return_meann_std)
    return_meann_std.plot()
    #df_return.plot.hist(bins=30)
    plt.title(f'STD da média móvel de 30 dias como proxy para volatilidade do ativo {ticker}, STD dos retornos = {std_ticket} ', fontsize=8)
    plt.show()

    # plt.plot(return_acm)
    return_acm.plot()
    plt.title(f'Retorno acumulado normalizado pelo preço do ativo {ticker}')
    plt.show()

    #return_acm contra IBOV
    df_acm_ag_ibov = pd.merge(ibov_return_acm,return_acm,how='inner',on='Date')
    df_acm_ag_ibov.plot()
    plt.title(f'Retorno acumulado normalizado pelo preço do ativo {ticker} X retorno IBOV ', fontsize=8)
    plt.show()

if __name__ == '__main__':
    analyze_type()
    actual_price()
    print(df_result)


