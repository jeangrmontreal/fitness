import streamlit as st
import time

st.set_page_config(page_title="Fitness Pro", page_icon="💪", layout="centered")

# 🎨 Estilo visual
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.card {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.title {
    font-size: 28px;
    font-weight: bold;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💪 Mi Fitness App PRO</div>', unsafe_allow_html=True)

dia = st.selectbox(
    "Selecciona tu día",
    ["Día 1", "Día 2", "Día 3", "Día 4"]
)

rutinas = {
    "Día 1": ["Press inclinado Smith", "Press convergente", "Aperturas", "Laterales", "Fondos"],
    "Día 2": ["Remo barra", "Dominadas", "Remo mancuerna", "Remo inclinado", "Pájaros", "Curl predicador", "Curl martillo"],
    "Día 3": ["Sentadilla", "Prensa", "Curl femoral", "Extensión", "Peso muerto rumano", "Gemelos"],
    "Día 4": ["Press inclinado", "Aperturas", "Press máquina", "Press militar", "Laterales", "Skull crushers", "Press cerrado"]
}

st.subheader("🏋️ Entrenamiento")

rutina = rutinas[dia]

if "progreso" not in st.session_state:
    st.session_state.progreso = {}

completados = 0

for ejercicio in rutina:
    key = f"{dia}_{ejercicio}"
    st.markdown(f'<div class="card">{ejercicio}</div>', unsafe_allow_html=True)
    estado = st.checkbox(f"Completar {ejercicio}", key=key)

    if estado:
        completados += 1

# 📊 progreso
st.write(f"Progreso: {completados}/{len(rutina)}")
st.progress(completados / len(rutina))

if completados == len(rutina):
    st.success("🔥 Entrenamiento completado 💪")

# ⏱️ temporizador
st.subheader("⏱️ Descanso")

if st.button("Descanso 30s"):
    for i in range(30, 0, -1):
        st.write(f"{i} segundos")
        time.sleep(1)
    st.success("¡Listo! Sigue 💪")
