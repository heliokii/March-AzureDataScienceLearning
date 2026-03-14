import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [200, 300, 250, 400]
}
df = pd.DataFrame(data)

# Line plot with Matplotlib
plt.figure(figsize=(8, 4))
plt.plot(df['Month'], df['Sales'], marker='o', color='b')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()  # This will display a line chart

# Bar plot with Seaborn
plt.figure(figsize=(8, 4))
sns.barplot(x='Month', y='Sales', data=df, palette='viridis')
plt.title('Monthly Sales Bar Chart')
plt.show()  # This will display a bar chart
