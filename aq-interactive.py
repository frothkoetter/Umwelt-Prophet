warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

DATAPATH = 'data/AirQualityUCI.csv'

data = pd.read_csv(DATAPATH, sep=';')
data.head()
data.shape


data.dropna(axis=1, how='all', inplace=True)
data.dropna(axis=0, how='all', inplace=True)


data.shape
data.head()

data['Date'] = pd.to_datetime(data['Date'])

for col in data.iloc[:,2:].columns:
    if data[col].dtypes == object:
        data[col] = data[col].str.replace(',', '.').astype('float')
        
        
def positive_average(num):
    return num[num > -200].mean()
    
daily_data = data.drop('Time', axis=1).groupby('Date').apply(positive_average)

daily_data.head()

daily_data.isna().sum() > 8

daily_data = daily_data.iloc[:,(daily_data.isna().sum() <= 8).values]
daily_data.head()
daily_data.shape
daily_data = daily_data.dropna()
daily_data.shape

weekly_data = daily_data.resample('W').mean()


weekly_data.head()
weekly_data = weekly_data.dropna()
weekly_data = weekly_data.dropna()

def plot_data(col):
    plt.figure(figsize=(17, 8))
    plt.plot(weekly_data[col])
    plt.xlabel('Time')
    plt.ylabel(col)
    plt.grid(False)
    plt.show()
    
for col in weekly_data.columns:
    plot_data(col)
    
    
# cols_to_drop = ['PT08.S1(CO)', 'C6H6(GT)', 'PT08.S2(NMHC)', 'PT08.S4(NO2)', 'PT08.S5(O3)', 'T', 'RH', 'AH']
#
# weekly_data = weekly_data.drop(cols_to_drop, axis=1)
