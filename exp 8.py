# Linear Regression Implementation (without sklearn)

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

n = len(x)

# Calculate mean
mean_x = sum(x) / n
mean_y = sum(y) / n

# Calculate slope (m) and intercept (c)
numerator = 0
denominator = 0

for i in range(n):
    numerator += (x[i] - mean_x) * (y[i] - mean_y)
    denominator += (x[i] - mean_x) ** 2

m = numerator / denominator
c = mean_y - m * mean_x

print("Slope (m):", m)
print("Intercept (c):", c)

# Predict value
x_new = 6
y_pred = m * x_new + c

print("Predicted value for x =", x_new, "is:", y_pred)
