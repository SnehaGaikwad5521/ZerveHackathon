import pandas as pd

# Load data and compute revenue column
df = pd.read_csv('data_challenge.csv')
df['Revenue'] = df['Price'] * df['Units_Sold']

# Calculate laptop revenue percentage of total revenue
total_revenue = df['Revenue'].sum()
laptop_revenue = df[df['Product'] == 'Laptop']['Revenue'].sum()
percentage = (laptop_revenue / total_revenue) * 100

print(f"Laptop Revenue:  ${laptop_revenue:,.2f}")
print(f"Total Revenue:   ${total_revenue:,.2f}")
print(f"Laptops account for {percentage:.2f}% of total revenue!")
