# 🏦 Loan Eligibility Predictor using ML

This is a machine learning project where I built a classification model to predict whether a loan applicant is eligible for approval based on details like income, dependents, credit history, and more. The trained model is integrated into a Streamlit web app that takes user inputs and gives real-time predictions!

## 📌 Project Overview
- **Goal:** Predict loan eligibility based on applicant details.
- **Model:** Logistic Regression and Random Forest Classifier (using scikit-learn).
- **UI:** Streamlit web interface for real-time user input and prediction.
- **Deployment:** hosted using Streamlit.

## 🗂️ Project Files

| File                    | Description                                |
|-------------------------|--------------------------------------------|
| `app.py`                | Streamlit web app for loan prediction      |
| `loan_model.pkl`        | Trained Random Forest model (saved file)   |
| `loan_model.ipynb`      | Jupyter notebook for model training        |
| `requirements.txt`      | Required Python libraries                  |
| `README.md`             | Project documentation (this file)          |
| `output`                | Sample output screenshots                  |

## 📊 Model Details

- **Features used:**
  - Credit History
  - Education
  - Property Area
  - Applicant & Coapplicant Income
  - Loan Amount & Loan Term
  - Marital Status
  - Self Employed
  - Number of Dependents

- **Target variable:**
  - `Loan_Status`: Y (eligible) or N (not eligible)

- **Algorithms:**
  - Logistic Regression
  - Random Forest (selected for deployment)

## 🧪 Accuracy Achieved

| Metric              | Value       |
|---------------------|-------------|
| Training Accuracy   | ~81–84%     |
| Test Accuracy       | ~80–83%     |
| ROC AUC Score       | High (0.85+)|

## 🖼️ How the App Works

1. Run the app using:
   ```
   streamlit run app.py
   ```

2. A browser window will open with the app.

3. Enter applicant details like:
   - Income
   - Number of Dependents
   - Credit History
   - Property Area
   - Loan Amount, etc.

4. Click **"Predict"** to get result:
   - ✅ Eligible or ❌ Not Eligible



## 🛠 Requirements

Install all dependencies with:

```
pip install -r requirements.txt
```

### Required Libraries:
- streamlit  
- scikit-learn  
- pandas  
- joblib  
- numpy

## 📊 Dataset Used

- Dataset: [Loan Prediction Dataset](https://raw.githubusercontent.com/shrikant-temburwar/Loan-Prediction-Dataset/master/train.csv)
- Contains ~600 loan applications with features like:
  - Gender
  - Education
  - Credit History
  - Income & Loan Info
  - Property Area

## 🎯 Future Improvements

- Add input validation and field explanation in UI
- Extend to support batch CSV input


## 🙌 Acknowledgments

Part of **RISE Internship by Tamizhan Skills – July 2025 batch**  

