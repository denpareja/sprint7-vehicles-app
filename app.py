import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("vehicles_us.csv")

st.title("🚗 Vehicle Dataset Explorer")

# Mostrar primeras filas
st.subheader("Vista previa de los datos")
st.write(df.head())

# Histograma de precios
st.subheader("Distribución de precios")
fig = px.histogram(df, x="price", nbins=50, title="Distribución de precios de los vehículos")
st.plotly_chart(fig)

# Dispersión odometer vs price
st.subheader("Precio vs Kilometraje")
fig2 = px.scatter(df, x="odometer", y="price", title="Precio vs Kilometraje (odometer)")
st.plotly_chart(fig2)

