import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import io

API_URL = 'http://127.0.0.1:8000/forecast'  

st.title('Time Series Forecasting App')

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    st.write("File Uploaded Successfully! Displaying the first few rows:")
    
    try:
        df = pd.read_csv(uploaded_file)
        
        st.write("Original Dataframe:")
        st.dataframe(df.head())

        if 'Unnamed: 0' in df.columns:
            df = df.drop(columns=['Unnamed: 0'])  
        if 'rolling_mean' in df.columns:
            df = df.drop(columns=['rolling_mean'])  
        
        df = df.rename(columns={'timestamp': 'timestamp', 'value': 'value'})

        if 'timestamp' not in df.columns or 'value' not in df.columns:
            st.error("The CSV file must contain 'timestamp' and 'value' columns.")
        else:
            st.write("Cleaned Dataframe:")
            st.dataframe(df.head())  

            csv_data = df.to_csv(index=False)
            file_data = io.StringIO(csv_data)

            files = {'file': (uploaded_file.name, file_data, 'text/csv')}
            
            response = requests.post(API_URL, files=files)

            if response.status_code == 200:
                data = response.json()

                st.write("Backend Response (JSON):")
                st.json(data)

                timestamps = [entry['timestamp'] for entry in data['results']]
                actual_values = [entry['point_value'] for entry in data['results']]
                predicted_values = [entry['predicted'] for entry in data['results']]

                fig = px.line(
                    x=timestamps, 
                    y=[actual_values, predicted_values], 
                    labels={'x': 'Timestamp', 'y': 'Values'},
                    title='Actual vs Predicted Time Series'
                )

                st.plotly_chart(fig)

                st.write(f"MAPE (Mean Absolute Percentage Error): {data['mape']}")
            else:
                st.write("Error in API response: ", response.json())

    except Exception as e:
        st.error(f"Error reading or processing the file: {str(e)}")
