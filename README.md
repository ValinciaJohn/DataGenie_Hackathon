# DataGenie_Hackathon  
**Time Series Forecasting with Automated Model Selection**

## Introduction

The world is generating an immense amount of data every day, and one of the most common types is time series data. Time series data consists of observations taken sequentially over time, and it is used in various fields like finance, weather forecasting, and manufacturing. However, forecasting and detecting anomalies in such data is a challenging task that requires specialized models.

The goal of this project is to develop an intelligent system for time series forecasting and anomaly detection that works efficiently and at scale.

 **Note:** For this project, I have used the sample time series dataset provided in the problem statement.

For more details, you can refer to the [Problem Statement](https://docs.google.com/document/d/1EOQDyFRSjp5oggR703sOq3dYMzdSF0NN65wACxBxNBU/edit?tab=t.0#heading=h.yywnxrulcrce).

---

## Goals & Checkpoints

###  Checkpoint 1: Automated Model Selection
Develop a classifier that predicts the best forecasting model for a given time series based on the dataset's characteristics.  
The best model is identified as the one achieving the lowest Mean Absolute Percentage Error (MAPE).

###  Checkpoint 2: Forecast Generation and Evaluation
Use the selected model to generate forecasts for the test data and evaluate its performance using the MAPE metric.

### Checkpoint 3: REST API Implementation
Build a REST API to allow users to:
- Upload time series data
- Get model predictions
- View the selected model and its corresponding MAPE score

###  Checkpoint 4 (Bonus): Simple UI & Deployment
Deploy a basic user interface (UI) that enables users to:
- Upload time series data
- Visualize the forecast and anomaly detection results using interactive plots powered by Plotly.

---

##  Checkpoint 1: Automated Model Selection

![image](https://github.com/user-attachments/assets/a4864c3c-a18a-4a12-8a92-0b4b616fbf3d)


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

➡ All extracted features were saved into a CSV file for future steps.

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

 Evaluation metrics used:
- Accuracy
- F1-score
- Confusion Matrix
- Cross-validation Mean Accuracy

 After comparing classifiers, **XGBoost** emerged as the best-performing classifier based on evaluation metrics.

✔ Saved the trained XGBoost classifier as a `.pkl` file for use in the next checkpoints.

## Checkpoint 2: Generate Predictions and Evaluate Performance

![image](https://github.com/user-attachments/assets/f40204c2-b64c-42e2-a3bf-bc853350d417)


### Step 1: Load Classifier Model and Dataset
- Loaded the pre-trained **XGBoost classifier** saved from Checkpoint 1.
- Imported the extracted features CSV file to use for predicting the best forecasting model for new time series data.

### Step 2: Predict the Best Time Series Model
- Used the XGBoost classifier to predict the most suitable time series forecasting model for each series in the dataset.
- The model selection is based on the characteristics (features) extracted in Checkpoint 1.
- Printed the selected models for verification.

### Step 3: Train-Test Split
- For each time series, split the data into training and testing sets to validate forecasting performance.
- Training data was used to fit the selected model, and testing data was used to evaluate predictions.

### Step 4: Generate Forecasts
- Applied the selected forecasting model (Naive, Holt-Winters, or ARIMA) to the training data.
- Generated future predictions on the test data.

### Step 5: Evaluate Forecasting Performance
- Calculated the **Mean Absolute Percentage Error (MAPE)** between the predicted and actual values.
- MAPE helps evaluate the accuracy of the forecast by measuring the average absolute percentage difference.

### Step 6: Anomaly Detection
- Compared the forecasted values with the actual observations.
- Identified anomalies as points where the deviation between the actual and forecasted values exceeded a threshold.
- Marked anomalies for potential further analysis.

### Step 7: Prepare Output
- Compiled the following results:
  - Selected forecasting model
  - Forecasted values
  - MAPE score
  - Anomaly points

✔ Saved the results for the next checkpoint where they will be served via an API.

##  Checkpoint 3: REST API Implementation

### Step 1: API Design
- Developed a simple **REST API** using **FastAPI** to serve the predictions for uploaded time series data.
- The API allows users to:
  - Upload a CSV file containing time series data.
  - Receive the predicted best model for the data.
  - Get the forecasted values along with the MAPE score for evaluation.
  - View the anomalies detected in the data.

### Step 2: Implementing the API Endpoints
The API exposes the following endpoints:
- **POST `/predict`**:
  - **Input**: CSV file with time series data.
  - **Output**: JSON response containing:
    - Forecasting model used.
    - Predictions.
    - MAPE score.
    - Anomalies detected in the data.

### Step 3: Testing with Postman
- Used **Postman** for testing the API:
  - Sent **POST requests** to the `/predict` endpoint by uploading CSV files.
  - Received JSON responses with the forecast results and anomaly detections.

### Step 4: API Response Example
- The response from the API includes the **best model**, **predictions**, and **MAPE value**:
![image](https://github.com/user-attachments/assets/be4ff56e-9a56-4c36-a514-651edef8c1a6)

##  Checkpoint 4: Simple UI & Deployment

### Step 1: UI Design
- Developed a **basic user interface (UI)** using **Streamlit** to allow users to easily interact with the time series data and forecast models.
- The UI enables users to:
  - **Upload time series data**: Users can upload a CSV file containing their time series data.
  - **View forecasted values and anomalies**: The interface displays the predicted values from the best forecasting model and highlights any anomalies detected in the dataset.
  - **Interact with the forecast data via Plotly graph**: The interface includes an interactive **Plotly** graph that allows users to visualize the forecasted values along with the actual values, as well as anomalies.
 ![image](https://github.com/user-attachments/assets/6340dfa7-0d6e-4a63-b925-692f8d43f275)

## Technologies used :

- Backend : FastAPI
- Frotend : Streamlit

## Conclusion

This provides an end-to-end solution for time series forecasting with automated model selection, anomaly detection, and a user-friendly interface. It allows businesses to efficiently choose the best forecasting model for their data and visualize the results interactively. The implementation covers:
- Automated model selection and prediction generation (Checkpoint 1 and 2).
- A REST API for real-time model prediction requests (Checkpoint 3).
- A simple UI to interact with time series data and view forecast results (Checkpoint 4).

## My approach:
The full documentation of my work and the demo video is here in this [link](https://www.loom.com/share/37cfc4f2292640feafedc6786527caa2?sid=6d936079-477e-42f9-9bb7-26948819f9bb).


