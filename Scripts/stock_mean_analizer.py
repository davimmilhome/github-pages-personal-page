import pandas as pd, pandas_datareader as wb, numpy as np, seaborn as sns, matplotlib.pyplot as plt

ticket_escolhido = input('Escolha um ticket do Yahoo Finance, por exemplo, BPAC11.SA: ')

def actual_price(ticket):
    ticket_df = wb.DataReader(f'{ticket}', data_source = 'yahoo', start = '2018-01-01')

    #Adiciona a coluna date e substitui o index por números inteiros
    ticket_df.reset_index(inplace = True)

    #Fechamento - Preço e data de fechamento
    v_actual_date = ticket_df["Date"].iloc[-1].strftime('%d/%m/%y')
    v_actual_price = round(ticket_df["Close"].iloc[-1],2)

    #Médias
    df_mean_6m = ticket_df["Close"].tail(180)
    v_mean_6m = round(df_mean_6m.mean(), 2)

    df_mean_12m = ticket_df["Close"].tail(360)
    v_mean_12m = round(df_mean_12m.mean(), 2)

    df_mean_36m = ticket_df["Close"].tail(1080)
    v_mean_36m = round(df_mean_36m.mean(), 2)

    df_mean_60m = ticket_df["Close"].tail(1800)
    v_mean_60m = round(df_mean_60m.mean(), 2)

    list_mean = [v_mean_60m,v_mean_36m,v_mean_12m,v_mean_6m]
    df_mean = pd.DataFrame(list_mean)

    #Saída
    print(f'Último fechamento: {v_actual_date,v_actual_price}')
    print(f'Média de fechamento dos últimos 5 anos - 3 anos - 1 ano - 6 meses\n{list_mean}')

    #plt.plot(df_mean)
    x = ['média_5_anos', 'média_3_anos', 'média_1_ano', 'média_6_meses']
    plt.figure(figsize=(6, 6))
    plt.plot(x,list_mean,markersize=12,linestyle='solid', marker = ',')
    plt.xlabel("""Média dos últimos 'x' anos""", size = 8)
    plt.ylabel("Preço Médio", size = 8)
    plt.title(f'Movimento da média de preço ativo: {ticket}')
    for a, b in zip(x, list_mean):
        plt.text(a, b, str(b))
    plt.show()

if __name__ == '__main__':
    actual_price(ticket_escolhido)



