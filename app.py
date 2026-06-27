import streamlit as st

st.title("Aplicación de Fundamentos Streamlit

st.sidebar.image("images.jpg")

st.sidebar.title("Parámetros")

monto = st.number_input("Ingrese el Monto de su Prestamo"
 
interes = st.number_input("Ingrese el interes")
 
tiempo_meses = st.number_input("Ingrese el tiempo en meses")
 
resultado = monto*interes*(tiempo_meses/12)    
 
st.write("El resultado es:" , resultado)
