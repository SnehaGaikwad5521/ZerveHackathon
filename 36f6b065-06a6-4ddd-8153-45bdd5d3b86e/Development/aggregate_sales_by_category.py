import pandas as pd

# Load the data
_df = pd.read_csv('data_challenge.csv')

# Run SQL-style aggregation using pandas (no pandasql needed)
sql_query_result = (
    _df.groupby('Category')
    .agg(
        Total_Units=('Units_Sold', 'sum'),
        Total_Revenue=('Price', lambda x: (x * _df.loc[x.index, 'Units_Sold']).sum())
    )
    .reset_index()
    .sort_values('Total_Units', ascending=False)
    .reset_index(drop=True)
)

print("--- SQL Query DataFrame Results ---")
print(sql_query_result)