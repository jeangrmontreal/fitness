import streamlit as st
from supabase import create_client
from datetime import datetime
import pandas as pd

SUPABASE_URL = "https://obhfwfkfeyfoiyuwczbe.supabase.co"
SUPABASE_KEY = "PEGA_TU_KEY_AQUI"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("🚀 APOLLO PRO+")

if "usuario" not in st.session_state:
    st.session_state.usuario = ""

if not st.session_state.usuario:
    nombre = st.text_input("Nombre")
    if st.button("Entrar"):
        st.session_state.usuario = nombre
        st.rerun()
    st.stop()

usuario = st.session_state.usuario

TABLE = "USUARIOS"

res = supabase.table(TABLE).select("*").eq("nombre", usuario).execute()

if not res.data:
    supabase.table(TABLE).insert({
        "nombre": usuario,
        "historial": [],
        "pesos": []
    }).execute()
    res = supabase.table(TABLE).select("*").eq("nombre", usuario).execute()

user_data = res.data[0]

st.write(f"Hola {usuario}")

if st.button("Guardar prueba"):
    historial = user_data["historial"] or []
    historial.append({"test": "ok"})

    supabase.table(TABLE).update({
        "historial": historial
    }).eq("nombre", usuario).execute()

    st.success("Guardado 🔥")
