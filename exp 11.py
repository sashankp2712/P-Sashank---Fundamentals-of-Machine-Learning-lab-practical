import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
'Income':[25000,40000,50000,60000,15000,30000],
'Age':[25,35,45,50,23,40],
'CreditScore':['Low','Medium','High','High','Low','Medium']
}

df = pd.DataFrame(data)

X = df[['Income','Age']]
y = df['CreditScore']

# Encode labels
y = y.map({'Low':0,'Medium':1,'High':2})

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1)

model = LogisticRegression()

model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Predicted values:", pred)
print("Actual values:", list(y_test))

print("Accuracy:", accuracy_score(y_test,pred))
