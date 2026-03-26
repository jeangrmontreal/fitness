import streamlit as st
from supabase import create_client
from datetime import datetime
import pandas as pd

# 🔥 PON TUS DATOS AQUÍ
SUPABASE_URL = "PEGA_TU_URL_AQUI"
SUPABASE_KEY = "PEGA_TU_PUBLISHABLE_KEY_AQUI"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="APOLLO PRO+", page_icon="💪")

st.title("🚀 APOLLO PRO+")

# -------- LOGIN --------
if "usuario" not in st.session_state:
    st.session_state.usuario = ""

if not st.session_state.usuario:
    nombre = st.text_input("👤 Nombre")
    if st.button("Entrar"):
        st.session_state.usuario = nombre.strip()
        st.rerun()
    st.stop()

usuario = st.session_state.usuario
st.sidebar.write(f"👤 {usuario}")

# -------- TABLA (IMPORTANTE MAYÚSCULAS) --------
TABLE = "USUARIOS"

# -------- BUSCAR USUARIO --------
try:
    res = supabase.table(TABLE).select("*").eq("nombre", usuario).execute()
except Exception as e:
    st.error("Error conectando con Supabase")
    st.stop()

if not res.data:
    supabase.table(TABLE).insert({
        "nombre": usuario,
        "historial": [],
        "pesos": []
    }).execute()
    res = supabase.table(TABLE).select("*").eq("nombre", usuario).execute()

user_data = res.data[0]

# -------- MENU --------
menu = st.sidebar.radio("Menú", ["🏋️ Entreno", "📊 Progreso", "⚖️ Peso"])

# -------- ENTRENAMIENTO --------
if menu == "🏋️ Entreno":

    st.header("Entrenamiento")

    ejercicios = ["Press banca", "Sentadilla", "Dominadas"]

    registro = []
    completados = 0

    for i, ej in enumerate(ejercicios):

        col1, col2, col3 = st.columns(3)

        with col1:
            series = st.number_input("Series", 1, 10, 3, key=f"s_{i}")

        with col2:
            reps = st.number_input("Reps", 1, 20, 10, key=f"r_{i}")

        with col3:
            peso = st.number_input("Peso", 0.0, step=2.5, key=f"p_{i}")

        hecho = st.checkbox(ej, key=f"c_{i}")

        if hecho:
            completados += 1
            registro.append({
                "ejercicio": ej,
                "series": series,
                "reps": reps,
                "peso": peso
            })

    st.progress(completados / len(ejercicios))

    if completados == len(ejercicios):
        if st.button("Guardar entrenamiento"):

            historial = user_data["historial"] or []
            historial.extend(registro)

            supabase.table(TABLE).update({
                "historial": historial
            }).eq("nombre", usuario).execute()

            st.success("Entreno guardado 🔥")

# -------- PROGRESO --------
elif menu == "📊 Progreso":

    st.header("Progreso")

    if user_data["historial"]:
        df = pd.DataFrame(user_data["historial"])
        ejercicio = st.selectbox("Ejercicio", df["ejercicio"].unique())
        df_f = df[df["ejercicio"] == ejercicio]

        if not df_f.empty:
            st.line_chart(df_f["peso"])
    else:
        st.info("Sin datos")

# -------- PESO --------
elif menu == "⚖️ Peso":

    st.header("Peso")

    peso = st.number_input("Peso actual")
    objetivo = st.number_input("Objetivo")

    if st.button("Guardar peso"):

        pesos = user_data["pesos"] or []
        pesos.append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "peso": peso,
            "objetivo": objetivo
        })

        supabase.table(TABLE).update({
            "pesos": pesos
        }).eq("nombre", usuario).execute()

        st.success("Peso guardado")
