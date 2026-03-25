import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="APOLLO PRO", page_icon="💪", layout="centered")

st.title("🚀 APOLLO PRO")

# 👤 LOGIN
if "user" not in st.session_state:
    name = st.text_input("👤 Nombre")
    if st.button("Entrar"):
        st.session_state.user = name
        st.rerun()
    st.stop()

st.sidebar.write(f"👤 {st.session_state.user}")

# 📊 ESTADOS
if "workouts" not in st.session_state:
    st.session_state.workouts = []

if "weights" not in st.session_state:
    st.session_state.weights = []

if "diet" not in st.session_state:
    st.session_state.diet = {"C1": False, "C2": False, "C3": False}

# 📱 MENÚ
menu = st.sidebar.radio(
    "Menú",
    ["🏋️ Entreno", "🍽️ Dieta", "⚖️ Peso", "📊 Progreso"]
)

# 🏋️ ENTRENAMIENTO
if menu == "🏋️ Entreno":

    st.header("🏋️ Entrenamiento")

    ejercicios = ["Press inclinado", "Sentadilla", "Dominadas", "Curl bíceps"]

    completados = 0

    for i, ej in enumerate(ejercicios):
        if st.checkbox(ej, key=f"ej_{i}"):
            completados += 1

    st.progress(completados / len(ejercicios))

    if completados == len(ejercicios):
        if st.button("💾 Guardar entrenamiento"):
            st.session_state.workouts.append(datetime.now().strftime("%Y-%m-%d"))
            st.success("Entreno guardado 💪")

# 🍽️ DIETA (ARREGLADA)
elif menu == "🍽️ Dieta":

    st.header("🍽️ Dieta")

    comidas = {
        "C1": "🍳 Desayuno (500 kcal)",
        "C2": "🍛 Comida (850 kcal)",
        "C3": "🥗 Cena (800 kcal)"
    }

    total = 0

    for key, val in comidas.items():
        st.subheader(val)

        check = st.checkbox(
            "Completada",
            value=st.session_state.diet[key],
            key=f"dieta_{key}"   # 🔥 KEY ÚNICA (ARREGLADO)
        )

        st.session_state.diet[key] = check

        if check:
            total += 1

    st.progress(total / 3)

    if total == 3:
        st.success("🔥 Dieta perfecta hoy")

    st.markdown("---")
    st.write("🔥 Total: 2150 kcal")
    st.write("💧 Agua: 3–4L")
    st.write("⚡ Creatina: 7g")

# ⚖️ PESO
elif menu == "⚖️ Peso":

    st.header("⚖️ Peso y objetivo")

    peso = st.number_input("Peso actual (kg)", min_value=40.0, max_value=150.0, key="peso_actual")
    objetivo = st.number_input("Peso objetivo (kg)", min_value=40.0, max_value=150.0, key="peso_obj")

    if st.button("Guardar peso"):
        st.session_state.weights.append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "peso": peso,
            "objetivo": objetivo
        })
        st.success("Peso guardado")

    if st.session_state.weights:
        df = pd.DataFrame(st.session_state.weights)
        st.line_chart(df.set_index("fecha")["peso"])

# 📊 PROGRESO
elif menu == "📊 Progreso":

    st.header("📊 Progreso general")

    st.write(f"🏋️ Entrenos realizados: {len(st.session_state.workouts)}")

    dieta_ok = sum(st.session_state.diet.values())
    st.write(f"🍽️ Dieta hoy: {dieta_ok}/3")

    if st.session_state.weights:
        df = pd.DataFrame(st.session_state.weights)
        st.line_chart(df.set_index("fecha")["peso"])
