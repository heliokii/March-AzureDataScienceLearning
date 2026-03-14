import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample data
data = {
    'Size': [1500, 1600, 1700, 1800, 1900],
    'Price': [300000, 320000, 340000, 360000, 380000]
}
df = pd.DataFrame(data)

# Prepare features (X) and target (y)
X = df[['Size']]  # Features
y = df['Price']   # Target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)
print("Predictions:", predictions)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Predict for a new size
new_size = [[2000]]
new_prediction = model.predict(new_size)
print("Predicted price for 2000 sq ft:", new_prediction[0])
