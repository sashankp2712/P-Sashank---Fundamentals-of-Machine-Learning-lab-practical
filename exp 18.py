# Perceptron Algorithm

data = [
[2,1,1],
[1,3,1],
[2,3,1],
[3,1,-1],
[3,2,-1],
[4,1,-1]
]

w1 = 0
w2 = 0
bias = 0
lr = 0.1

for epoch in range(10):
    for row in data:

        x1 = row[0]
        x2 = row[1]
        y = row[2]

        output = w1*x1 + w2*x2 + bias

        if output >= 0:
            pred = 1
        else:
            pred = -1

        if pred != y:
            w1 = w1 + lr*y*x1
            w2 = w2 + lr*y*x2
            bias = bias + lr*y

print("Weights:",w1,w2)
print("Bias:",bias)
