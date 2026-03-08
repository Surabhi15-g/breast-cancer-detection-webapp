import numpy as np
import os
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
cancer = load_breast_cancer()

# Use only 4 features
X = cancer.data[:, [0,1,2,3]]  
y = cancer.target

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)


def predict_cancer(features):

    features = np.array(features).reshape(1, -1)

    scaled = scaler.transform(features)

    prediction = model.predict(scaled)

    if prediction[0] == 0:
        return "Malignant (Cancer)"
    else:
        return "Benign (No Cancer)"


def get_accuracy():
    return round(accuracy*100,2)


def generate_pca_plot(user_features):

    plt.figure(figsize=(6,4))

    # Plot dataset
    plt.scatter(
        X_pca[:,0],
        X_pca[:,1],
        c=y,
        cmap='viridis'
    )

    # Transform user point
    user_scaled = scaler.transform([user_features])
    user_pca = pca.transform(user_scaled)

    # Plot user point
    plt.scatter(
        user_pca[:,0],
        user_pca[:,1],
        color='red',
        s=200
    )

    plt.xlabel("First Principal Component")
    plt.ylabel("Second Principal Component")
    plt.title("PCA Visualization of Breast Cancer Dataset")

    if not os.path.exists("static"):
        os.makedirs("static")

    plt.savefig("static/pca_plot.png")
    plt.close()