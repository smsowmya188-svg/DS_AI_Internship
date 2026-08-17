# Step 1: Import libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Step 2: Load the Iris dataset
iris = load_iris()

# Step 3: Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add the target column
df["Species"] = iris.target

# Step 4: Display the dataset
print("Dataset:")
print(df.head())

# Step 5: Identify features and label

# Features
X = df[iris.feature_names]

# Label
y = df["Species"]

print("\nFeatures:")
print(X.head())

print("\nLabel:")
print(y.head())

# Step 6: Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 7: Create the classification model
model = DecisionTreeClassifier(random_state=42)

# Step 8: Train the model
model.fit(X_train, y_train)

# Step 9: Make predictions
y_pred = model.predict(X_test)

# Step 10: Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nActual values:")
print(y_test.values)

print("\nPredicted values:")
print(y_pred)

print("\nAccuracy:", accuracy)