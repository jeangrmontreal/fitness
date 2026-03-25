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

# MENÚ
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

            # 🔥 TEMPORIZADOR FIX
            if st.button("Descanso", key=f"btn_{i}"):
                timer = st.empty()
                for t in range(30, 0, -1):
                    timer.markdown(f"## ⏳ {t} s")
                    time.sleep(1)
                timer.markdown("## ✅ Listo")

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

# ---------------- DIETA PRO ----------------
elif menu == "🍽️ Dieta":

    st.header("🍽️ Dieta")

    comida = st.selectbox("Selecciona comida", ["Comida 1", "Comida 2", "Comida 3"])

    # COMIDA 1
    if comida == "Comida 1":

        opcion = st.radio("Opciones", [
            "Tostada jamón",
            "Tostada huevos",
            "Tortitas avena",
            "Leche + cereales"
        ])

        if opcion == "Tostada jamón":
            st.write("Pan integral 100g")
            st.write("Jamón serrano 50g")
            st.write("Tomate 50g")
            st.write("Aceite 8ml")
            st.write("Fruta 1 pieza")

        elif opcion == "Tostada huevos":
            st.write("Pan 100g")
            st.write("Huevo 100g")
            st.write("Guacamole 20g")

        elif opcion == "Tortitas avena":
            st.write("Avena 50g")
            st.write("Huevo 60g")
            st.write("Claras 80g")
            st.write("Plátano 100g")

        else:
            st.write("Leche 300g")
            st.write("Corn flakes 50g")
            st.write("Cacao 10g")

        st.success("🔥 500 kcal")

    # COMIDA 2
    elif comida == "Comida 2":

        opcion = st.radio("Opciones", [
            "Patata + atún",
            "Arroz + pollo",
            "Pasta + carne",
            "Macarrones + salmón"
        ])

        if opcion == "Patata + atún":
            st.write("Patata 300g")
            st.write("Atún 160g")
            st.write("Huevo 120g")

        elif opcion == "Arroz + pollo":
            st.write("Arroz 85g")
            st.write("Pollo 150g")

        elif opcion == "Pasta + carne":
            st.write("Pasta 100g")
            st.write("Carne 200g")

        else:
            st.write("Macarrones 100g")
            st.write("Salmón 220g")

        st.success("🔥 850 kcal")

    # COMIDA 3
    else:

        opcion = st.radio("Opciones", [
            "Pasta + pollo",
            "Merluza + patata",
            "Arroz + atún",
            "Pavo + quinoa"
        ])

        if opcion == "Pasta + pollo":
            st.write("Pasta 120g")
            st.write("Pollo 200g")

        elif opcion == "Merluza + patata":
            st.write("Patata 300g")
            st.write("Merluza 200g")

        elif opcion == "Arroz + atún":
            st.write("Arroz 120g")
            st.write("Atún 160g")

        else:
            st.write("Quinoa 120g")
            st.write("Pavo 200g")

        st.success("🔥 800 kcal")

    st.markdown("---")
    st.write("🔥 Total: 2150 kcal")
    st.write("💧 Agua: 3–4L")
    st.write("⚡ Creatina: 7g")

# ---------------- PESO ----------------
elif menu == "⚖️ Peso":

    st.header("⚖️ Peso")

    peso = st.number_input("Peso actual", min_value=40.0, max_value=150.0)
    objetivo = st.number_input("Objetivo", min_value=40.0, max_value=150.0)

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
