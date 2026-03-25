import streamlit as st
import time
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="APOLLO FITNESS", page_icon="💪", layout="centered")

st.title("🚀 APOLLO FITNESS")

# 👤 LOGIN SIMPLE
if "usuario" not in st.session_state:
    usuario = st.text_input("Introduce tu nombre")
    if st.button("Entrar"):
        st.session_state.usuario = usuario
        st.success(f"Bienvenido {usuario}")
        st.rerun()
    st.stop()

st.write(f"👤 {st.session_state.usuario}")

# 📱 MENÚ MÓVIL
menu = st.radio(
    "Navegación",
    ["🏋️ Entreno", "📊 Progreso", "📅 Historial", "🍽️ Dieta"],
    horizontal=True
)

# DATOS
rutinas = {
    "Día 1": [("Press inclinado Smith", "pesado"), ("Press convergente", "hipertrofia"), ("Aperturas", "aislamiento"), ("Laterales", "aislamiento"), ("Fondos", "pesado")],
    "Día 2": [("Remo barra", "pesado"), ("Dominadas", "pesado"), ("Remo mancuerna", "hipertrofia"), ("Remo inclinado", "hipertrofia"), ("Pájaros", "aislamiento"), ("Curl predicador", "hipertrofia"), ("Curl martillo", "aislamiento")],
    "Día 3": [("Sentadilla", "pesado"), ("Prensa", "hipertrofia"), ("Curl femoral", "aislamiento"), ("Extensión", "aislamiento"), ("Peso muerto rumano", "hipertrofia"), ("Gemelos", "aislamiento")],
    "Día 4": [("Press inclinado", "pesado"), ("Aperturas", "aislamiento"), ("Press máquina", "hipertrofia"), ("Press militar", "pesado"), ("Laterales", "aislamiento"), ("Skull crushers", "hipertrofia"), ("Press cerrado", "pesado")]
}

descansos = {"pesado": 90, "hipertrofia": 60, "aislamiento": 45}

# 🍽️ DIETA (EDITA AQUÍ CON TU PLAN)
dietas = {
    "Día 1": ["Desayuno: Avena + proteína", "Comida: Pollo + arroz", "Cena: Tortilla + ensalada"],
    "Día 2": ["Desayuno: Yogur + fruta", "Comida: Carne + patata", "Cena: Pescado + verduras"],
    "Día 3": ["Desayuno: Tostadas + huevos", "Comida: Pasta + pollo", "Cena: Ensalada + atún"],
    "Día 4": ["Desayuno: Batido", "Comida: Arroz + carne", "Cena: Verduras + pollo"]
}

# estado
if "historial" not in st.session_state:
    st.session_state.historial = []

# 🏋️ ENTRENAMIENTO
if menu == "🏋️ Entreno":

    dia = st.selectbox("Día", ["Día 1", "Día 2", "Día 3", "Día 4"])
    rutina = rutinas[dia]

    completados = 0
    pesos_registro = []

    for ejercicio, tipo in rutina:
        st.markdown(f"### {ejercicio}")

        peso = st.number_input(f"{ejercicio} (kg)", min_value=0.0, step=2.5, key=ejercicio+"_peso")
        hecho = st.checkbox(f"✔️ {ejercicio}", key=ejercicio+"_check")

        if hecho:
            completados += 1
            pesos_registro.append({"ejercicio": ejercicio, "peso": peso})

            if st.button(f"Descanso {ejercicio}", key=ejercicio+"_btn"):
                for i in range(descansos[tipo], 0, -1):
                    st.write(f"{i}s")
                    time.sleep(1)

    st.progress(completados / len(rutina))

    if completados == len(rutina):
        if st.button("💾 Guardar"):
            fecha = datetime.now().strftime("%Y-%m-%d")

            for item in pesos_registro:
                st.session_state.historial.append({
                    "fecha": fecha,
                    "ejercicio": item["ejercicio"],
                    "peso": item["peso"]
                })

            st.success("Guardado 🔥")

# 📊 PROGRESO
elif menu == "📊 Progreso":

    if st.session_state.historial:
        df = pd.DataFrame(st.session_state.historial)

        ejercicio = st.selectbox("Ejercicio", df["ejercicio"].unique())
        df_f = df[df["ejercicio"] == ejercicio]

        st.line_chart(df_f.set_index("fecha")["peso"])
    else:
        st.write("Sin datos")

# 📅 HISTORIAL
elif menu == "📅 Historial":

    if st.session_state.historial:
        st.dataframe(pd.DataFrame(st.session_state.historial))
    else:
        st.write("Vacío")

# 🍽️ DIETA
elif menu == "🍽️ Dieta":

    dia = st.selectbox("Día dieta", ["Día 1", "Día 2", "Día 3", "Día 4"])

    for comida in dietas[dia]:
        st.write("👉", comida)
