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

# -------- USER --------
res = supabase.table("usuarios").select("*").eq("nombre", usuario).execute()

if not res.data:
    supabase.table("usuarios").insert({
        "nombre": usuario,
        "historial": [],
        "pesos": []
    }).execute()
    res = supabase.table("usuarios").select("*").eq("nombre", usuario).execute()

user = res.data[0]

st.sidebar.write(f"👤 {usuario}")

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

    registro = []

    for i, (ej, (series, reps)) in enumerate(ejercicios.items()):

        st.subheader(ej)
        st.write(f"Series: {series} | Reps: {reps}")

        peso = st.number_input(f"Peso {ej}", 0.0, step=2.5, key=f"p{i}")

        if st.button(f"⏱️ Descanso {ej}", key=f"t{i}"):
            for t in range(30, 0, -1):
                st.write(f"⏳ {t}s")
                time.sleep(1)

        registro.append({
            "ejercicio": ej,
            "peso": peso,
            "series": series,
            "reps": reps
        })

    if st.button("💾 Guardar entreno"):

        historial = user.get("historial")
        if not isinstance(historial, list):
            historial = []

        for r in registro:
            r["fecha"] = datetime.now().strftime("%Y-%m-%d")
            historial.append(r)

        supabase.table("usuarios").update({
            "historial": historial
        }).eq("id", user["id"]).execute()

        st.success("🔥 Entreno guardado")

# -------- HISTORIAL --------
elif menu == "📅 Historial":

    st.header("📅 Historial")

    historial = user.get("historial")

    if historial:
        df = pd.DataFrame(historial)
        st.dataframe(df)
    else:
        st.info("Sin datos")

# -------- PROGRESO --------
elif menu == "📊 Progreso":

    st.header("📊 Progreso")

    historial = user.get("historial")

    if historial:
        df = pd.DataFrame(historial)
        ejercicio = st.selectbox("Ejercicio", df["ejercicio"].unique())
        df_f = df[df["ejercicio"] == ejercicio]

        st.line_chart(df_f["peso"])
    else:
        st.info("No hay datos")

# -------- DIETA --------
elif menu == "🍽️ Dieta":

    st.header("🍽️ Dieta")

    st.subheader("Desayuno (500 kcal)")
    st.write("Pan 100g | Jamón 50g | Tomate | Aceite | Fruta")

    st.subheader("Comida (850 kcal)")
    st.write("Arroz 85g | Pollo 150g | Verduras")

    st.subheader("Cena (800 kcal)")
    st.write("Pasta 120g | Pollo 200g")

    st.success("🔥 Total: 2150 kcal")
