import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv('vehicles_us.csv')

df['price'] = df['price'].astype(float)
df['days_listed'] = df['days_listed'].astype(float)
df['price'] = df['price'].fillna(0).astype(int)
df['days_listed'] = df['days_listed'].fillna(0).astype(int)
   
   
print(df.dtypes)
   

# creating a Header
st.header("Car Sales Dashboard")

# creating a histogram 
fig = px.histogram(df, x="price")
st.plotly_chart(fig)

# creating a scatterplot
fig = px.scatter(df, x="price", y="odometer")
st.plotly_chart(fig)

# creating a checkbox
   
if st.checkbox("Show Raw Data"):
    st.dataframe(df)
   



