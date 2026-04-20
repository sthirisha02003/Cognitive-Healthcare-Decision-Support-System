# Cognitive Healthcare Decision Support System

## 📌 Overview
This project builds an intelligent healthcare decision-support system to predict diabetes risk using OCR, Machine Learning, and Fuzzy Logic.

The system extracts medical data from report images and provides accurate, explainable predictions.

---

## 🧠 Key Features
- OCR-based medical data extraction (Tesseract + OpenCV)
- Data preprocessing & feature engineering
- Machine Learning models:
  - Random Forest
  - SVM
  - Neural Networks
- Fuzzy logic for explainable reasoning
- SHAP for model interpretability
- Full-stack web application (React + Flask/FastAPI)

---

## 🏗️ Architecture
1. Image Input (Medical Reports)
2. Image Processing (OpenCV)
3. Text Extraction (OCR - Tesseract)
4. Feature Engineering (Regex + NLP)
5. ML Models (RF, SVM, NN)
6. Fuzzy Logic Layer
7. Explainability (SHAP)
8. Web Dashboard Output

---

## 📊 Dataset
- 500+ labeled medical report images
- Classes:
  - Normal
  - Pre-diabetic
  - Type 1 Diabetes
  - Type 2 Diabetes

---

## ⚙️ Technologies Used
- Python
- OpenCV
- Tesseract OCR
- Pandas, NumPy
- Scikit-learn
- TensorFlow
- SHAP
- React.js
- Flask / FastAPI

---

## 📈 Model Evaluation
- Accuracy, Precision, Recall, F1-score
- ROC-AUC
- Confusion Matrix
- Cross-validation

---

## 💡 Results
- Successfully detected Type 2 Diabetes with ~90% confidence
- Identified key risk factors:
  - High HbA1c
  - High glucose levels
  - Insulin resistance
- Provided explainable insights using SHAP

---

## 🚀 How to Run
1. Upload medical report image
2. Run OCR extraction
3. Process features
4. Run ML models
5. View prediction + explanation

---

## 📌 Future Scope
- Real-time hospital integration
- Advanced deep learning models
- Mobile application deployment
