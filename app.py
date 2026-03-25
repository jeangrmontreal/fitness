import streamlit as st
import time

st.title("💪 Mi Rutina Personal")

dia = st.selectbox(
    "Selecciona el día",
    ["Día 1", "Día 2", "Día 3", "Día 4"]
)

st.subheader("🏋️ Rutina")

# Rutinas
rutinas = {
    "Día 1": [
        "Press inclinado Smith",
        "Press convergente",
        "Aperturas",
        "Laterales",
        "Fondos"
    ],
    "Día 2": [
        "Remo barra",
        "Dominadas",
        "Remo mancuerna",
        "Remo inclinado",
        "Pájaros",
        "Curl predicador",
        "Curl martillo"
    ],
    "Día 3": [
        "Sentadilla",
        "Prensa",
        "Curl femoral",
        "Extensión",
        "Peso muerto rumano",
        "Gemelos"
    ],
    "Día 4": [
        "Press inclinado",
        "Aperturas",
        "Press máquina",
        "Press militar",
        "Laterales",
        "Skull crushers",
        "Press cerrado"
    ]
}

rutina = rutinas[dia]

# Estado guardado
if "progreso" not in st.session_state:
    st.session_state.progreso = {}

completados = 0

for ejercicio in rutina:
    key = f"{dia}_{ejercicio}"
    estado = st.checkbox(ejercicio, key=key)

    if estado:
        completados += 1

# Progreso
st.write(f"📊 Progreso: {completados}/{len(rutina)}")

st.progress(completados / len(rutina))

if completados == len(rutina):
    st.success("🔥 Entrenamiento completado 💪")

# ⏱️ Temporizador simple
st.subheader("⏱️ Temporizador descanso")

if st.button("Iniciar 30 segundos"):
    for i in range(30, 0, -1):
        st.write(f"⏳ {i} segundos")
        time.sleep(1)
    st.success("¡Descanso terminado!")")
