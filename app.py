import streamlit as st
from supabase import create_client
from datetime import datetime
import pandas as pd

st.title("🚀 APOLLO v6")

SUPABASE_URL = "https://obhfwfkfeyfoiyuwczbe.supabase.co"
SUPABASE_KEY = "sb_publishable__6hcsOxp7_6blIRz-nOphQ_8RZCKW2d"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.success("✅ Conectado a Supabase")

# -------- LOGIN --------
if "usuario" not in st.session_state:
    st.session_state.usuario = ""

if not st.session_state.usuario:
    nombre = st.text_input("👤 Tu nombre")
    if st.button("Entrar"):
        st.session_state.usuario = nombre.strip()
        st.rerun()
    st.stop()

usuario = st.session_state.usuario

# -------- USUARIO --------
res = supabase.table("usuarios").select("*").eq("nombre", usuario).execute()

if not res.data:
    supabase.table("usuarios").insert({
        "nombre": usuario,
        "historial": [],
        "pesos": []
    }).execute()
    res = supabase.table("usuarios").select("*").eq("nombre", usuario).execute()

user = res.data[0]

st.write(f"👤 {usuario}")

# -------- ENTRENAMIENTO --------
st.header("🏋️ Entrenamiento")

ejercicio = st.selectbox("Ejercicio", ["Press banca", "Sentadilla", "Dominadas"])
peso = st.number_input("Peso", 0.0, step=2.5)
reps = st.number_input("Reps", 1, 20)
series = st.number_input("Series", 1, 10)

if st.button("💾 Guardar entreno"):

    historial = user.get("historial")

    if not isinstance(historial, list):
        historial = []

    historial.append({
        "fecha": datetime.now().strftime("%Y-%m-%d"),
        "ejercicio": ejercicio,
        "peso": float(peso),
        "reps": int(reps),
        "series": int(series)
    })

    supabase.table("usuarios").update({
        "historial": historial
    }).eq("id", user["id"]).execute()

    st.success("🔥 Entreno guardado")

# -------- HISTORIAL --------
st.header("📊 Historial")

historial = user.get("historial")

if historial:
    df = pd.DataFrame(historial)
    st.dataframe(df)
else:
    st.info("No hay entrenos aún")
