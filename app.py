import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

st.title("Calculadora Geométrica y Trigonométrica.")
st.sidebar.write("Deyra Renata Herrera Juárez Matrícula:38584 Grupo: 3L")
# Crear pestañas
tab1, tab2 = st.tabs(["Geometría", "Trigonometría"])

# 🟦 GEOMETRÍA
with tab1:
    figura = st.selectbox("Selecciona la figura", ["Triángulo", "Círculo", "Rectángulo", "Cuadrado", "Teorema de Pitágoras"])

    # TRIÁNGULO
    if figura == "Triángulo":
        st.subheader("Parámetros del triángulo")
        base = st.number_input("Base (b)", min_value=0.0, format="%.2f")
        altura = st.number_input("Altura (h)", min_value=0.0, format="%.2f")
        lado_a = st.number_input("Lado a", min_value=0.0, format="%.2f")
        lado_b = st.number_input("Lado b", min_value=0.0, format="%.2f")
        lado_c = st.number_input("Lado c", min_value=0.0, format="%.2f")
        color = st.color_picker("Color del borde", "#00F900")
        area = 0.5 * base * altura
        perimetro = lado_a + lado_b + lado_c
        st.metric("Área", f"{area:.2f}")
        st.metric("Perímetro", f"{perimetro:.2f}")
        st.success("Resultados")

        fig_tri, ax_tri = plt.subplots()
        x = [-base/2, base/2, 0]
        y = [0, 0, altura]
        triangle = plt.Polygon(list(zip(x, y)), edgecolor=color, fill=False)
        ax_tri.add_patch(triangle)
        ax_tri.set_xlim(-base, base)
        ax_tri.set_ylim(0, altura + 2)
        ax_tri.set_aspect('equal')
        ax_tri.axis('off')
        st.pyplot(fig_tri)

    # CÍRCULO
    if figura == "Círculo":
        st.subheader("Parámetros del círculo")
        radio = st.slider("Radio del círculo", 0.0, 100.0, 5.0)
        area = math.pi * radio**2
        perimetro = 2 * math.pi * radio
        color = st.color_picker("Color del borde", "#00F900")
        st.metric("Área", f"{area:.2f}")
        st.metric("Perímetro", f"{perimetro:.2f}")
        st.success("Resultados")

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
        base = st.slider("Base", 0.0, 100.0, 5.0)
        altura = st.slider("Altura", 0.0, 100.0, 5.0)
        area = base * altura
        perimetro = 2 * (base + altura)
        color = st.color_picker("Color del borde", "#00F900")
        st.metric("Área", f"{area:.2f}")
        st.metric("Perímetro", f"{perimetro:.2f}")
        st.success("Resultados")

        fig_rect, ax_rect = plt.subplots()
        rect = plt.Rectangle((0, 0), base, altura, edgecolor=color, facecolor='none')
        ax_rect.add_patch(rect)
        ax_rect.set_xlim(-1, base + 1)
        ax_rect.set_ylim(-1, altura + 1)
        ax_rect.set_aspect('equal')
        ax_rect.axis('off')
        st.pyplot(fig_rect)

    # CUADRADO
    if figura == "Cuadrado":
        st.subheader("Parámetros del Cuadrado")
        lado = st.slider("Lado", 0.0, 100.0, 5.0)
        area = lado**2
        perimetro = 4 * lado
        color = st.color_picker("Color del borde", "#00F900")
        st.metric("Área", f"{area:.2f}")
        st.metric("Perímetro", f"{perimetro:.2f}")
        st.success("Resultados")

        fig_cuad, ax_cuad = plt.subplots()
        square = plt.Rectangle((0, 0), lado, lado, edgecolor=color, facecolor='none')
        ax_cuad.add_patch(square)
        ax_cuad.set_xlim(-1, lado + 1)
        ax_cuad.set_ylim(-1, lado + 1)
        ax_cuad.set_aspect('equal')
        ax_cuad.axis('off')
        st.pyplot(fig_cuad)

    # TEOREMA DE PITÁGORAS
    if figura == "Teorema de Pitágoras":
        st.subheader("Calculadora del Teorema de Pitágoras")
        cateto_a = st.number_input("Cateto a", min_value=0.0, format="%.2f")
        cateto_b = st.number_input("Cateto b", min_value=0.0, format="%.2f")
        color = st.color_picker("Color del borde", "#00F900")

        if cateto_a > 0 and cateto_b > 0:
            hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
            st.metric("Hipotenusa", f"{hipotenusa:.2f}")
            st.success("Resultados")

            A = [0, 0]
            B = [cateto_a, 0]
            C = [cateto_a, cateto_b]

            fig_pitagoras, ax_pitagoras = plt.subplots()
            triangle = plt.Polygon([A, B, C], edgecolor=color, fill=False)
            ax_pitagoras.add_patch(triangle)
            ax_pitagoras.text((A[0] + B[0]) / 2, -0.5, "a", ha='center')
            ax_pitagoras.text(C[0] + 0.5, (B[1] + C[1]) / 2, "b", va='center')
            ax_pitagoras.text((A[0] + C[0]) / 2 - 0.5, (A[1] + C[1]) / 2, "c", rotation=45)
            ax_pitagoras.set_xlim(-1, cateto_a + 2)
            ax_pitagoras.set_ylim(-1, cateto_b + 2)
            ax_pitagoras.set_aspect('equal')
            ax_pitagoras.axis('off')
            st.pyplot(fig_pitagoras)
        else:
            st.info("Ingresa valores mayores a cero para visualizar el triángulo.")

# 📐 TRIGONOMETRÍA
with tab2:
    st.subheader("Visualizador de funciones trigonométricas")
    opcion = st.selectbox("Selecciona la función", ["Seno", "Coseno", "Tangente", "Onda Amortiguada"])
    frecuencia = st.slider("Frecuencia", 0.1, 10.0, 1.0)
    amplitud = st.slider("Amplitud", 0.1, 5.0, 1.0)
    x = np.linspace(0, 10, 500)

    if opcion == "Seno":
        y = amplitud * np.sin(frecuencia * x)
    elif opcion == "Coseno":
        y = amplitud * np.cos(frecuencia * x)
    elif opcion == "Tangente":
        y = amplitud * np.tan(frecuencia * x)
        y[np.abs(y) > 10] = np.nan
    elif opcion == "Onda Amortiguada":
        y = amplitud * np.exp(-0.1 * x) * np.sin(frecuencia * x)

    fig_funcion, ax_funcion = plt.subplots()
    ax_funcion.plot(x, y, color="red")
    ax_funcion.set_title(f"Función: {opcion}")
    ax_funcion.grid(True)
    st.pyplot(fig_funcion)
    
