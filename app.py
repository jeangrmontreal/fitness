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

# -------- TIMER --------
if "timer" not in st.session_state:
    st.session_state.timer = 0

timer_placeholder = st.empty()

# -------- LOGIN --------
if "usuario" not in st.session_state:
    st.session_state.usuario = None
    st.session_state.rol = None

if not st.session_state.usuario:
    nombre = st.text_input("👤 Nombre")
    codigo = st.text_input("🔑 Código", type="password")

    if st.button("Entrar"):
        if codigo == "apollo123":
            st.session_state.usuario = "ENTRENADOR"
            st.session_state.rol = "entrenador"
        else:
            st.session_state.usuario = nombre.strip()
            st.session_state.rol = "cliente"
        st.rerun()
    st.stop()

usuario = st.session_state.usuario
rol = st.session_state.rol

st.sidebar.write(f"👤 {usuario}")
st.sidebar.write(f"Rol: {rol}")

# -------- USER --------
if rol == "entrenador":
    res = supabase.table("usuarios").select("*").execute()
    nombres = [u["nombre"] for u in res.data if u["nombre"] != "ENTRENADOR"]

    cliente = st.sidebar.selectbox("Cliente", nombres)
    user = next(u for u in res.data if u["nombre"] == cliente)
else:
    res = supabase.table("usuarios").select("*").eq("nombre", usuario).execute()

    if not res.data:
        supabase.table("usuarios").insert({
            "nombre": usuario,
            "historial": [],
            "pesos": [],
            "rutina": [],
            "dieta_admin": ""
        }).execute()

        res = supabase.table("usuarios").select("*").eq("nombre", usuario).execute()

    user = res.data[0]

# -------- MENU --------
menu = st.sidebar.radio("Menú", [
    "🏋️ Entreno",
    "📊 Progreso",
    "📅 Historial",
    "🍽️ Dieta",
    "👑 Admin"
])

# -------- ENTRENAMIENTO --------
if menu == "🏋️ Entreno":

    st.header("🏋️ Tu rutina")

    rutina = user.get("rutina")

    if rutina:
        registro = []

        for i, r in enumerate(rutina):

            st.subheader(r["ejercicio"])

            col1, col2, col3 = st.columns(3)

            with col1:
                series = st.number_input("Series", 1, 10, r["series"], key=f"s{i}")
            with col2:
                reps = st.number_input("Reps", 1, 20, r["reps"], key=f"r{i}")
            with col3:
                peso = st.number_input("Peso", 0.0, step=2.5, key=f"p{i}")

            if st.button("⏱️ Descanso", key=f"t{i}"):
                st.session_state.timer = 30

            registro.append({
                "ejercicio": r["ejercicio"],
                "series": series,
                "reps": reps,
                "peso": float(peso)
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

    else:
        st.warning("Tu entrenador aún no te asignó rutina")

# -------- HISTORIAL --------
elif menu == "📅 Historial":

    historial = user.get("historial")

    if historial:
        st.dataframe(pd.DataFrame(historial))

# -------- PROGRESO --------
elif menu == "📊 Progreso":

    historial = user.get("historial")

    if historial:
        df = pd.DataFrame(historial)
        df = df[df["tipo"] == "entreno"]

        if not df.empty:
            ej = st.selectbox("Ejercicio", df["ejercicio"].unique())
            st.line_chart(df[df["ejercicio"] == ej]["peso"])

# -------- DIETA CLIENTE --------
elif menu == "🍽️ Dieta":

    st.header("🍽️ Tu dieta")

    dieta = user.get("dieta_admin")

    if dieta:
        st.write(dieta)
    else:
        st.warning("Tu entrenador no te asignó dieta")

# -------- ADMIN --------
elif menu == "👑 Admin":

    if rol != "entrenador":
        st.warning("No tienes acceso")
        st.stop()

    st.header("👑 Panel Admin")

    # -------- RUTINA --------
    st.subheader("🏋️ Crear rutina")

    ejercicios = ["Press banca", "Sentadilla", "Dominadas"]

    rutina = []

    for i, ej in enumerate(ejercicios):

        col1, col2 = st.columns(2)

        with col1:
            series = st.number_input(f"Series {ej}", 1, 10, 3, key=f"as{i}")
        with col2:
            reps = st.number_input(f"Reps {ej}", 1, 20, 10, key=f"ar{i}")

        rutina.append({
            "ejercicio": ej,
            "series": series,
            "reps": reps
        })

    if st.button("💾 Guardar rutina"):

        supabase.table("usuarios").update({
            "rutina": rutina
        }).eq("id", user["id"]).execute()

        st.success("Rutina asignada 🔥")

    # -------- DIETA --------
    st.subheader("🍽️ Asignar dieta")

    dieta_admin = st.text_area("Dieta personalizada")

    if st.button("💾 Guardar dieta"):

        supabase.table("usuarios").update({
            "dieta_admin": dieta_admin
        }).eq("id", user["id"]).execute()

        st.success("Dieta asignada 🔥")
