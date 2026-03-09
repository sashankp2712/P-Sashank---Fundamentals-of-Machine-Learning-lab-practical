import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Sample dataset
X = np.array([1,2,3,4,5,6]).reshape(-1,1)
y = np.array([2,5,7,10,15,20])

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X,y)

linear_pred = linear_model.predict(X)

# Polynomial Regression
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly,y)

poly_pred = poly_model.predict(X_poly)

print("Input Values:", X.flatten())
print("Actual Output:", y)

print("\nLinear Regression Predictions:")
print(linear_pred)

print("\nPolynomial Regression Predictions:")
print(poly_pred)
