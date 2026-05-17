# Wine Quality Prediction App

##  Project Overview

The **Wine Quality Prediction App** is a machine learning-based web application built using **Python** and **Streamlit**. The application predicts the quality of wine based on its chemical properties such as acidity, alcohol content, pH level, sulphates, and density.

Users can enter wine attributes through an interactive interface, and the trained machine learning model predicts the wine quality instantly.

# Features

* Interactive and user-friendly UI using Streamlit
* Real-time wine quality prediction
* Machine Learning model integration
* Data preprocessing using scaler
* Simple deployment-ready structure
* Beginner-friendly AI/ML project

# Technologies Used

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| Python           | Programming Language      |
| Streamlit        | Web Application Framework |
| NumPy            | Numerical Computation     |
| Joblib           | Model Saving & Loading    |
| Machine Learning | Prediction Model          |


#  Project Structure

```bash
Wine-Quality-Prediction/
│
├── app.py
├── wine_model.joblib
├── wine_model.pkl
├── scaler.joblib
├── README.md
└── requirements.txt
```

---

# How It Works

1. User enters wine chemical properties.
2. Input data is converted into a NumPy array.
3. Data is scaled using the saved scaler.
4. Machine Learning model predicts wine quality.
5. Predicted quality score is displayed on screen.

# 📊 Input Features

The model uses the following wine parameters:

* Fixed Acidity
* Volatile Acidity
* Citric Acid
* Residual Sugar
* Chlorides
* Free Sulfur Dioxide
* Total Sulfur Dioxide
* Density
* pH
* Sulphates
* Alcohol

# Installation & Setup

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/wine-quality-prediction.git
cd wine-quality-prediction
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Run the Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

Create a `requirements.txt` file with:

```txt
streamlit
numpy
joblib
scikit-learn
```

---

# Machine Learning Workflow

## Data Preprocessing

* Feature scaling using StandardScaler
* Input normalization before prediction

## Model Training

* Model trained using wine quality dataset
* Saved using Joblib/Pickle for deployment

## Prediction

* Real-time prediction using trained ML model

---

# Future Improvements

* Add graphical data visualization
* Add multiple ML model comparison
* Improve UI/UX design
* Deploy on Streamlit Cloud or Render
* Add dataset upload option
* Include prediction confidence score
* Add dark/light mode

---

# Deployment Platforms

You can deploy this project on:

* Streamlit Cloud
* Render
* Railway
* Hugging Face Spaces
* Heroku

---

#  Project Output

The application predicts wine quality based on user inputs and displays the predicted score instantly.

Example:

```bash
Predicted Wine Quality: 6.42
```

# ✅ Strengths of the Project

* Clean and simple implementation
* Proper use of ML model and scaler
* Beginner-friendly architecture
* Real-world dataset usage
* Easy to understand and deploy



---

# 📜 License

This project is open-source and free to use for educational purposes.
