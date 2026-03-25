import streamlit as st
import time

st.set_page_config(page_title="Fitness PRO MAX", page_icon="💪", layout="centered")

# 🎨 estilo
st.markdown("""
<style>
body { background-color: #0f172a; }
.card {
    background-color: #1e293b;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 8px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("💪 Fitness PRO MAX")

dia = st.selectbox("Selecciona tu día", ["Día 1", "Día 2", "Día 3", "Día 4"])

# 🧠 ejercicios + tipo
rutinas = {
    "Día 1": [
        ("Press inclinado Smith", "pesado"),
        ("Press convergente", "hipertrofia"),
        ("Aperturas", "aislamiento"),
        ("Laterales", "aislamiento"),
        ("Fondos", "pesado"),
    ],
    "Día 2": [
        ("Remo barra", "pesado"),
        ("Dominadas", "pesado"),
        ("Remo mancuerna", "hipertrofia"),
        ("Remo inclinado", "hipertrofia"),
        ("Pájaros", "aislamiento"),
        ("Curl predicador", "hipertrofia"),
        ("Curl martillo", "aislamiento"),
    ],
    "Día 3": [
        ("Sentadilla", "pesado"),
        ("Prensa", "hipertrofia"),
        ("Curl femoral", "aislamiento"),
        ("Extensión", "aislamiento"),
        ("Peso muerto rumano", "hipertrofia"),
        ("Gemelos", "aislamiento"),
    ],
    "Día 4": [
        ("Press inclinado", "pesado"),
        ("Aperturas", "aislamiento"),
        ("Press máquina", "hipertrofia"),
        ("Press militar", "pesado"),
        ("Laterales", "aislamiento"),
        ("Skull crushers", "hipertrofia"),
        ("Press cerrado", "pesado"),
    ]
}

# ⏱️ descanso recomendado
descansos = {
    "pesado": 90,
    "hipertrofia": 60,
    "aislamiento": 45
}

rutina = rutinas[dia]

st.subheader("🏋️ Entrenamiento")

completados = 0

for ejercicio, tipo in rutina:
    st.markdown(f'<div class="card">{ejercicio} ({tipo})</div>', unsafe_allow_html=True)
    if st.checkbox(f"Completar {ejercicio}", key=ejercicio):
        completados += 1

        tiempo = descansos[tipo]

        if st.button(f"Descanso recomendado {ejercicio}"):
            for i in range(tiempo, 0, -1):
                st.write(f"⏳ {i} segundos")
                time.sleep(1)
            st.success("🔥 Sigue con el siguiente ejercicio")

# progreso
st.write(f"Progreso: {completados}/{len(rutina)}")
st.progress(completados / len(rutina))

if completados == len(rutina):
    st.success("🏆 Entrenamiento completo PRO")
