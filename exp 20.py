# Future Sales Prediction using Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data (Days vs Sales)
days = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
sales = np.array([200, 220, 250, 270, 300, 320])

# Model
model = LinearRegression()
model.fit(days, sales)

# Predict future sales (Day 7)
future_day = np.array([[7]])
predicted_sales = model.predict(future_day)

print("Predicted Sales for Day 7:", predicted_sales[0])
