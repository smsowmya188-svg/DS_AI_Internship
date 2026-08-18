import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report)

data = {
    "income": [
        25000, 30000, 45000, 50000, 60000,
        70000, 80000, 35000, 40000, 90000,
        28000, 32000, 55000, 65000, 75000,
        22000, 38000, 48000, 58000, 85000
    ],

    "credit_score": [
        580, 600, 650, 700, 720,
        750, 780, 620, 640, 800,
        590, 610, 690, 710, 760,
        570, 630, 660, 730, 790
    ],

    "loan_amount": [
        200000, 250000, 150000, 300000, 250000,
        200000, 300000, 280000, 220000, 250000,
        350000, 300000, 180000, 200000, 250000,
        400000, 270000, 200000, 180000, 220000
    ],

    "employment_status": [
        "Unemployed", "Self-employed", "Employed", "Employed", "Employed",
        "Employed", "Employed", "Self-employed", "Employed", "Employed",
        "Unemployed", "Self-employed", "Employed", "Employed", "Employed",
        "Unemployed", "Self-employed", "Employed", "Employed", "Employed"
    ],

    "previous_payment_history": [
        1, 2, 5, 6, 7,
        8, 9, 3, 5, 10,
        1, 2, 6, 7, 8,
        0, 4, 5, 7, 9
    ],

    "default": [
        1, 1, 0, 0, 0,
        0, 0, 1, 0, 0,
        1, 1, 0, 0, 0,
        1, 1, 0, 0, 0
    ]}

df = pd.DataFrame(data)
print("Dataset:")
print(df)

encoder = LabelEncoder()
df["employment_status"] = encoder.fit_transform(
    df["employment_status"])

print("\nAfter Encoding:")
print(df)

X = df.drop("default", axis=1)
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("\n----- MODEL PERFORMANCE -----")
print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1)

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["No Default", "Default"],
    zero_division=0))

cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

display = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["No Default", "Default"])

display.plot()
plt.title("Loan Default Prediction - Confusion Matrix")
plt.show()

new_customer = pd.DataFrame({"income": [35000],"credit_score": [610],"loan_amount": [300000],
    "employment_status": [encoder.transform(["Self-employed"])[0]],
    "previous_payment_history": [2]})

new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)
probability = model.predict_proba(new_customer_scaled)

print("\n----- NEW CUSTOMER PREDICTION -----")

if prediction[0] == 1:
    print("Prediction: Customer is likely to DEFAULT")
else:
    print("Prediction: Customer is NOT likely to DEFAULT")

print("Default Probability:",round(probability[0][1] * 100, 2),"%")

print("No Default Probability:",round(probability[0][0] * 100, 2),"%")