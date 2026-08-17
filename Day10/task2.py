# Household Electricity Consumption Prediction

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Create sample dataset
data = {
    "Temperature": [22, 24, 26, 28, 30, 32, 25, 27, 29, 31,
                    23, 26, 28, 30, 33, 21, 24, 27, 29, 32],

    "Appliances": [2, 3, 3, 4, 5, 6, 3, 4, 5, 6,
                   2, 3, 4, 5, 7, 2, 3, 4, 5, 6],

    "TimeOfDay": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                  16, 17, 18, 19, 20, 21, 22, 23, 5, 4],

    "PreviousUsage": [1.2, 1.4, 1.6, 1.8, 2.2, 2.5, 2.0, 2.3,
                      2.6, 2.8, 2.5, 3.0, 3.2, 3.5, 4.0, 3.8,
                      3.5, 3.0, 1.5, 1.3],

    "CurrentUsage": [1.5, 1.7, 1.9, 2.2, 2.7, 3.1, 2.5, 2.8,
                     3.1, 3.4, 3.0, 3.6, 3.9, 4.3, 4.9, 4.6,
                     4.2, 3.7, 1.8, 1.6]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Input features
X = df[["Temperature", "Appliances", "TimeOfDay", "PreviousUsage"]]

# Target
y = df["CurrentUsage"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Display predictions
print("\nActual vs Predicted:")
for actual, predicted in zip(y_test, y_pred):
    print("Actual:", round(actual, 2),
          "Predicted:", round(predicted, 2))

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

# Predict electricity consumption for a new situation
new_data = pd.DataFrame(
    [[45, 7, 20, 5.0]],
    columns=["Temperature", "Appliances", "TimeOfDay", "PreviousUsage"])

prediction = model.predict(new_data)

print("\nPredicted Electricity Consumption:",
      round(prediction[0], 2), "kWh")