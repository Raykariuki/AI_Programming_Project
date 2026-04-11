# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dataset Loading
data = {
    "Size": [650, 800, 1200, 1500, 2000, 2500],
    "Price": [70000, 85000, 120000, 150000, 200000, 250000]
}
df = pd.DataFrame(data)

# Features (X) and target (y)
X = df[["Size"]]
y = df["Price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))
print("y_pred:", y_pred)