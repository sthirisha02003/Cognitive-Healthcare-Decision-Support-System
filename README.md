# Cognitive Healthcare Decision Support System

## 📌 Overview

The Cognitive Healthcare Decision Support System is an AI-powered application developed to predict diabetes risk from medical report images using OCR, Machine Learning, and rule-based fuzzy logic.

The system automatically extracts medical values such as glucose and BMI from uploaded reports and provides intelligent risk predictions with confidence scores.

---

## 🧠 Key Features

* OCR-based medical report text extraction using Tesseract OCR
* Automatic extraction of healthcare parameters
* Diabetes prediction using Machine Learning
* Risk classification using fuzzy logic
* REST API backend using FastAPI
* Frontend integration support
* Explainable healthcare prediction workflow

---

## 🏗️ System Architecture

1. Medical Report Image Upload
2. OCR Text Extraction
3. Data Preprocessing
4. Feature Extraction
5. Machine Learning Prediction
6. Fuzzy Logic Risk Analysis
7. Prediction Dashboard Output

---

## ⚙️ Technologies Used

* Python
* FastAPI
* Tesseract OCR
* NumPy
* Scikit-learn
* Joblib
* PIL (Python Imaging Library)
* Regex
* HTML/CSS/JavaScript or React.js

---

## 🤖 Machine Learning

The system uses Logistic Regression for diabetes risk prediction based on extracted medical features such as:

* Glucose Level
* BMI

Prediction output:

* Diabetic / Non-Diabetic
* Confidence Score

---

## 🧩 Fuzzy Logic Layer

A rule-based fuzzy logic module is used to classify risk levels:

* LOW Risk
* MEDIUM Risk
* HIGH Risk

Example:

* High glucose + high BMI → HIGH risk

---

## 💡 Results

* Successfully extracted medical values from report images
* Generated diabetes risk predictions with confidence scores
* Combined OCR + ML + fuzzy reasoning in a single workflow
* Built a lightweight healthcare AI backend system

---

## 🚀 How to Run

### Install Dependencies

```bash
pip install fastapi uvicorn pytesseract pillow scikit-learn joblib python-multipart
```

### Install OCR Engine

```bash
apt-get install tesseract-ocr -y
```

### Run Backend

```bash
uvicorn main:app --reload
```

### Open API Docs

```arduino
http://127.0.0.1:8000/docs
```

---

## 📌 Future Scope

* Integration with real hospital datasets
* Advanced Deep Learning models
* SHAP-based explainability
* Mobile healthcare application
* Real-time cloud deployment

## 📌 Future Scope
- Real-time hospital integration
- Advanced deep learning models
- Mobile application deployment
