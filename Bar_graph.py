import pandas as pds
import seaborn as sea
import matplotlib.pyplot as plot
import scipy.stats as stats


df_ = pds.read_csv('diamonds.csv')  
df_ = df_.drop('index', axis=1, errors='ignore')
sea.countplot(x='cut', data=df_)
plot.show()

sea.countplot(x='color', data=df_)
plot.show()

sea.countplot(x='clarity', data=df_)
plot.show()
