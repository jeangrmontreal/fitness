import streamlit as st
from supabase import create_client
from datetime import datetime
import pandas as pd
import time

# -------- CONFIG --------
SUPABASE_URL = "https://obhfwfkfeyfoiyuwczbe.supabase.co"
SUPABASE_KEY = "sb_publishable__6hcsOxp7_6blIRz-nOphQ_8RZCKW2d"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="APOLLO PRO", layout="centered")

st.title("🚀 APOLLO PRO")

# -------- LOGIN CON CODIGO --------
if "usuario" not in st.session_state:
    st.session_state.usuario = None
    st.session_state.rol = None

if not st.session_state.usuario:

    nombre = st.text_input("👤 Nombre")
    codigo = st.text_input("🔑 Código acceso", type="password")

    if st.button("Entrar"):

        if codigo == "apollo123":  # 🔥 código entrenador
            st.session_state.rol = "entrenador"
            st.session_state.usuario = "ENTRENADOR"
        else:
            st.session_state.rol = "cliente"
            st.session_state.usuario = nombre.strip()

        st.rerun()

    st.stop()

usuario = st.session_state.usuario
rol = st.session_state.rol

st.sidebar.write(f"👤 {usuario}")
st.sidebar.write(f"Rol: {rol}")

# -------- MODO ENTRENADOR --------
if rol == "entrenador":

    st.header("👥 Panel de clientes")

    res = supabase.table("usuarios").select("*").execute()

    nombres = [u["nombre"] for u in res.data]

    cliente = st.selectbox("Selecciona cliente", nombres)

    user = next(u for u in res.data if u["nombre"] == cliente)

    st.write(f"📊 Viendo a: {cliente}")

# -------- MODO CLIENTE --------
else:

    res = supabase.table("usuarios").select("*").eq("nombre", usuario).execute()

    if not res.data:
        supabase.table("usuarios").insert({
            "nombre": usuario,
            "historial": [],
            "pesos": []
        }).execute()
        res = supabase.table("usuarios").select("*").eq("nombre", usuario).execute()

    user = res.data[0]

# -------- MENU --------
menu = st.sidebar.radio("Menú", [
    "🏋️ Entreno",
    "📊 Progreso",
    "📅 Historial",
    "🍽️ Dieta"
])

# -------- ENTRENAMIENTO --------
if menu == "🏋️ Entreno":

    st.header("🏋️ Rutina")

    ejercicios = {
        "Press inclinado en Smith": (3, "6-8"),
        "Press convergente": (3, "10-12"),
        "Aperturas en contractora": (3, "10-12"),
        "Elevaciones laterales": (4, "12-15"),
        "Fondos en paralelas": (4, "8-12"),
    }

    for ej, (series, reps) in ejercicios.items():
        st.write(f"**{ej}** → {series} series | {reps} reps")

# -------- HISTORIAL --------
elif menu == "📅 Historial":

    historial = user.get("historial")

    if historial:
        df = pd.DataFrame(historial)
        st.dataframe(df)

# -------- PROGRESO --------
elif menu == "📊 Progreso":

    historial = user.get("historial")

    if historial:
        df = pd.DataFrame(historial)
        df = df[df["tipo"] == "entreno"]

        if not df.empty:
            ejercicio = st.selectbox("Ejercicio", df["ejercicio"].unique())
            st.line_chart(df[df["ejercicio"] == ejercicio]["peso"])

# -------- DIETA --------
elif menu == "🍽️ Dieta":

    st.header("🍽️ Dieta")

    st.write("Plan diario personalizado")
