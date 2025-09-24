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

# ---------------- Versión interactiva ----------------
col1, col2 = st.columns(2)
with col1:
    hist_btn = st.button("Mostrar histograma (odometer)")
with col2:
    scatter_btn = st.button("Mostrar dispersión (price vs odometer)")

if hist_btn:
    st.subheader("Histograma (odometer)")
    fig = px.histogram(df, x="odometer", nbins=40, title="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)

if scatter_btn:
    st.subheader("Dispersión (price vs odometer)")
    fig2 = px.scatter(df, x="odometer", y="price", title="Precio vs Kilometraje")
    st.plotly_chart(fig2, use_container_width=True)