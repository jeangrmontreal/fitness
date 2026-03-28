import streamlit as st
from datetime import datetime
import pandas as pd
import time

st.set_page_config(page_title="APOLLO", layout="centered")

st.title("💪 APOLLO")

# -------- MENU --------
menu = st.radio("", ["🏋️ Entreno", "🍽️ Dieta", "📊 Progreso"])

# -------- ENTRENAMIENTO --------
if menu == "🏋️ Entreno":

    st.header("🏋️ Rutina")

    ejercicios = [
        "Press inclinado en Smith",
        "Press convergente",
        "Aperturas en contractora",
        "Elevaciones laterales",
        "Fondos en paralelas"
    ]

    if "timer" not in st.session_state:
        st.session_state.timer = 0

    timer_placeholder = st.empty()

    completados = 0

    for i, ej in enumerate(ejercicios):

        st.subheader(ej)

        peso = st.number_input("Peso", 0.0, step=2.5, key=f"p{i}")
        check = st.checkbox("Completado", key=f"c{i}")

        if check:
            completados += 1

        if st.button("⏱️ Descanso", key=f"t{i}"):
            st.session_state.timer = 30

    if st.session_state.timer > 0:
        timer_placeholder.markdown(f"## ⏳ {st.session_state.timer}s")
        time.sleep(1)
        st.session_state.timer -= 1
        st.rerun()

    st.progress(completados / len(ejercicios))

# -------- DIETA --------
elif menu == "🍽️ Dieta":

    st.header("🍽️ Dieta")

    # DESAYUNO
    desayuno = st.selectbox("Desayuno", [
        "Tostada + jamón + fruta (500 kcal)",
        "Huevos + guacamole + fruta (500 kcal)",
        "Tortitas avena + fresas (500 kcal)",
        "Leche + cereales + fruta (500 kcal)"
    ])

    # COMIDA
    comida = st.selectbox("Comida", [
        "Patata + atún + huevo (850 kcal)",
        "Arroz + pollo + verduras (850 kcal)",
        "Pasta + carne + tomate (850 kcal)",
        "Macarrones + salmón (850 kcal)"
    ])

    # CENA
    cena = st.selectbox("Cena", [
        "Pasta + pollo (800 kcal)",
        "Merluza + patata (800 kcal)",
        "Arroz + atún (800 kcal)",
        "Pavo + quinoa (800 kcal)"
    ])

    total = 500 + 850 + 800

    st.success(f"🔥 TOTAL: {total} kcal")

# -------- PROGRESO --------
elif menu == "📊 Progreso":

    st.header("📊 Progreso")

    if "pesos" not in st.session_state:
        st.session_state.pesos = []

    peso = st.number_input("Peso actual")

    if st.button("Guardar peso"):
        st.session_state.pesos.append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "peso": peso
        })

    if st.session_state.pesos:
        df = pd.DataFrame(st.session_state.pesos)
        st.line_chart(df["peso"])
