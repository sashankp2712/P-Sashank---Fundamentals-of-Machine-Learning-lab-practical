# FIND-S Algorithm Implementation

# Training data
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Number of attributes
num_attr = len(data[0]) - 1

# Initialize hypothesis with most specific values
hypothesis = ['Ø'] * num_attr

print("Initial Hypothesis:", hypothesis)

# FIND-S Algorithm
for example in data:
    if example[-1] == 'Yes':  # Only positive examples
        for i in range(num_attr):
            if hypothesis[i] == 'Ø':
                hypothesis[i] = example[i]
            elif hypothesis[i] != example[i]:
                hypothesis[i] = '?'
    print("Updated Hypothesis:", hypothesis)

print("\nFinal Hypothesis:", hypothesis)
