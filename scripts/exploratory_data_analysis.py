import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data/e_commerce_dataset.csv')
print(data.head())
print(data.describe())


data.groupby('OrderDate')['TotalPrice'].sum().plot()
plt.show()

data.groupby('ProductCategory')['TotalPrice'].sum().plot(kind='bar')
plt.show()
