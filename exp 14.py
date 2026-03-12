# House Price Prediction

# dataset: size vs price
size = [800, 1000, 1200, 1500, 1800]
price = [150000, 200000, 240000, 300000, 360000]

n = len(size)

mean_x = sum(size) / n
mean_y = sum(price) / n

num = 0
den = 0

for i in range(n):
    num += (size[i] - mean_x) * (price[i] - mean_y)
    den += (size[i] - mean_x) ** 2

b1 = num / den
b0 = mean_y - b1 * mean_x

print("Intercept:", b0)
print("Slope:", b1)

x = float(input("Enter house size: "))
predicted = b0 + b1 * x

print("Predicted House Price:", predicted)
