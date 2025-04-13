# DataGenie_Hackathon  
**Time Series Forecasting with Automated Model Selection**

## Introduction

The world is generating an immense amount of data every day, and one of the most common types is time series data. Time series data consists of observations taken sequentially over time, and it is used in various fields like finance, weather forecasting, and manufacturing. However, forecasting and detecting anomalies in such data is a challenging task that requires specialized models.

The goal of this project is to develop an intelligent system for time series forecasting and anomaly detection that works efficiently and at scale.

👉 **Note:** For this project, I have used the sample time series dataset provided in the problem statement.

For more details, you can refer to the [Problem Statement](https://docs.google.com/document/d/1EOQDyFRSjp5oggR703sOq3dYMzdSF0NN65wACxBxNBU/edit?tab=t.0#heading=h.yywnxrulcrce).

---

## Goals & Checkpoints

### ✅ Checkpoint 1: Automated Model Selection
Develop a classifier that predicts the best forecasting model for a given time series based on the dataset's characteristics.  
The best model is identified as the one achieving the lowest Mean Absolute Percentage Error (MAPE).

### ✅ Checkpoint 2: Forecast Generation and Evaluation
Use the selected model to generate forecasts for the test data and evaluate its performance using the MAPE metric.

### ✅ Checkpoint 3: REST API Implementation
Build a REST API to allow users to:
- Upload time series data
- Get model predictions
- View the selected model and its corresponding MAPE score

### ✅ Checkpoint 4 (Bonus): Simple UI & Deployment
Deploy a basic user interface (UI) that enables users to:
- Upload time series data
- Visualize the forecast and anomaly detection results using interactive plots powered by Plotly.

---

## ✅ Checkpoint 1: Automated Model Selection

### Step 1: Data Loading and Preprocessing
- Loaded the sample time series dataset provided in the problem statement.
- Performed data cleaning to handle missing values and inconsistencies.
- Converted the cleaned dataset into a Python list format for ease of processing in the next steps.

### Step 2: Exploratory Data Analysis (EDA)
- Conducted EDA to understand the patterns, trends, and anomalies in the dataset.
- Visualized the data to identify seasonality, trends, and potential outliers.

### Step 3: Feature Extraction
Extracted essential features from the time series to help the classifier understand data characteristics:
- **Stationarity (ADF Test p-value):** Determines if the time series has a constant mean and variance over time.
- **Trend Strength (Rolling Mean Standard Deviation):** Measures how strong the trend is in the series.
- **Seasonality:** Quantifies repetitive patterns at regular intervals.
- **Skewness & Kurtosis:** Helps understand the distribution and shape of the data.
- **Anomaly Count:** Counts data points that deviate significantly from the expected range.

➡️ All extracted features were saved into a CSV file for future steps.

### Step 4: Time Series Model Training and Evaluation

Trained multiple time series models to forecast values and compute MAPE (Mean Absolute Percentage Error):
- **Naive Forecast Model:** A simple baseline that uses the last known value as the forecast.
- **Holt-Winters (Exponential Smoothing):** Captures level, trend, and seasonality components.
- **ARIMA Model:** Advanced statistical model capturing autocorrelations in time series.

For each model:
- Generated forecasts.
- Calculated the MAPE value.
- Selected the best-performing model based on the lowest MAPE score.
- Printed MAPE values for verification.

### Step 5: Classifier Model Training

After identifying the best model for each time series, trained multiple classification models to predict the best forecasting model:
- **Random Forest**
- **XGBoost**
- **Logistic Regression**
- **LightGBM**
- **CatBoost**

📊 Evaluation metrics used:
- Accuracy
- F1-score
- Confusion Matrix
- Cross-validation Mean Accuracy

🔍 After comparing classifiers, **XGBoost** emerged as the best-performing classifier based on evaluation metrics.

✔️ Saved the trained XGBoost classifier as a `.pkl` file for use in the next checkpoints.

