#quantity sales by category & visualisation
import pandas as pd
df=pd.read_csv('Data.csv')
import matplotlib.pyplot as plt

category_counts = df['Category'].value_counts()

plt.figure(figsize=(7,5))
plt.bar(category_counts.index, category_counts.values, color=['#FF6B6B', '#4ECDC4','#FFD93D'])
    
plt.title('Product Demand by Category')
plt.xlabel('Category')
plt.ylabel('Number of Items Sold')
plt.tight_layout()
plt.show()

category_revenue = df.groupby('Category')['Price'].sum()

plt.figure(figsize=(7,5))
plt.bar(category_revenue.index, category_revenue.values, color=['#FFA07A','#87CEEB','#B0E57C'])

plt.title('Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Total Revenue ($)')
plt.tight_layout()
plt.show()