import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset 
clinical_records = pd.read_csv(r'C:\Users\bolua\OneDrive\Documents\VSCode\Heart Problem Prediction\Code\heart_failure_clinical_records_dataset.csv')

# Creating a copy of the data to avoid the error I keep getting "SettingWithCopyWarning"
X = clinical_records.drop(columns=['time', 'DEATH_EVENT']).copy()  # Making a copy of the DataFrame
Y = clinical_records['DEATH_EVENT'] # Setting my Y axis/ values as Death Event

# Split the data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Standardizing the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Logistic Regression for Classification
logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_train_scaled, Y_train)  # Fit the logistic regression model
y_pred_logistic = logistic_model.predict(X_test_scaled)  # Predictions

# Logistic Regression
accuracy = accuracy_score(Y_test, y_pred_logistic)
conf_matrix = confusion_matrix(Y_test, y_pred_logistic)
class_report = classification_report(Y_test, y_pred_logistic)

print(f'Accuracy (Logistic Regression): {accuracy}')
print('Confusion Matrix:\n', conf_matrix)
print('Classification Report:\n', class_report)
