import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data_challenge.csv')

# Calculate Revenue column
df['Revenue'] = df['Price'] * df['Units_Sold']

# Show the first few rows
print(df.head())

# Create a quick bar chart of Revenue per Product
df.plot(kind='bar', x='Product', y='Revenue', color='teal')
plt.title('Revenue by Product')
plt.ylabel('Dollars ($)')
plt.show()