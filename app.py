import streamlit as st
import time
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="APOLLO FITNESS", page_icon="💪", layout="centered")

# 🎨 ESTILO
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
}
h1, h2, h3 {
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 APOLLO FITNESS")

# 👤 LOGIN
if "usuario" not in st.session_state:
    usuario = st.text_input("👤 Tu nombre")
    if st.button("Entrar"):
        st.session_state.usuario = usuario
        st.rerun()
    st.stop()

st.sidebar.write(f"👤 {st.session_state.usuario}")

# 📱 MENÚ LATERAL
menu = st.sidebar.radio(
    "Menú",
    ["🏋️ Entrenamiento", "📊 Progreso", "📅 Historial", "🍽️ Dieta"]
)

# DATOS
rutinas = {
    "Día 1": [("Press inclinado Smith", "pesado"), ("Press convergente", "hipertrofia"), ("Aperturas", "aislamiento"), ("Laterales", "aislamiento"), ("Fondos", "pesado")],
    "Día 2": [("Remo barra", "pesado"), ("Dominadas", "pesado"), ("Remo mancuerna", "hipertrofia"), ("Remo inclinado", "hipertrofia"), ("Pájaros", "aislamiento"), ("Curl predicador", "hipertrofia"), ("Curl martillo", "aislamiento")],
    "Día 3": [("Sentadilla", "pesado"), ("Prensa", "hipertrofia"), ("Curl femoral", "aislamiento"), ("Extensión", "aislamiento"), ("Peso muerto rumano", "hipertrofia"), ("Gemelos", "aislamiento")],
    "Día 4": [("Press inclinado", "pesado"), ("Aperturas", "aislamiento"), ("Press máquina", "hipertrofia"), ("Press militar", "pesado"), ("Laterales", "aislamiento"), ("Skull crushers", "hipertrofia"), ("Press cerrado", "pesado")]
}

descansos = {"pesado": 90, "hipertrofia": 60, "aislamiento": 45}

if "historial" not in st.session_state:
    st.session_state.historial = []

# 🏋️ ENTRENAMIENTO
if menu == "🏋️ Entrenamiento":

    st.header("🏋️ Entrenamiento")

    dia = st.selectbox("Selecciona tu día", ["Día 1", "Día 2", "Día 3", "Día 4"])
    rutina = rutinas[dia]

    completados = 0
    pesos_registro = []

    for ejercicio, tipo in rutina:
        with st.container():
            st.subheader(ejercicio)

            peso = st.number_input(f"Peso (kg)", min_value=0.0, step=2.5, key=ejercicio+"_peso")
            hecho = st.checkbox("Completar", key=ejercicio+"_check")

            if hecho:
                completados += 1
                pesos_registro.append({"ejercicio": ejercicio, "peso": peso})

                if st.button("Descanso", key=ejercicio+"_btn"):
                    for i in range(descansos[tipo], 0, -1):
                        st.write(f"{i}s")
                        time.sleep(1)

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

# 📊 PROGRESO
elif menu == "📊 Progreso":

    st.header("📊 Progreso")

    if st.session_state.historial:
        df = pd.DataFrame(st.session_state.historial)

        ejercicio = st.selectbox("Ejercicio", df["ejercicio"].unique())
        df_f = df[df["ejercicio"] == ejercicio]

        st.line_chart(df_f.set_index("fecha")["peso"])
    else:
        st.info("Aún no hay datos")

# 📅 HISTORIAL
elif menu == "📅 Historial":

    st.header("📅 Historial")

    if st.session_state.historial:
        st.dataframe(pd.DataFrame(st.session_state.historial))
    else:
        st.info("No hay entrenamientos guardados")

# 🍽️ DIETA
elif menu == "🍽️ Dieta":

    st.header("🍽️ Dieta")

    comida = st.selectbox("Comida", ["Comida 1", "Comida 2", "Comida 3"])

    if comida == "Comida 1":
        opciones = [
            "Tostada integral + jamón + tomate + aceite + fruta",
            "Tostada integral + huevos + guacamole + fruta",
            "Tortitas avena + chocolate + fresas",
            "Leche + corn flakes + cacao + fruta"
        ]
        kcal = "500 kcal"

    elif comida == "Comida 2":
        opciones = [
            "Ensalada patata + atún + huevo",
            "Arroz + pollo + champiñones",
            "Espaguetis + carne + tomate",
            "Macarrones + salmón + verduras"
        ]
        kcal = "850 kcal"

    else:
        opciones = [
            "Pasta + pollo + tomate",
            "Merluza + puré de patata",
            "Arroz + atún + verduras",
            "Pavo + quinoa + judías"
        ]
        kcal = "800 kcal"

    st.radio("Opciones", opciones)
    st.write(f"🔥 {kcal}")

    st.markdown("---")
    st.write("🔥 Total diario: 2150 kcal")
    st.write("💧 Agua: 3–4L")
    st.write("⚡ Creatina: 7g")

    if st.button("✅ Día completado"):
        st.success("Dieta cumplida 💪")
