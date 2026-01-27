# 🧑‍💼 Employee Attrition Prediction System

A Machine Learning powered web application that predicts whether an employee is likely to leave the company. This system helps HR teams take proactive, data-driven decisions to reduce employee turnover.

The model is deployed using **Flask** and provides an interactive web interface for real-time predictions and visualization.

---

## 🚀 Project Overview

Employee attrition is a major challenge for organizations. This project uses historical HR data and machine learning models to:

- Predict employee attrition
- Provide instant predictions through a web interface
- Visualize employee data using charts
- Assist HR in early intervention and retention planning

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Backend | Flask (Python) |
| Frontend | HTML, CSS, JavaScript |
| Machine Learning | Scikit-learn (Logistic Regression / Random Forest) |
| Data Handling | Pandas, NumPy |
| Visualization | Chart.js |
| Model Serialization | Joblib |

---

## 📊 Dataset Used

IBM HR Analytics Employee Attrition Dataset

Contains employee information like:

- Age, Department, Job Role
- Salary, Experience, Work Environment
- Job Satisfaction, Overtime, etc.
- Attrition status (Yes/No)

---

## 🧠 Machine Learning Workflow

1. Data Cleaning & Preprocessing
2. Encoding categorical features using `LabelEncoder`
3. Feature selection and splitting into train/test
4. Model training using Logistic Regression / Random Forest
5. Model evaluation using accuracy score
6. Model saved using Joblib
7. Integrated with Flask for real-time prediction

---

## 💻 Features

- Employee data input form
- Real-time attrition prediction
- Clean and responsive UI
- Data visualization using Chart.js
- Easy to deploy locally

---

## 📁 Project Structure

```
Employee-Attrition-Prediction/
│
├── dataset/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── static/
│   ├── style.css
│   └── chart.js
│
├── templates/
│   └── index.html
│
├── model/
│   └── attrition_model.pkl
│
├── app.py
├── train_model.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/employee-attrition-prediction.git
cd employee-attrition-prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train the Model

```bash
python train_model.py
```

### 4️⃣ Run the Flask App

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🧪 Sample Input for Testing

| Feature | Value |
|--------|------|
| Age | 35 |
| Department | Sales |
| JobRole | Sales Executive |
| MonthlyIncome | 5000 |
| OverTime | Yes |
| JobSatisfaction | 2 |

Prediction output: **Attrition: Yes/No**

---

## 📈 Visualization

The dashboard uses **Chart.js** to show:

- Distribution of attrition
- Employee demographics
- Department-wise analysis

---

## 🎯 Use Case

This system can be used by:

- HR teams for retention planning
- Managers for performance monitoring
- Organizations for workforce analytics

---

## 🧩 Future Improvements

- Deploy on cloud (Render / AWS / Heroku)
- Add more advanced ML models (XGBoost, Neural Networks)
- Add authentication for HR login
- Store employee records in a database
- Improve UI with React or Flutter frontend

---

## 👨‍💻 Author

**Devang Garg**  
Machine Learning & Web Development Enthusiast

---
