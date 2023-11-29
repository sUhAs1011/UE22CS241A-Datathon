import pandas as panda
import seaborn as sns
import matplotlib.pyplot as plot
import scipy.stats as stats

# Read CSV file into a DataFrame
df_ = panda.read_csv('diamonds.csv')  
stats.probplot(df_['carat'], dist="norm", plot=plot)
plot.title('Normal Probability Plot For Carat')
plot.show()
