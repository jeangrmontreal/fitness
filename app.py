import streamlit as st
import time
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="APOLLO FITNESS", page_icon="💪", layout="centered")

st.title("🚀 APOLLO FITNESS")

# LOGIN
if "usuario" not in st.session_state:
    usuario = st.text_input("👤 Tu nombre")
    if st.button("Entrar"):
        st.session_state.usuario = usuario
        st.rerun()
    st.stop()

st.sidebar.write(f"👤 {st.session_state.usuario}")

# ESTADOS
if "historial" not in st.session_state:
    st.session_state.historial = []

if "pesos" not in st.session_state:
    st.session_state.pesos = []

# MENÚ
menu = st.sidebar.radio(
    "Menú",
    ["🏋️ Entrenamiento", "📊 Progreso", "📅 Historial", "🍽️ Dieta", "⚖️ Peso"]
)

# ---------------- ENTRENAMIENTO ----------------
if menu == "🏋️ Entrenamiento":

    st.header("🏋️ Entrenamiento")

    rutinas = {
        "Día 1": ["Press inclinado", "Press convergente", "Aperturas", "Laterales", "Fondos"],
        "Día 2": ["Remo barra", "Dominadas", "Remo mancuerna", "Curl", "Pájaros"],
        "Día 3": ["Sentadilla", "Prensa", "Curl femoral", "Extensión", "Gemelos"],
        "Día 4": ["Press inclinado", "Aperturas", "Press máquina", "Press militar"]
    }

    dia = st.selectbox("Selecciona tu día", list(rutinas.keys()))
    rutina = rutinas[dia]

    completados = 0
    registro = []

    for i, ejercicio in enumerate(rutina):

        st.subheader(ejercicio)

        col1, col2, col3 = st.columns(3)

        with col1:
            series = st.number_input("Series", 1, 10, 3, key=f"s_{i}")

        with col2:
            reps = st.number_input("Reps", 1, 20, 10, key=f"r_{i}")

        with col3:
            peso = st.number_input("Peso", 0.0, step=2.5, key=f"p_{i}")

        hecho = st.checkbox("Completar", key=f"c_{i}")

        if hecho:
            completados += 1
            registro.append({
                "ejercicio": ejercicio,
                "series": series,
                "reps": reps,
                "peso": peso
            })

            if st.button("Descanso", key=f"b_{i}"):
                timer = st.empty()
                for t in range(30, 0, -1):
                    timer.markdown(f"## ⏳ {t} s")
                    time.sleep(1)
                timer.markdown("## ✅ Listo")

        st.divider()

    st.progress(completados / len(rutina))

    if completados == len(rutina):
        if st.button("💾 Guardar entrenamiento"):
            fecha = datetime.now().strftime("%Y-%m-%d")
            for item in registro:
                st.session_state.historial.append({
                    "fecha": fecha,
                    **item
                })
            st.success("Entrenamiento guardado 🔥")

# ---------------- PROGRESO ----------------
elif menu == "📊 Progreso":

    st.header("📊 Progreso")

    if st.session_state.historial:
        df = pd.DataFrame(st.session_state.historial)
        ejercicio = st.selectbox("Ejercicio", df["ejercicio"].unique())
        df_f = df[df["ejercicio"] == ejercicio]
        st.line_chart(df_f.set_index("fecha")["peso"])
    else:
        st.info("Aún no hay datos")

# ---------------- HISTORIAL ----------------
elif menu == "📅 Historial":

    st.header("📅 Historial")

    if st.session_state.historial:
        st.dataframe(pd.DataFrame(st.session_state.historial))
    else:
        st.info("No hay entrenamientos")

# ---------------- DIETA ----------------
elif menu == "🍽️ Dieta":

    st.header("🍽️ Dieta")

    comida = st.selectbox("Comida", ["Comida 1", "Comida 2", "Comida 3"])

    if comida == "Comida 1":

        opcion = st.radio("Opciones", [
            "Tostada jamón",
            "Tostada huevos",
            "Tortitas avena",
            "Leche + cereales"
        ])

        if opcion == "Tostada jamón":
            st.write("Pan 100g | Jamón 50g | Tomate 50g | Aceite 8ml | Fruta")

        elif opcion == "Tostada huevos":
            st.write("Pan 100g | Huevo 100g | Guacamole 20g | Fruta")

        elif opcion == "Tortitas avena":
            st.write("Avena 50g | Huevo 60g | Claras 80g | Plátano 100g")

        else:
            st.write("Leche 300g | Corn flakes 50g | Cacao 10g")

        st.success("🔥 500 kcal")

    elif comida == "Comida 2":

        opcion = st.radio("Opciones", [
            "Patata + atún",
            "Arroz + pollo",
            "Pasta + carne",
            "Macarrones + salmón"
        ])

        if opcion == "Patata + atún":
            st.write("Patata 300g | Atún 160g | Huevo 120g")

        elif opcion == "Arroz + pollo":
            st.write("Arroz 85g | Pollo 150g")

        elif opcion == "Pasta + carne":
            st.write("Pasta 100g | Carne 200g")

        else:
            st.write("Macarrones 100g | Salmón 220g")

        st.success("🔥 850 kcal")

    else:

        opcion = st.radio("Opciones", [
            "Pasta + pollo",
            "Merluza + patata",
            "Arroz + atún",
            "Pavo + quinoa"
        ])

        if opcion == "Pasta + pollo":
            st.write("Pasta 120g | Pollo 200g")

        elif opcion == "Merluza + patata":
            st.write("Patata 300g | Merluza 200g")

        elif opcion == "Arroz + atún":
            st.write("Arroz 120g | Atún 160g")

        else:
            st.write("Quinoa 120g | Pavo 200g")

        st.success("🔥 800 kcal")

    st.markdown("---")
    st.write("🔥 Total: 2150 kcal")
    st.write("💧 Agua: 3–4L")
    st.write("⚡ Creatina: 7g")

# ---------------- PESO ----------------
elif menu == "⚖️ Peso":

    st.header("⚖️ Peso")

    peso = st.number_input("Peso actual", 40.0, 150.0)
    objetivo = st.number_input("Objetivo", 40.0, 150.0)

    if st.button("Guardar"):
        st.session_state.pesos.append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "peso": peso,
            "objetivo": objetivo
        })
        st.success("Guardado")

    if st.session_state.pesos:
        df = pd.DataFrame(st.session_state.pesos)
        st.line_chart(df.set_index("fecha")["peso"])
