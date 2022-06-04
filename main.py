import pandas as pd, pandas_datareader as wb, numpy as np, seaborn as sns, matplotlib.pyplot as plt

btg = wb.DataReader('BPAC11.SA', data_source = 'yahoo', start = '2018-01-01')

print(btg.columns)

btg['High'].plot()
#plt.plot(btg['High'])
plt.show()

