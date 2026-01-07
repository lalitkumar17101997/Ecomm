import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

def main():
    st.title("This is my streamlit app for ecomm business that i have")
    st.sidebar.title("Upload your file")

    uploaded_file =  uploaded_file = st.sidebar.file_uploader("upload your file here",type=['csv','xlsx'])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else :
             
                data = pd.read_excel(uploaded_file)
            st.sidebar.success("File uploaded successfully!")

            st.subheader("Data overview")
            st.dataframe(data.head())
         
            st.subheader("Basic information of the data")
            st.write("Shape of the data:", data.shape)
            st.write("Columns in the data:", data.columns.tolist()) 
            st.write("Missing Value", data.isnull().sum())
            
            st.subheader("I will Show you stats of the data")
            st.write(data.describe())
        except Exception as e:
            print("Error:", e)
    else:   
        pass
if __name__ == "__main__":
    main()
  