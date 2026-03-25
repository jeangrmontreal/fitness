import streamlit as st
import time
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="APOLLO FITNESS", page_icon="💪", layout="centered")

st.title("🚀 APOLLO FITNESS")

# seleccionar día
dia = st.selectbox("Selecciona tu día", ["Día 1", "Día 2", "Día 3", "Día 4"])

# rutinas
rutinas = {
    "Día 1": [("Press inclinado Smith", "pesado"), ("Press convergente", "hipertrofia"), ("Aperturas", "aislamiento"), ("Laterales", "aislamiento"), ("Fondos", "pesado")],
    "Día 2": [("Remo barra", "pesado"), ("Dominadas", "pesado"), ("Remo mancuerna", "hipertrofia"), ("Remo inclinado", "hipertrofia"), ("Pájaros", "aislamiento"), ("Curl predicador", "hipertrofia"), ("Curl martillo", "aislamiento")],
    "Día 3": [("Sentadilla", "pesado"), ("Prensa", "hipertrofia"), ("Curl femoral", "aislamiento"), ("Extensión", "aislamiento"), ("Peso muerto rumano", "hipertrofia"), ("Gemelos", "aislamiento")],
    "Día 4": [("Press inclinado", "pesado"), ("Aperturas", "aislamiento"), ("Press máquina", "hipertrofia"), ("Press militar", "pesado"), ("Laterales", "aislamiento"), ("Skull crushers", "hipertrofia"), ("Press cerrado", "pesado")]
}

descansos = {"pesado": 90, "hipertrofia": 60, "aislamiento": 45}

# guardar datos
if "historial" not in st.session_state:
    st.session_state.historial = []

rutina = rutinas[dia]

st.subheader("🏋️ Entrenamiento")

completados = 0
pesos_registro = []

for ejercicio, tipo in rutina:
    st.markdown(f"### {ejercicio} ({tipo})")

    peso = st.number_input(f"Peso en {ejercicio} (kg)", min_value=0.0, step=2.5, key=ejercicio+"_peso")

    hecho = st.checkbox(f"Completar {ejercicio}", key=ejercicio+"_check")

    if hecho:
        completados += 1
        pesos_registro.append({"ejercicio": ejercicio, "peso": peso})

        tiempo = descansos[tipo]

        if st.button(f"Descanso {ejercicio}", key=ejercicio+"_btn"):
            for i in range(tiempo, 0, -1):
                st.write(f"⏳ {i} s")
                time.sleep(1)
            st.success("🔥 Sigue")

# progreso
st.write(f"📊 Progreso: {completados}/{len(rutina)}")
st.progress(completados / len(rutina))

# guardar entrenamiento
if completados == len(rutina):
    if st.button("💾 Guardar entrenamiento"):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

        for item in pesos_registro:
            st.session_state.historial.append({
                "fecha": fecha,
                "dia": dia,
                "ejercicio": item["ejercicio"],
                "peso": item["peso"]
            })

        st.success("Entrenamiento guardado 🚀")

# historial
st.subheader("📅 Historial")

if st.session_state.historial:
    df = pd.DataFrame(st.session_state.historial)
    st.dataframe(df)

    # gráfico
    st.subheader("📈 Progreso de pesos")

    ejercicio_unico = st.selectbox(
        "Selecciona ejercicio para ver progreso",
        df["ejercicio"].unique()
    )

    df_filtrado = df[df["ejercicio"] == ejercicio_unico]

    st.line_chart(df_filtrado.set_index("fecha")["peso"])
else:
    st.write("Aún no hay datos")
