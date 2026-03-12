# Naive Bayes Iris Classification (simplified)

dataset = [
[5.1,3.5,1.4,0.2,'setosa'],
[4.9,3.0,1.4,0.2,'setosa'],
[6.2,3.4,5.4,2.3,'virginica'],
[5.9,3.0,5.1,1.8,'virginica'],
[5.5,2.3,4.0,1.3,'versicolor'],
[6.5,2.8,4.6,1.5,'versicolor']
]

classes = {}

for row in dataset:
    label = row[-1]
    if label not in classes:
        classes[label] = 0
    classes[label] += 1

total = len(dataset)

print("Class Probabilities")

for c in classes:
    prob = classes[c] / total
    print(c, ":", prob)

# simple prediction (majority class)
prediction = max(classes, key=classes.get)

print("Predicted Class:", prediction)
