import streamlit as st
import math

# TRIÁNGULO 
st.title("Calcular el área y permímetro de figuras")
figura = st.selectbox("Selecciona la figura", ["Triángulo"])

if figura == "Triángulo":
    st.subheader("Parámetros del triángulo")
    base = st.number_input("Base (b)", min_value=0.0, format="%.2f")
    altura = st.number_input("Altura (h)", min_value=0.0, format="%.2f")
    lado_a = st.number_input("Lado a", min_value=0.0, format="%.2f")
    lado_b = st.number_input("Lado b", min_value=0.0, format="%.2f")
    lado_c = st.number_input("Lado c", min_value=0.0, format="%.2f")
        area = 0.5 * base * altura
        perimetro = lado_a + lado_b + lado_c

        st.metric("Área", f"{area:.2f}")
        st.metric("Perímetro", f"{perimetro:.2f}")
        st.success("Resultados")
