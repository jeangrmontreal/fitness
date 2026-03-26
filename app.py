import streamlit as st
import time
from datetime import datetime
import pandas as pd
import json
import os

st.set_page_config(page_title="APOLLO PRO+", page_icon="💪", layout="centered")

st.title("🚀 APOLLO PRO+")

# ---------------- DATA ----------------
DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"usuarios": {}}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

# ---------------- LOGIN ----------------
if "usuario" not in st.session_state:
    st.session_state.usuario = ""

if not st.session_state.usuario:
    nombre = st.text_input("👤 Nombre de usuario")
    if st.button("Entrar"):
        st.session_state.usuario = nombre
        st.rerun()
    st.stop()

usuario = st.session_state.usuario

# CREAR USUARIO SI NO EXISTE
if usuario not in data["usuarios"]:
    data["usuarios"][usuario] = {
        "historial": [],
        "pesos": [],
        "racha": 0,
        "ultimo_entreno": ""
    }
    save_data(data)

user_data = data["usuarios"][usuario]

# LOGOUT
if st.sidebar.button("Cerrar sesión"):
    st.session_state.usuario = ""
    st.rerun()

st.sidebar.write(f"👤 {usuario}")

# ---------------- MENU ----------------
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

    dia = st.selectbox("Día", list(rutinas.keys()))
    rutina = rutinas[dia]

    completados = 0
    registro = []

    for i, ejercicio in enumerate(rutina):

        st.subheader(ejercicio)

        col1, col2, col3 = st.columns(3)

        with col1:
            series = st.number_input("Series", 1, 10, 3, key=f"{dia}_s_{i}")

        with col2:
            reps = st.number_input("Reps", 1, 20, 10, key=f"{dia}_r_{i}")

        with col3:
            peso = st.number_input("Peso", 0.0, step=2.5, key=f"{dia}_p_{i}")

        hecho = st.checkbox("Completar", key=f"{dia}_c_{i}")

        if hecho:
            completados += 1
            registro.append({
                "ejercicio": ejercicio,
                "series": series,
                "reps": reps,
                "peso": peso
            })

            if st.button("Descanso", key=f"{dia}_b_{i}"):
                timer = st.empty()
                for t in range(30, 0, -1):
                    timer.markdown(f"## ⏳ {t}s")
                    time.sleep(1)
                timer.markdown("## ✅ Listo")

        st.divider()

    progreso = completados / len(rutina)
    st.progress(progreso)

    if completados == len(rutina):
        if st.button("💾 Guardar entrenamiento"):

            hoy = datetime.now().strftime("%Y-%m-%d")

            for item in registro:
                user_data["historial"].append({
                    "fecha": hoy,
                    "dia": dia,
                    **item
                })

            # 🔥 Racha (streak)
            if user_data["ultimo_entreno"] != hoy:
                user_data["racha"] += 1
                user_data["ultimo_entreno"] = hoy

            save_data(data)
            st.success("Entreno guardado 🔥")

# ---------------- PROGRESO ----------------
elif menu == "📊 Progreso":

    st.header("📊 Progreso")

    st.metric("🔥 Racha actual", user_data["racha"])

    if user_data["historial"]:
        df = pd.DataFrame(user_data["historial"])
        ejercicio = st.selectbox("Ejercicio", df["ejercicio"].unique())
        df_f = df[df["ejercicio"] == ejercicio]
        st.line_chart(df_f.set_index("fecha")["peso"])
    else:
        st.info("Sin datos")

# ---------------- HISTORIAL ----------------
elif menu == "📅 Historial":

    st.header("📅 Historial")

    if user_data["historial"]:
        st.dataframe(pd.DataFrame(user_data["historial"]))
    else:
        st.info("Vacío")

# ---------------- DIETA ----------------
elif menu == "🍽️ Dieta":

    st.header("🍽️ Dieta")

    comida = st.selectbox("Comida", ["Comida 1", "Comida 2", "Comida 3"])

    if comida == "Comida 1":
        st.write("Pan 100g | Jamón 50g | Tomate 50g | Aceite 8ml | Fruta")
        st.success("🔥 500 kcal")

    elif comida == "Comida 2":
        st.write("Arroz 85g | Pollo 150g")
        st.success("🔥 850 kcal")

    else:
        st.write("Pasta 120g | Pollo 200g")
        st.success("🔥 800 kcal")

    st.markdown("---")
    st.write("🔥 Total: 2150 kcal")

# ---------------- PESO ----------------
elif menu == "⚖️ Peso":

    st.header("⚖️ Peso")

    peso = st.number_input("Peso actual", 40.0, 150.0)
    objetivo = st.number_input("Objetivo", 40.0, 150.0)

    if st.button("Guardar"):
        user_data["pesos"].append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "peso": peso,
            "objetivo": objetivo
        })
        save_data(data)
        st.success("Guardado")

    if user_data["pesos"]:
        df = pd.DataFrame(user_data["pesos"])
        st.line_chart(df.set_index("fecha")["peso"])
