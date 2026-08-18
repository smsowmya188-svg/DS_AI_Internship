from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (confusion_matrix,accuracy_score,precision_score,
    recall_score,f1_score,ConfusionMatrixDisplay)
import matplotlib.pyplot as plt

X = [[2, 60],[3, 65],[4, 70],[5, 75],[6, 80],[7, 85],[8, 90],
    [9, 95],[1, 50],[2, 55],[3, 60],[4, 65],[6, 75],[7, 80],
    [8, 85],[9, 90],[2, 50],[3, 55],[5, 70],[7, 75]]

y = [0, 0, 0, 1, 1,
     1, 1, 1, 0, 0,
     0, 0, 1, 1, 1,
     1, 0, 0, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42,stratify=y)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Actual Values:   ", y_test)
print("Predicted Values:", y_pred)

cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

precision = precision_score(y_test, y_pred)
print("Precision:", precision)

recall = recall_score(y_test, y_pred)
print("Recall:", recall)

f1 = f1_score(y_test, y_pred)
print("F1 Score:", f1)

disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["Fail", "Pass"])
disp.plot()
plt.title("Student Pass/Fail Prediction")
plt.show()