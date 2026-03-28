import streamlit as st
import json
from datetime import datetime
import pandas as pd
import time
import os

st.set_page_config(page_title="APOLLO", layout="centered")

FILE = "data.json"

# -------- CREAR ARCHIVO --------
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({"entrenos": [], "dietas": [], "pesos": []}, f)

with open(FILE, "r") as f:
    data = json.load(f)

st.markdown("## 💪 APOLLO")

menu = st.radio("", ["🏋️ Entreno", "🍽️ Dieta", "📊 Progreso"], horizontal=True)

# ---------------- ENTRENAMIENTO ----------------
if menu == "🏋️ Entreno":

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
            st.session_state.timer = 60

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
            "ejercicios": registro
        })

        with open(FILE, "w") as f:
            json.dump(data, f)

        st.success("Entreno guardado 🔥")

# ---------------- DIETA ----------------
elif menu == "🍽️ Dieta":

    st.subheader("🍽️ Dieta (2150 kcal)")

    dieta = {
        "Desayuno": [
            ("Tostada de pan integral, jamón serrano, tomate y aceite + fruta", 500),
            ("Pan integral + huevos revueltos + guacamole + fruta", 500),
            ("Tortitas de avena con chocolate y fresas", 500),
            ("Leche con corn flakes + cacao + fruta", 500),
        ],
        "Comida": [
            ("Patata + atún + huevo + pimiento", 850),
            ("Arroz + pollo + champiñones", 850),
            ("Espaguetis + carne + tomate", 850),
            ("Macarrones + salmón + verduras", 850),
        ],
        "Cena": [
            ("Pasta + pollo + verduras", 800),
            ("Merluza + puré de patatas", 800),
            ("Arroz + atún + verduras", 800),
            ("Pavo + quinoa + judías", 800),
        ]
    }

    total = 0
    seleccion = {}

    for comida, opciones in dieta.items():

        nombres = [o[0] for o in opciones]
        opcion = st.selectbox(comida, nombres, key=comida)

        kcal = next(o[1] for o in opciones if o[0] == opcion)

        st.write(f"🔥 {kcal} kcal")

        seleccion[comida] = opcion
        total += kcal

    st.markdown("---")
    st.success(f"🔥 TOTAL: {total} kcal")

    if st.button("💾 Guardar dieta"):

        data["dietas"].append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "comidas": seleccion,
            "kcal": total
        })

        with open(FILE, "w") as f:
            json.dump(data, f)

        st.success("Dieta guardada ✅")

# ---------------- PROGRESO ----------------
elif menu == "📊 Progreso":

    st.subheader("📊 Progreso")

    # -------- PESO CORPORAL --------
    st.markdown("### ⚖️ Peso corporal")

    peso = st.number_input("Tu peso")

    if st.button("Guardar peso"):
        data["pesos"].append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "peso": peso
        })

        with open(FILE, "w") as f:
            json.dump(data, f)

    if data["pesos"]:
        df_peso = pd.DataFrame(data["pesos"])
        st.line_chart(df_peso.set_index("fecha")["peso"])

    st.markdown("---")

    # -------- PROGRESO EJERCICIOS --------
    st.markdown("### 🏋️ Progreso ejercicios")

    registros = []

    for entreno in data["entrenos"]:

        if "ejercicios" not in entreno:
            continue

        for ej in entreno["ejercicios"]:
            registros.append({
                "fecha": entreno["fecha"],
                "ejercicio": ej["ejercicio"],
                "peso": ej["peso"]
            })

    if registros:
        df = pd.DataFrame(registros)

        ejercicio = st.selectbox("Ejercicio", df["ejercicio"].unique())

        df_filtrado = df[df["ejercicio"] == ejercicio]

        st.line_chart(df_filtrado.set_index("fecha")["peso"])

    else:
        st.info("Sin datos aún")
