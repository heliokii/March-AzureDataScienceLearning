import numpy as np
import pandas as pd

# Create a NumPy array and perform basic operations
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean:", np.mean(arr))  # Output: 3.0
print("Squared:", arr ** 2)   # Output: [1 4 9 16 25]

# Create a Pandas DataFrame (like a table)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Filter rows where Age > 30
filtered = df[df['Age'] > 30]
print("\nFiltered DataFrame:\n", filtered)

# Add a new column
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus:\n", df)
