import streamlit as st
import matplotlib.pyplot as plt
import math

st.title("Calcular el área y permímetro de figuras")
st.sidebar.write("Deyra Renata Herrera Juárez Matrícula:38584 Grupo: 3L")

# Crear pestañas
tab1, tab2, tab3, tab4 = st.tabs(["Círculo", "Rectángulo", "Cuadrado", "Triángulo"])

# 🟢 CÍRCULO
with tab1:
    st.subheader("Parámetros del círculo")
    radio = st.slider("Radio del círculo", 0.0, 100.0, 5.0)
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("Resultados")

    color = st.color_picker("Color del borde - Círculo", "#00f900")
    fig_circulo, ax_circulo = plt.subplots()
    circle = plt.Circle((0, 0), radio, color=color, fill=False)
    ax_circulo.add_artist(circle)
    ax_circulo.set_xlim(-radio - 1, radio + 1)
    ax_circulo.set_ylim(-radio - 1, radio + 1)
    ax_circulo.set_aspect('equal')
    ax_circulo.axis('off')
    st.pyplot(fig_circulo)

# 🟠 RECTÁNGULO
with tab2:
    st.subheader("Parámetros del Rectángulo")
    base = st.slider("Base", 0.0, 100.0, 5.0)
    altura = st.slider("Altura", 0.0, 100.0, 5.0)
    area = base * altura
    perimetro = 2 * (base + altura)
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("Resultados")

    color = st.color_picker("Color del borde - Rectángulo", "#FF5733")
    fig_rect, ax_rect = plt.subplots()
    rect = plt.Rectangle((0, 0), base, altura, edgecolor=color, facecolor='none')
    ax_rect.add_patch(rect)
    ax_rect.set_xlim(-1, base + 1)
    ax_rect.set_ylim(-1, altura + 1)
    ax_rect.set_aspect('equal')
    ax_rect.axis('off')
    st.pyplot(fig_rect)

# 🔵 CUADRADO
with tab3:
    st.subheader("Parámetros del Cuadrado")
    lado = st.slider("Lado", 0.0, 100.0, 5.0)
    area = lado**2
    perimetro = 4 * lado
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("Resultados")

    color = st.color_picker("Color del borde - Cuadrado", "#33FFAA")
    fig_cuad, ax_cuad = plt.subplots()
    square = plt.Rectangle((0, 0), lado, lado, edgecolor=color, facecolor='none')
    ax_cuad.add_patch(square)
    ax_cuad.set_xlim(-1, lado + 1)
    ax_cuad.set_ylim(-1, lado + 1)
    ax_cuad.set_aspect('equal')
    ax_cuad.axis('off')
    st.pyplot(fig_cuad)

# 🔺 TRIÁNGULO
with tab4:
    st.subheader("Parámetros del Triángulo")
    base = st.slider("Base", 0.0, 100.0, 5.0)
    altura = st.slider("Altura", 0.0, 100.0, 5.0)
    lado_a = st.slider("Lado a", 0.0, 100.0, 5.0)
    lado_b = st.slider("Lado b", 0.0, 100.0, 5.0)
    lado_c = st.slider("Lado c", 0.0, 100.0, 5.0)
    area = (base * altura) / 2
    perimetro = lado_a + lado_b + lado_c
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("Resultados")

    color = st.color_picker("Color del borde - Triángulo", "#FF00FF")
    fig_tri, ax_tri = plt.subplots()
    triangle = plt.Polygon([[0, 0], [base, 0], [base / 2, altura]], edgecolor=color, facecolor='none')
    ax_tri.add_patch(triangle)
    ax_tri.set_xlim(-1, base + 1)
    ax_tri.set_ylim(-1, altura + 1)
    ax_tri.set_aspect('equal')
    ax_tri.axis('off')
    
