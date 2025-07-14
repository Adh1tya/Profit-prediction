import streamlit as st
from PIL import Image
import pickle
import numpy as np

model = pickle.load(open('../Model/ML_Model_Advertising_01.pkl', 'rb'))

def run():
    img1 = Image.open('bank.png')
    img1 = img1.resize((156,145))
    st.image(img1,use_column_width=False)
    st.title("Company Profit Prediction based on Advertising investments")

    ## House Area in sqft
    tv = st.number_input("Investment amount(INR) in TV Advertising in Crores",value=0.0)    
    
    ## Number of Bedrooms required
    radio = st.number_input("Investment amount(INR) in Radio Advertising in Crores",value=0.0)  

    ## Number of Bathrooms required
    newspaper = st.number_input("Investment amount (INR) in Newspaper Advertisement in Crores",value=0.0)  

    ## Number of Bathrooms required
    #balcony = st.number_input("Number of Balconies required",value=0) 

    ## For Location area of the House in Bangalore
    #loc_display = ('Bommanahalli','Electronics City','Indira Nagar','Vijayanagar', 'Whitefield')
    #loc_options = list(range(len(loc_display)))
    #location = st.selectbox("location",loc_options, format_func=lambda x: loc_display[x])

    if st.button("Submit"):
        
        features = [[tv, radio, newspaper]]
        print(features)
        
        Profit = model.predict(features)
        st.subheader('Predicted Profit of the Company in Crores :')
        st.subheader('INR'+' '+str(np.round(Profit[0])))

run()