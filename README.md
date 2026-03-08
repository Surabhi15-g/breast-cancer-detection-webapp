# Breast Cancer Detection Web App

A Machine Learning web application that predicts whether a tumor is **Benign** or **Malignant** using Logistic Regression.
The system also visualizes the prediction using **PCA (Principal Component Analysis)** on a 2D graph.

The web application is built using the **Flask** framework and provides an interactive interface for users to input tumor feature values and view predictions with visualization.

---

## 🚀 Features

* Predicts **Benign or Malignant breast cancer**
* Uses **Logistic Regression Machine Learning Model**
* PCA visualization of prediction on a 2D graph
* Interactive web interface
* Clear input option for new predictions
* Graph shows dataset distribution and predicted sample point

---

## 🧠 Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* HTML
* CSS

---

## 📊 Machine Learning Concepts

The project uses:

* **Logistic Regression** for classification
* **Principal Component Analysis (PCA)** for 2D visualization of the dataset

The PCA plot shows:

* **Yellow points** → Benign tumors
* **Purple points** → Malignant tumors
* **Red point** → User prediction

---

## 📂 Project Structure

```
breast-cancer-detection/
│
├── app.py              # Flask application
├── model.py            # Machine learning model and PCA logic
│
├── templates/
│   └── index.html      # Frontend UI
│
├── static/
│   └── style.css       # Styling files
│
├── __pycache__/        # Python cache
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository

```
git clone https://github.com/your-username/breast-cancer-detection-webapp.git
```

2. Navigate to the project folder

```
cd breast-cancer-detection-webapp
```

3. Install required libraries

```
pip install flask scikit-learn pandas numpy matplotlib
```

---

## ▶️ Running the Application

Run the Flask server:

```
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🖥️ How It Works

1. User enters tumor feature values.
2. The machine learning model processes the input.
3. Logistic Regression predicts whether the tumor is benign or malignant.
4. The PCA graph visualizes where the input lies compared to the dataset.

---

## 📈 Dataset

This project uses the **Breast Cancer Wisconsin Dataset** from Scikit-learn.

---

## 📌 Future Improvements

* Deploy the application online
* Add model accuracy metrics
* Improve UI design
* Add more ML models for comparison

---

## 👨‍💻 Author

Developed as a Machine Learning web application project using Flask and Scikit-learn.
