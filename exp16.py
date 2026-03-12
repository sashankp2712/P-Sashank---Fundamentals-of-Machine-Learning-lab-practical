# Compare Classification Algorithms

dataset = [
[1,1,'A'],
[1,2,'A'],
[2,1,'A'],
[4,5,'B'],
[5,4,'B'],
[5,5,'B']
]

# KNN Classification
def knn(test):
    distances = []

    for row in dataset:
        d = ((row[0]-test[0])**2 + (row[1]-test[1])**2)**0.5
        distances.append((d,row[2]))

    distances.sort()

    neighbors = distances[:3]

    votes = {}
    for n in neighbors:
        label = n[1]
        votes[label] = votes.get(label,0)+1

    return max(votes,key=votes.get)

# Naive Bayes (majority)
def naive_bayes():
    count={}
    for row in dataset:
        label=row[2]
        count[label]=count.get(label,0)+1
    return max(count,key=count.get)

test=[2,2]

print("KNN Prediction:",knn(test))
print("Naive Bayes Prediction:",naive_bayes())
