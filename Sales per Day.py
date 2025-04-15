import pandas as pd
df=pd.read_csv('Data.csv')

print("Original dta:")
print(df)

total_sales_per_day=df.pivot_table(values='Price', index ='Day', aggfunc='sum')

print("\ntotal sales:")
print(total_sales_per_day)

#total sales per day line graph
import matplotlib.pyplot as plt

total_sales_per_day = df.pivot_table(values='Price', index='Day',aggfunc='sum')

plt.figure(figsize=(8,5))
plt.plot(total_sales_per_day.index, total_sales_per_day['Price'], marker='o', linestyle='-', color='teal')

plt.title('Daily sales')
plt.xlabel('Date')
plt.ylabel('total Sales ($)')
plt.grid(True)
plt.tight_layout()
plt.show()



