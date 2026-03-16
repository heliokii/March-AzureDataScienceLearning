import pandas as pd
import numpy as np

# Create a DataFrame with some missing values
data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Price': [10.5, np.nan, 15.0, 12.5],  # np.nan simulates missing data
    'Quantity': [100, 150, 200, 120]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Basic statistics
print("\nStatistics:\n", df.describe())

# Handle missing values: Fill NaN with mean price
mean_price = df['Price'].mean()
df['Price'].fillna(mean_price, inplace=True)
print("\nDataFrame after filling NaN:\n", df)

# Compute total value
df['Total'] = df['Price'] * df['Quantity']
print("\nDataFrame with Total:\n", df)
