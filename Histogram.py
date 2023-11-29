import pandas as panda
import seaborn as sea
import matplotlib.pyplot as plot
import scipy.stats as stats

# Read CSV file into a DataFrame
df = panda.read_csv('diamonds.csv')  
df = df.drop('index', axis=1, errors='ignore')
plot.hist(df['carat'], bins=range(0, int(df['carat'].max()) + 1, 1))
plot.xlabel('carat')
plot.ylabel('No of Diamonds')
plot.show()
