import streamlit as st
import time
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="APOLLO FITNESS", page_icon="💪", layout="centered")

# 🌑 ESTILO NEGRO PRO
st.markdown("""
<style>
body {
    background-color: #000000;
    color: white;
}
.block-container {
    padding-top: 1rem;
}
.card {
    background-color: #111111;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    border: 1px solid #222;
}
.title {
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
}
button {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 APOLLO FITNESS</div>', unsafe_allow_html=True)

dia = st.selectbox("📅 Día", ["Día 1", "Día 2", "Día 3", "Día 4"])

rutinas = {
    "Día 1": [("Press inclinado Smith", "pesado"), ("Press convergente", "hipertrofia"), ("Aperturas", "aislamiento"), ("Laterales", "aislamiento"), ("Fondos", "pesado")],
    "Día 2": [("Remo barra", "pesado"), ("Dominadas", "pesado"), ("Remo mancuerna", "hipertrofia"), ("Remo inclinado", "hipertrofia"), ("Pájaros", "aislamiento"), ("Curl predicador", "hipertrofia"), ("Curl martillo", "aislamiento")],
    "Día 3": [("Sentadilla", "pesado"), ("Prensa", "hipertrofia"), ("Curl femoral", "aislamiento"), ("Extensión", "aislamiento"), ("Peso muerto rumano", "hipertrofia"), ("Gemelos", "aislamiento")],
    "Día 4": [("Press inclinado", "pesado"), ("Aperturas", "aislamiento"), ("Press máquina", "hipertrofia"), ("Press militar", "pesado"), ("Laterales", "aislamiento"), ("Skull crushers", "hipertrofia"), ("Press cerrado", "pesado")]
}

descansos = {"pesado": 90, "hipertrofia": 60, "aislamiento": 45}

if "historial" not in st.session_state:
    st.session_state.historial = []

rutina = rutinas[dia]

st.subheader("🏋️ Entrenamiento")

completados = 0
pesos_registro = []

for ejercicio, tipo in rutina:
    st.markdown(f'<div class="card">💪 {ejercicio} ({tipo})</div>', unsafe_allow_html=True)

    peso = st.number_input(f"Peso (kg) - {ejercicio}", min_value=0.0, step=2.5, key=ejercicio+"_peso")

    hecho = st.checkbox(f"✔️ {ejercicio}", key=ejercicio+"_check")

    if hecho:
        completados += 1
        pesos_registro.append({"ejercicio": ejercicio, "peso": peso})

        if st.button(f"⏱️ Descanso {ejercicio}", key=ejercicio+"_btn"):
            for i in range(descansos[tipo], 0, -1):
                st.write(f"{i}s")
                time.sleep(1)
            st.success("🔥 Vamos al siguiente")

st.write(f"📊 {completados}/{len(rutina)}")
st.progress(completados / len(rutina))

if completados == len(rutina):
    if st.button("💾 Guardar"):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        for item in pesos_registro:
            st.session_state.historial.append({
                "fecha": fecha,
                "ejercicio": item["ejercicio"],
                "peso": item["peso"]
            })
        st.success("Guardado 🚀")

# historial + gráfico
st.subheader("📈 Progreso")

if st.session_state.historial:
    df = pd.DataFrame(st.session_state.historial)
    st.dataframe(df)

    ejercicio_sel = st.selectbox("Ejercicio", df["ejercicio"].unique())
    df_f = df[df["ejercicio"] == ejercicio_sel]

    st.line_chart(df_f.set_index("fecha")["peso"])
