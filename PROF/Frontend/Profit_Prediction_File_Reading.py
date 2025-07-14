import streamlit as st
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import time
from tqdm import tqdm
import re
import seaborn as sns
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

model = pickle.load(open('../Model/ML_Model_Advertising_01.pkl', 'rb'))
st.title("Company Profit Prediction based on Advertising investments")

#------------Cutomer Data File Uploading-------------------------------------------------
uploaded_file = st.file_uploader('Choose your "Customer Advertising Data" File')
time.sleep(25)
#------------Customer Advertising Data File Uploading is completed-----------------------

#------------Customer Data File Reading starts-------------------------------------------
progress_text = "Customer Advertising Data File reading is in progress. Please wait. ⏳"
my_progress_bar = st.progress(0)
status_text = st.empty()

for percent_complete in range(0, 101):
    time.sleep(0.02)
    my_progress_bar.progress(percent_complete)
    status_text.text(f"{progress_text} {percent_complete}%")

status_text.text("Customer Advertising Data file reading is completed! ⌛")
my_progress_bar.empty()

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.text('Input Customer file Data')
  st.write(df)
#<---------------Customer Data file reading End----------------------------------------->
time.sleep(15)

#<-------Customer Data Preprocessing Starts--------------------------------------------->
#st.text('Entered "Customer Data Preprocessing" Code Block...')
st.text('Customer Data Preprocessing starts...')
#-------------------------------------------------------
progress_text = "Data Preprocessing is in progress. Please wait. ⏳"
my_progress_bar = st.progress(0)
status_text = st.empty()

for percent_complete in range(0, 101):
    time.sleep(0.02)
    my_progress_bar.progress(percent_complete)
    status_text.text(f"{progress_text} {percent_complete}%")

status_text.text("Data Preprocessing is completed! ⌛")
my_progress_bar.empty()
#<--------Customer Data Preprocessing ends---------------------------------------------->

#<-------Customer Data Prediction Starts-------------------------------->
time.sleep(5)
st.text('Customer Data based Profit Prediction process starts...')
time.sleep(5)
#st.text('Please click on "Predict" button below to execute the Prediction Task...')
#if st.button("Predict"):
prediction = model.predict(df)

df["Pred_Value"]=prediction
df1=df
st.text('Customer Data based Profit Prediction process ends...')
st.text('Customer Data with Predicted Values')
st.write(df1)
time.sleep(5)
#st.text('Customer Data based Profit Prediction process ends...')
#<-------Customer Data Prediction Ends-------------------------------->
time.sleep(5)

#<-------Customer Data with Prediction Values file Downloading Starts------>
st.text('Customer Data file with Predicted values downloading Process starts...')
time.sleep(5)
#st.text('Please click on "Download data as CSV" button below to download the CSV file')

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv1 = convert_df(df)
df1.to_csv("D:/Muthu-Office/Indi-ML-Projects-2023/03-Ananconda-Projects/12_Profit_Prediction/Frontend/Customer_Data_with_Profit_Predicted_Values.csv", index = False)
#st.download_button(
#    label="Download data as CSV",
#    data=csv,
#    file_name='Tweets_with_Predicted_Sentiment_Values.csv',
#    mime='text/csv',
#)
#-------------------------------------------------------
progress_text = "Downloading of CSV file is in progress. Please wait. ⏳"
my_progress_bar = st.progress(0)
status_text = st.empty()

for percent_complete in range(0, 101):
    time.sleep(0.02)
    my_progress_bar.progress(percent_complete)
    status_text.text(f"{progress_text} {percent_complete}%")

status_text.text("File has been downloaded! ⌛")
my_progress_bar.empty()
#--------------------------------------------------------
#time.sleep(5)
#st.text('Customer Data file with Predicted values downloading Process ends...')
#<-------Customer Data with Prediction Values file Downloading End------>


time.sleep(5)
#st.text('Downloading of the .csv file has been completed')
st.text('Downloaded file is in your "Frontend" folder')
st.title('Execution of "Profit Prediction Application" is completed')
#st.text('Customer Data file with Predicted values downloading Process ends...')
#<-------Customer Data with Prediction Values file Downloading End------>



