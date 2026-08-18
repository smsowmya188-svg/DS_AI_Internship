import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, classification_report


# ==========================================
# 1. LOAD DATASET
# ==========================================

data = pd.read_csv("flight_data.csv")

print("Dataset loaded successfully!")
print(data.head())


# ==========================================
# 2. ENCODE CATEGORICAL FEATURES
# ==========================================

airline_encoder = LabelEncoder()
origin_encoder = LabelEncoder()
destination_encoder = LabelEncoder()
weather_encoder = LabelEncoder()

data["airline"] = airline_encoder.fit_transform(data["airline"])
data["origin"] = origin_encoder.fit_transform(data["origin"])
data["destination"] = destination_encoder.fit_transform(data["destination"])
data["weather"] = weather_encoder.fit_transform(data["weather"])


# ==========================================
# 3. FEATURES AND TARGET
# ==========================================

X = data[
    [
        "airline",
        "origin",
        "destination",
        "distance",
        "departure_hour",
        "weather",
        "previous_delay"
    ]
]

y = data["delay"]


# ==========================================
# 4. TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ==========================================
# 5. CLASSIFICATION MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# ==========================================
# 6. MODEL EVALUATION
# ==========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nClassification Accuracy:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ==========================================
# 7. SAVE CLASSIFICATION MODEL
# ==========================================

joblib.dump(model, "models/classification_model.pkl")


# ==========================================
# 8. SAVE ENCODERS
# ==========================================

encoders = {
    "airline": airline_encoder,
    "origin": origin_encoder,
    "destination": destination_encoder,
    "weather": weather_encoder
}

joblib.dump(encoders, "models/encoders.pkl")


# ==========================================
# 9. CLUSTERING
# ==========================================

cluster_features = data[
    [
        "distance",
        "departure_hour",
        "previous_delay"
    ]
]


# Scale data
scaler = StandardScaler()

scaled_data = scaler.fit_transform(cluster_features)


# ==========================================
# 10. K-MEANS CLUSTERING
# ==========================================

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

kmeans.fit(scaled_data)


# ==========================================
# 11. SAVE CLUSTERING MODEL
# ==========================================

joblib.dump(kmeans, "models/clustering_model.pkl")

joblib.dump(scaler, "models/scaler.pkl")


print("\nModels trained successfully!")

print("\nFiles created:")
print("classification_model.pkl")
print("clustering_model.pkl")
print("scaler.pkl")
print("encoders.pkl")