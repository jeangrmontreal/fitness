import streamlit as st
import json
from datetime import datetime
import pandas as pd
import time
import os

st.set_page_config(page_title="APOLLO", layout="centered")

FILE = "data.json"

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({"entrenos": [], "dietas": [], "pesos": []}, f)

with open(FILE, "r") as f:
    data = json.load(f)

st.markdown("## 💪 APOLLO")

menu = st.radio("", ["🏋️", "🍽️", "📊"], horizontal=True)

# ---------------- ENTRENAMIENTO ----------------
if menu == "🏋️":

    dia = st.selectbox("Día", ["Día 1", "Día 2", "Día 3", "Día 4"])

    rutina = {
        "Día 1": [
            ("Press inclinado Smith", "3x6-8"),
            ("Press convergente", "3x10-12"),
            ("Aperturas contractora", "3x10-12"),
            ("Elevaciones laterales", "4x12-15"),
            ("Fondos tríceps", "4x8-12"),
        ],
        "Día 2": [
            ("Remo barra", "4x12/10/10/8"),
            ("Dominadas", "4x6-8"),
            ("Remo mancuerna", "3x12/10/8"),
            ("Remo inclinado", "3x10-12"),
            ("Pájaros", "3x10-12"),
            ("Curl predicador", "3x10-12"),
            ("Curl martillo", "2x10-8"),
        ],
        "Día 3": [
            ("Sentadilla", "2x6 + 3x10"),
            ("Prensa", "3x8-10"),
            ("Curl femoral", "3x10"),
            ("Extensión cuádriceps", "3x10"),
            ("Peso muerto rumano", "3x10-12"),
            ("Gemelo Smith", "4x10-15"),
        ],
        "Día 4": [
            ("Press inclinado Smith", "3x8/6/6"),
            ("Aperturas", "3x10-12"),
            ("Press máquina", "3x10-12"),
            ("Press militar", "2x8"),
            ("Laterales", "3x10-12"),
            ("Skull crushers", "4x8-10"),
            ("Press cerrado", "4x8-10"),
        ]
    }

    if "timer" not in st.session_state:
        st.session_state.timer = 0

    timer = st.empty()
    registro = []

    for i, (ej, info) in enumerate(rutina[dia]):

        st.markdown(f"**{ej} ({info})**")

        peso = st.number_input("Kg", 0.0, step=2.5, key=f"p{i}")

        if st.button("⏱️", key=f"t{i}"):
            st.session_state.timer = 30

        registro.append({
            "ejercicio": ej,
            "peso": peso
        })

    if st.session_state.timer > 0:
        timer.markdown(f"## ⏳ {st.session_state.timer}s")
        time.sleep(1)
        st.session_state.timer -= 1
        st.rerun()

    if st.button("💾 Guardar entreno"):
        data["entrenos"].append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "dia": dia,
            "data": registro
        })

        with open(FILE, "w") as f:
            json.dump(data, f)

        st.success("Entreno guardado 🔥")

# ---------------- DIETA ----------------
elif menu == "🍽️":

    st.subheader("Dieta (2150 kcal)")

    dieta = {
        "Desayuno": [
            ("Tostada + jamón + fruta", "Pan 100g, jamón 50g...", 500),
            ("Huevos + guacamole", "Huevo 100g, guacamole 20g...", 500),
            ("Tortitas avena", "Avena 50g, huevo, plátano...", 500),
            ("Leche + cereales", "Leche 300g, corn flakes...", 500),
        ],
        "Comida": [
            ("Patata + atún", "Patata 300g, atún...", 850),
            ("Arroz + pollo", "Arroz 85g, pollo 150g...", 850),
            ("Pasta + carne", "Espaguetis 100g...", 850),
            ("Macarrones + salmón", "Salmón 220g...", 850),
        ],
        "Cena": [
            ("Pasta + pollo", "Macarrones 120g...", 800),
            ("Merluza + patata", "Patata 300g...", 800),
            ("Arroz + atún", "Arroz 120g...", 800),
            ("Pavo + quinoa", "Quinoa 120g...", 800),
        ]
    }

    total = 0
    seleccion = {}

    for comida, opciones in dieta.items():

        nombres = [o[0] for o in opciones]
        opcion = st.selectbox(comida, nombres)

        detalle = next(o for o in opciones if o[0] == opcion)

        st.caption(detalle[1])
        st.write(f"{detalle[2]} kcal")

        seleccion[comida] = opcion
        total += detalle[2]

    st.success(f"🔥 TOTAL: {total} kcal")

    if st.button("💾 Guardar dieta"):
        data["dietas"].append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "data": seleccion,
            "kcal": total
        })

        with open(FILE, "w") as f:
            json.dump(data, f)

        st.success("Dieta guardada")

# ---------------- PROGRESO ----------------
elif menu == "📊":

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
