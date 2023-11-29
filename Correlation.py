import pandas as panda
import seaborn as sea
import matplotlib.pyplot as plot
import scipy.stats as stats

# Read CSV file into a DataFrame
df_ = panda.read_csv('diamonds.csv')  
df_ = df_.drop('index', axis=1, errors='ignore')
# 7. Correlation Analysis
# Calculate the correlation between price and all other numeric columns.
correlation_matrix = df_.select_dtypes(include=['float64', 'int64']).corr()

# Create a heatmap
plot.figure(figsize=(10, 8))
sea.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plot.title('Correlation Heatmap')
plot.show()
