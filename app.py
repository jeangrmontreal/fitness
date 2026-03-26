import streamlit as st
from supabase import create_client
from datetime import datetime
import pandas as pd

# 🔥 PEGA AQUÍ TUS DATOS
SUPABASE_URL = "https://obhfwfkfeyfoiyuwczbe.supabase.co"
SUPABASE_KEY = "sb_publishable__6hcsOxp7_6blIRz-nOphQ_8RZCKW2d"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="APOLLO PRO+", page_icon="💪")

st.title("🚀 APOLLO PRO+")

# -------- LOGIN --------
if "usuario" not in st.session_state:
    st.session_state.usuario = ""

if not st.session_state.usuario:
    nombre = st.text_input("👤 Nombre")
    if st.button("Entrar"):
        st.session_state.usuario = nombre
        st.rerun()
    st.stop()

usuario = st.session_state.usuario
st.sidebar.write(f"👤 {usuario}")

# -------- BUSCAR USUARIO --------
res = supabase.table("usuarios").select("*").eq("nombre", usuario).execute()

if not res.data:
    supabase.table("usuarios").insert({
        "nombre": usuario,
        "historial": [],
        "pesos": []
    }).execute()

res = supabase.table("usuarios").select("*").eq("nombre", usuario).execute()
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

    if completados == len(ejercicios):
        if st.button("Guardar entrenamiento"):

            historial = user_data["historial"]
            historial.extend(registro)

            supabase.table("usuarios").update({
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
        st.line_chart(df_f.set_index("ejercicio")["peso"])
    else:
        st.info("Sin datos")

# -------- PESO --------
elif menu == "⚖️ Peso":

    st.header("Peso")

    peso = st.number_input("Peso actual")
    objetivo = st.number_input("Objetivo")

    if st.button("Guardar peso"):

        pesos = user_data["pesos"]
        pesos.append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "peso": peso,
            "objetivo": objetivo
        })

        supabase.table("usuarios").update({
            "pesos": pesos
        }).eq("nombre", usuario).execute()

        st.success("Peso guardado")
