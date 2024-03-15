import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

accepted_data = pd.read_csv("../data/accepted_data.csv",encoding='latin-1')
rejected_data = pd.read_csv("../data/rejected_data.csv",encoding='latin-1')

data = pd.concat([accepted_data,rejected_data])

# 特征选择
# features = ['loan_amnt','State','emp_length']
features = ['State']
X = data[features]
X = pd.get_dummies(X)
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test,y_pred))

coefficients = pd.DataFrame({
    'feature':X.columns,
    'coefficient':model.coef_[0]
})

print(coefficients)