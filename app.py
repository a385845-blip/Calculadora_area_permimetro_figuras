import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

st.title("Calcular el área y permímetro de figuras")
st.sidebar.write("Deyra Renata Herrera Juárez Matrícula:38584 Grupo: 3L")
figura = st.selectbox("Selecciona la figura", ["Triángulo", "Círculo", "Rectángulo", "Cuadrado", "Trigonometría", "Teorema de pitágoras"])

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

    color = st.color_picker("Color del borde - Triángulo", "#00f900")
    fig_triangulo, ax_triangulo = plt.subplots()
    x = [-base/2, base/2, 0]
    y = [0, 0, altura]
    triangle = plt.Polygon(list(zip(x, y)), edgecolor=color, fill=False)
    ax_triangulo.add_artist(triangle)
    ax_triangulo.set_xlim(-base, base)
    ax_triangulo.set_ylim(0, altura + 2)
    ax_triangulo.set_aspect('equal')
    ax_triangulo.axis('off')
    st.pyplot(fig_triangulo)

# CÍRCULO
if figura == "Círculo":
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

# RECTÁNGULO

if figura == "Rectángulo":
    st.subheader("Parámetros del Rectángulo")
    base = st.slider("Selecciona la magnitud de la base", 0.0, 100.0, 5.0)
    altura = st.slider("Selecciona la magnitud de la altura", 0.0, 100.0, 5.0)
    area = base * altura
    perimetro = 2 * (base + altura)
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("Resultados")

    color = st.color_picker("Color del borde - Rectángulo", "#FF5733")
    fig, ax = plt.subplots()
    rect = plt.Rectangle((0, 0), base, altura, edgecolor=color, facecolor='none')
    ax.add_patch(rect)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 1)
    ax.set_aspect('equal')
    ax.axis('off')
    st.pyplot(fig)
    
# CUADRADO

if figura == "Cuadrado":
    st.subheader("Parámetros del Cuadrado")
    lado = st.slider("Selecciona la magnitud del lado", 0.0, 100.0, 5.0)
    area = lado**2
    perimetro = 4 * lado
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("Resultados")

    color = st.color_picker("Color del borde - Cuadrado", "#33FFAA")
    fig, ax = plt.subplots()
    square = plt.Rectangle((0, 0), lado, lado, edgecolor=color, facecolor='none')
    ax.add_patch(square)
    ax.set_xlim(-1, lado + 1)
    ax.set_ylim(-1, lado + 1)
    ax.set_aspect('equal')
    ax.axis('off')
    st.pyplot(fig)
    
# Trigonometría

if figura == "Trigonometría":
    st.subheader("Funciones trigonométricas")
    funcion = st.selectbox("Selecciona la función", ["Seno", "Coseno", "Tangente"])
    rango = st.slider("Rango en radianes", 0.0, 4 * math.pi, (0.0, 2 * math.pi))
    amplitud = st.slider("Amplitud", 0.1, 5.0, 1.0)

    x = np.linspace(rango[0], rango[1], 300)

    if funcion == "Seno":
        y = amplitud * np.sin(x)
    elif funcion == "Coseno":
        y = amplitud * np.cos(x)
    elif funcion == "Tangente":
        y = amplitud * np.tan(x)
        y[np.abs(y) > 10] = np.nan  # Evita saltos extremos

    fig_trigo, ax_trigo = plt.subplots()
    ax_trigo.plot(x, y, color="purple")
    ax_trigo.set_title(f"Función {funcion}")
    ax_trigo.grid(True)
    st.pyplot(fig_trigo)

# Teorema de pitágoras
if figura == "Teorema de Pitágoras":
    st.subheader("Calculadora del Teorema de Pitágoras")
    cateto_a = st.number_input("Cateto a", min_value=0.0, format="%.2f")
    cateto_b = st.number_input("Cateto b", min_value=0.0, format="%.2f")

    if cateto_a > 0 and cateto_b > 0:
        hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
        st.metric("Hipotenusa", f"{hipotenusa:.2f}")
        st.success("Resultados")

        # Coordenadas del triángulo rectángulo
        punto_A = [0, 0]
        punto_B = [cateto_a, 0]
        punto_C = [cateto_a, cateto_b]

        fig_pitagoras, ax_pitagoras = plt.subplots()
        triangle = plt.Polygon([punto_A, punto_B, punto_C], edgecolor="blue", fill=False)
        ax_pitagoras.add_patch(triangle)

        # Etiquetas
        ax_pitagoras.text((punto_A[0] + punto_B[0]) / 2, -0.5, "a", ha='center')
        ax_pitagoras.text(punto_C[0] + 0.5, (punto_B[1] + punto_C[1]) / 2, "b", va='center')
        ax_pitagoras.text((punto_A[0] + punto_C[0]) / 2 - 0.5, (punto_A[1] + punto_C[1]) / 2, "c", rotation=45)

        ax_pitagoras.set_xlim(-1, cateto_a + 2)
        ax_pitagoras.set_ylim(-1, cateto_b + 2)
        ax_pitagoras.set_aspect('equal')
        ax_pitagoras.axis('off')
        st.pyplot(fig_pitagoras)
    else:
        st.info("Ingresa valores mayores a cero para visualizar el triángulo.")
        st.pyplot(fig_pitagoras)
    else:
        st.info("Ingresa valores mayores a cero para visualizar el triángulo.")
  

