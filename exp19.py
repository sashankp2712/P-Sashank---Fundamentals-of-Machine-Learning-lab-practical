# Naive Bayes for Bank Loan Prediction

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'Income': [25000, 40000, 50000, 60000, 20000, 30000, 70000, 80000],
    'Credit_Score': [600, 650, 700, 720, 580, 610, 750, 770],
    'Loan_Approved': [0, 1, 1, 1, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Income', 'Credit_Score']]
y = df['Loan_Approved']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = GaussianNB()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Test with new data
new_data = [[45000, 680]]
prediction = model.predict(new_data)

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Not Approved")
