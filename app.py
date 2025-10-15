import streamlit as st
import math
import matplotlib.pyplot as plt

st.title("Calcular el área y permímetro de figuras")
st.sidebar.write("Deyra Renata Herrera Juárez 385845")
figura = st.selectbox("Selecciona la figura", ["Triángulo", "Círculo", "Rectángulo", "Cuadrado"])

#TRIÁNGULO

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
color = st.color_picker("Selecciona el color del borde", "#00f900")
fig, ax = plt.subplots()
if figura == "Triángulo":
    x = [-base/2, base/2, 0]
    y = [0, 0, altura]
    triangle = plt.Polygon(list(zip(x, y)), edgecolor=color, fill=False)
    ax.add_artist(triangle)
    ax.set_xlim(-base, base)
    ax.set_ylim(0, altura + 2)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

# CÍRCULO

if figura == "Círculo":
    st.subheader("Parámetros del círculo")
    radio = st.slider("Radio del círculo", 0.0, 100.0, 5.0)
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("Resultados")
color = st.color_picker("Selecciona el color del borde", "#00f900")
fig, ax = plt.subplots()
circle = plt.Circle((0, 0), radio, color=color, fill=False)
ax.add_artist(circle)
ax.set_xlim(-radio - 1, radio + 1)
ax.set_ylim(-radio - 1, radio + 1)


# RECTÁNGULO

if figura == "Rectángulo":
    st.subheader("Parámetros del círculo")
    base = st.slider("Selecciona la magnitud de la base", 0.0, 100.0, 5.0)
    altura = st.slider("Selecciona la magnitud de la altura", 0.0, 100.0, 5.0)
    area = base * altura
    perimetro = 2 * (base + altura)
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("Resultados")

# CUADRADO

if figura == "Cuadrado":
    st.subheader("Parámetros del cuadrado")
    lado = st.slider("Selecciona la magnitud de el lado", 0.0, 100.0, 5.0)
    area = lado**2
    perimetro = 4 * lado
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("Resultados") 
