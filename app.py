import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

# Read the CSV file
df = pd.read_csv('vehicles_us.csv')

# Ensure numerical columns are correctly typed
df['price'] = df['price'].fillna(0).astype(np.float64)
df['days_listed'] = df['days_listed'].fillna(0).astype(np.float64)

# Print data types for verification
print(df.dtypes)

# Streamlit dashboard components
st.header("Car Sales Dashboard")

# Plotly Express for visualizations
fig = px.histogram(df, x="price")
st.plotly_chart(fig)

fig = px.scatter(df, x="price", y="odometer")
st.plotly_chart(fig)

# Checkbox to display raw data
if st.checkbox("Show Raw Data"):
    st.dataframe(df)