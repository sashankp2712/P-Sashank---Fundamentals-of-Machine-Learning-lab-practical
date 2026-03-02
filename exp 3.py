import pandas as pd
import math

# Calculate entropy
def entropy(data):
    target = data.iloc[:, -1]
    values = target.value_counts()
    ent = 0
    for v in values:
        p = v / len(data)
        ent -= p * math.log2(p)
    return ent

# Calculate information gain
def information_gain(data, attribute):
    total_entropy = entropy(data)
    values = data[attribute].unique()
    weighted_entropy = 0
    
    for v in values:
        subset = data[data[attribute] == v]
        weighted_entropy += (len(subset)/len(data)) * entropy(subset)
    
    return total_entropy - weighted_entropy

# ID3 Algorithm
def id3(data, attributes):
    target = data.iloc[:, -1]
    
    # If all examples are same
    if len(target.unique()) == 1:
        return target.iloc[0]
    
    # If no attributes left
    if len(attributes) == 0:
        return target.mode()[0]
    
    # Select attribute with max information gain
    gains = [information_gain(data, attr) for attr in attributes]
    best_attr = attributes[gains.index(max(gains))]
    
    tree = {best_attr: {}}
    
    for value in data[best_attr].unique():
        subset = data[data[best_attr] == value]
        if subset.empty:
            tree[best_attr][value] = target.mode()[0]
        else:
            remaining_attrs = [a for a in attributes if a != best_attr]
            tree[best_attr][value] = id3(subset, remaining_attrs)
    
    return tree

# Load dataset
data = pd.read_csv("tennis.csv")

attributes = list(data.columns[:-1])
tree = id3(data, attributes)

print("Decision Tree:")
print(tree)
