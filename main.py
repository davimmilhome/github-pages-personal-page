import pandas as pd, pandas_datareader as wb, numpy as np, seaborn as sns, matplotlib.pyplot as plt

ticket_escolhido = input('Escolha um ticket: ')

def actual_price(ticket):
    ticket_df = wb.DataReader(f'{ticket}', data_source = 'yahoo', start = '2018-01-01')
    print(f'Fechamento:\n {ticket_df["Close"].tail(1)}')


# btg = wb.DataReader('BPAC11.SA', data_source = 'yahoo', start = '2018-01-01')
#
# print(btg.columns)
#
# btg['High'].plot()
# #plt.plot(btg['High'])
# plt.show()

if __name__ == '__main__':
    actual_price(ticket_escolhido)



