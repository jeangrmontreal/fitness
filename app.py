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

# -------- DARK MODE --------
st.markdown("""
<style>
body {background-color: #0e1117; color: white;}
</style>
""", unsafe_allow_html=True)

st.title("🚀 APOLLO PRO")

# -------- TIMER --------
if "timer" not in st.session_state:
    st.session_state.timer = 0

timer_placeholder = st.empty()

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

# -------- ROLES --------
if "rol" not in st.session_state:
    st.session_state.rol = "cliente"

rol = st.sidebar.selectbox("Modo", ["cliente", "entrenador"])

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
if rol == "entrenador":

    st.header("👥 Clientes")

    res = supabase.table("usuarios").select("*").execute()

    nombres = [u["nombre"] for u in res.data]

    cliente = st.selectbox("Selecciona cliente", nombres)

    user = next(u for u in res.data if u["nombre"] == cliente)

    st.write(f"Viendo a: {cliente}")

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
            st.session_state.timer = 30

        registro.append({
            "ejercicio": ej,
            "peso": float(peso),
            "series": series,
            "reps": reps
        })

    if st.session_state.timer > 0:
        timer_placeholder.markdown(f"## ⏳ {st.session_state.timer}s")
        time.sleep(1)
        st.session_state.timer -= 1
        st.rerun()

    if st.button("💾 Guardar entreno"):

        historial = user.get("historial")
        if not isinstance(historial, list):
            historial = []

        for r in registro:
            r["fecha"] = datetime.now().strftime("%Y-%m-%d")
            r["tipo"] = "entreno"
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
        df = df[df["tipo"] == "entreno"]

        if not df.empty:
            ejercicio = st.selectbox("Ejercicio", df["ejercicio"].unique())
            df_f = df[df["ejercicio"] == ejercicio]

            st.line_chart(df_f["peso"])
        else:
            st.info("Sin entrenos")

# -------- DIETA (FIX TOTAL) --------
elif menu == "🍽️ Dieta":

    st.header("🍽️ Dieta diaria")

    dieta = {
        "Desayuno": {
            "Tostada jamón": 500,
            "Huevos + guacamole": 500,
            "Tortitas avena": 500,
            "Leche + cereales": 500
        },
        "Comida": {
            "Patata + atún": 850,
            "Arroz + pollo": 850,
            "Pasta + carne": 850,
            "Macarrones + salmón": 850
        },
        "Cena": {
            "Pasta + pollo": 800,
            "Merluza + patata": 800,
            "Arroz + atún": 800,
            "Pavo + quinoa": 800
        }
    }

    total_calorias = 0
    seleccion = {}

    for comida, opciones in dieta.items():
        st.subheader(comida)

        opcion = st.selectbox(comida, list(opciones.keys()), key=comida)
        calorias = int(opciones[opcion])

        st.write(f"🔥 {calorias} kcal")

        seleccion[comida] = {
            "opcion": opcion,
            "calorias": calorias
        }

        total_calorias += calorias

    st.markdown("---")
    st.success(f"🔥 TOTAL: {total_calorias} kcal")

    if st.button("💾 Guardar dieta"):

        historial = user.get("historial")
        if not isinstance(historial, list):
            historial = []

        registro_dieta = {
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "tipo": "dieta",
            "comidas": seleccion,
            "total_kcal": int(total_calorias)
        }

        historial.append(registro_dieta)

        supabase.table("usuarios").update({
            "historial": historial
        }).eq("id", user["id"]).execute()

        st.success("✅ Dieta guardada PERFECTA")
