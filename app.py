import streamlit as st
import json
from datetime import datetime
import pandas as pd
import time
import os

st.set_page_config(page_title="APOLLO", layout="centered")

# -------- FILE STORAGE --------
FILE = "data.json"

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({"entrenos": [], "dietas": [], "pesos": []}, f)

with open(FILE, "r") as f:
    data = json.load(f)

# -------- UI --------
st.markdown("## 💪 APOLLO")

menu = st.radio("", ["🏋️", "🍽️", "📊"], horizontal=True)

# -------- ENTRENAMIENTO --------
if menu == "🏋️":

    st.subheader("Entreno")

    rutina = {
        "Pecho": [
            "Press inclinado en Smith",
            "Press convergente",
            "Aperturas en contractora"
        ],
        "Hombro": [
            "Elevaciones laterales"
        ],
        "Tríceps": [
            "Fondos en paralelas"
        ]
    }

    if "timer" not in st.session_state:
        st.session_state.timer = 0

    timer_box = st.empty()

    registro = []

    for grupo, ejercicios in rutina.items():

        st.markdown(f"### {grupo}")

        for i, ej in enumerate(ejercicios):

            st.write(f"➡️ {ej}")

            col1, col2, col3 = st.columns(3)

            with col1:
                series = st.number_input("S", 1, 10, 3, key=f"s{grupo}{i}")
            with col2:
                reps = st.number_input("R", 1, 20, 10, key=f"r{grupo}{i}")
            with col3:
                peso = st.number_input("Kg", 0.0, step=2.5, key=f"p{grupo}{i}")

            if st.button("⏱️", key=f"t{grupo}{i}"):
                st.session_state.timer = 30

            registro.append({
                "grupo": grupo,
                "ejercicio": ej,
                "series": series,
                "reps": reps,
                "peso": peso
            })

    if st.session_state.timer > 0:
        timer_box.markdown(f"## ⏳ {st.session_state.timer}s")
        time.sleep(1)
        st.session_state.timer -= 1
        st.rerun()

    if st.button("💾 Guardar entreno"):

        data["entrenos"].append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "data": registro
        })

        with open(FILE, "w") as f:
            json.dump(data, f)

        st.success("Guardado 🔥")

# -------- DIETA --------
elif menu == "🍽️":

    st.subheader("Dieta")

    dieta = {
        "Desayuno": [
            ("Tostada jamón", 500),
            ("Huevos + guacamole", 500),
            ("Tortitas avena", 500),
            ("Leche + cereales", 500)
        ],
        "Comida": [
            ("Patata + atún", 850),
            ("Arroz + pollo", 850),
            ("Pasta + carne", 850),
            ("Macarrones + salmón", 850)
        ],
        "Cena": [
            ("Pasta + pollo", 800),
            ("Merluza + patata", 800),
            ("Arroz + atún", 800),
            ("Pavo + quinoa", 800)
        ]
    }

    total = 0
    seleccion = {}

    for comida, opciones in dieta.items():

        nombres = [o[0] for o in opciones]
        opcion = st.selectbox(comida, nombres)

        kcal = next(o[1] for o in opciones if o[0] == opcion)

        st.write(f"{kcal} kcal")

        seleccion[comida] = opcion
        total += kcal

    st.success(f"🔥 TOTAL: {total} kcal")

    if st.button("💾 Guardar dieta"):

        data["dietas"].append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "comidas": seleccion,
            "kcal": total
        })

        with open(FILE, "w") as f:
            json.dump(data, f)

        st.success("Dieta guardada")

# -------- PROGRESO --------
elif menu == "📊":

    st.subheader("Progreso")

    peso = st.number_input("Peso")

    if st.button("Guardar peso"):
        data["pesos"].append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "peso": peso
        })

        with open(FILE, "w") as f:
            json.dump(data, f)

    if data["pesos"]:
        df = pd.DataFrame(data["pesos"])
        st.line_chart(df["peso"])
