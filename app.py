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

if "dieta_check" not in st.session_state:
    st.session_state.dieta_check = {"C1": False, "C2": False, "C3": False}

# MENÚ LATERAL (COMO TE GUSTABA)
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
    pesos_registro = []

    for i, ejercicio in enumerate(rutina):
        st.subheader(ejercicio)

        peso = st.number_input("Peso (kg)", min_value=0.0, step=2.5, key=f"peso_{i}")
        hecho = st.checkbox("Completar", key=f"check_{i}")

        if hecho:
            completados += 1
            pesos_registro.append({"ejercicio": ejercicio, "peso": peso})

            if st.button("Descanso", key=f"btn_{i}"):
                for t in range(30, 0, -1):
                    st.write(f"{t}s")
                    time.sleep(1)

        st.divider()

    st.progress(completados / len(rutina))

    if completados == len(rutina):
        if st.button("💾 Guardar entrenamiento"):
            fecha = datetime.now().strftime("%Y-%m-%d")
            for item in pesos_registro:
                st.session_state.historial.append({
                    "fecha": fecha,
                    "ejercicio": item["ejercicio"],
                    "peso": item["peso"]
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
        st.info("No hay entrenamientos guardados")

# ---------------- DIETA ----------------
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
            value=st.session_state.dieta_check[key],
            key=f"dieta_{key}"
        )

        st.session_state.dieta_check[key] = check

        if check:
            total += 1

    st.progress(total / 3)

    if total == 3:
        st.success("🔥 Dieta perfecta")

    st.markdown("---")
    st.write("🔥 2150 kcal")
    st.write("💧 Agua: 3–4L")
    st.write("⚡ Creatina: 7g")

# ---------------- PESO ----------------
elif menu == "⚖️ Peso":

    st.header("⚖️ Peso")

    peso = st.number_input("Peso actual", min_value=40.0, max_value=150.0, key="peso_actual")
    objetivo = st.number_input("Objetivo", min_value=40.0, max_value=150.0, key="peso_obj")

    if st.button("Guardar peso"):
        st.session_state.pesos.append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "peso": peso,
            "objetivo": objetivo
        })
        st.success("Guardado")

    if st.session_state.pesos:
        df = pd.DataFrame(st.session_state.pesos)
        st.line_chart(df.set_index("fecha")["peso"])
