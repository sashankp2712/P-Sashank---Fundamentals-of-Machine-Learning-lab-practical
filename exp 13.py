# Car Price Prediction using Linear Regression (from scratch)

# dataset: mileage vs price
mileage = [10, 15, 20, 25, 30]
price = [30000, 25000, 20000, 18000, 15000]

n = len(mileage)

mean_x = sum(mileage) / n
mean_y = sum(price) / n

num = 0
den = 0

for i in range(n):
    num += (mileage[i] - mean_x) * (price[i] - mean_y)
    den += (mileage[i] - mean_x) ** 2

b1 = num / den
b0 = mean_y - b1 * mean_x

print("Intercept:", b0)
print("Slope:", b1)

# prediction
x = float(input("Enter mileage: "))
predicted_price = b0 + b1 * x

print("Predicted Car Price:", predicted_price)
