import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="APOLLO PRO", page_icon="💪", layout="centered")

st.title("🚀 APOLLO PRO")

# LOGIN
if "user" not in st.session_state:
    name = st.text_input("👤 Nombre")
    if st.button("Entrar"):
        st.session_state.user = name
        st.rerun()
    st.stop()

st.sidebar.write(f"👤 {st.session_state.user}")

# ESTADOS
if "workouts" not in st.session_state:
    st.session_state.workouts = []

if "weights" not in st.session_state:
    st.session_state.weights = []

if "diet" not in st.session_state:
    st.session_state.diet = {"C1": False, "C2": False, "C3": False}

# MENU
menu = st.sidebar.radio("Menú", ["🏋️ Entreno", "🍽️ Dieta", "⚖️ Peso", "📊 Progreso"])

# ENTRENAMIENTO
if menu == "🏋️ Entreno":

    st.header("🏋️ Entrenamiento")

    ejercicios = ["Press inclinado", "Sentadilla", "Dominadas", "Curl bíceps"]

    completados = 0

    for ej in ejercicios:
        if st.checkbox(ej):
            completados += 1

    st.progress(completados / len(ejercicios))

    if completados == len(ejercicios):
        if st.button("Guardar"):
            st.session_state.workouts.append(datetime.now().strftime("%Y-%m-%d"))
            st.success("Entreno guardado")

# DIETA
elif menu == "🍽️ Dieta":

    st.header("🍽️ Dieta")

    comidas = {
        "C1": "500 kcal - Desayuno completo",
        "C2": "850 kcal - Comida fuerte",
        "C3": "800 kcal - Cena"
    }

    total = 0

    for key, val in comidas.items():
        st.write(val)
        check = st.checkbox("Hecho", value=st.session_state.diet[key])
        st.session_state.diet[key] = check

        if check:
            total += 1

    st.progress(total / 3)

    if total == 3:
        st.success("🔥 Dieta perfecta")

# PESO
elif menu == "⚖️ Peso":

    st.header("⚖️ Peso")

    peso = st.number_input("Peso actual")
    objetivo = st.number_input("Objetivo")

    if st.button("Guardar peso"):
        st.session_state.weights.append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "peso": peso,
            "objetivo": objetivo
        })
        st.success("Guardado")

    if st.session_state.weights:
        df = pd.DataFrame(st.session_state.weights)
        st.line_chart(df.set_index("fecha")["peso"])

# PROGRESO
elif menu == "📊 Progreso":

    st.header("📊 Progreso general")

    st.write(f"Entrenos: {len(st.session_state.workouts)}")

    dieta_ok = sum(st.session_state.diet.values())
    st.write(f"Dieta hoy: {dieta_ok}/3")

    if st.session_state.weights:
        df = pd.DataFrame(st.session_state.weights)
        st.line_chart(df.set_index("fecha")["peso"])
