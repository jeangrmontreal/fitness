import streamlit as st

st.title("💪 Mi Rutina Personal")

dia = st.selectbox(
    "Selecciona el día",
    ["Día 1", "Día 2", "Día 3", "Día 4"]
)

st.subheader("🏋️ Rutina")

if dia == "Día 1":
    rutina = [
        "Press de banca inclinado en Smith: 3x6-8",
        "Press convergente: 3x10-12",
        "Aperturas en contractora: 3x10-12",
        "Elevaciones laterales: 4x12-15",
        "Fondos en paralelas: 4x8-12"
    ]

elif dia == "Día 2":
    rutina = [
        "Remo con barra: 4x12/10/10/8",
        "Dominadas: 4x6-8",
        "Remo con mancuerna: 3x12/10/8",
        "Remo en banco inclinado: 3x10-12",
        "Pájaros con mancuernas: 3x10-12",
        "Curl predicador: 3x10-12",
        "Curl martillo: 2x10-8"
    ]

elif dia == "Día 3":
    rutina = [
        "Sentadillas: 2x6 + 3x10",
        "Prensa: 3x8-10",
        "Curl femoral: 3x10",
        "Extensión de cuádriceps: 3x10",
        "Peso muerto rumano: 3x10-12",
        "Gemelos en Smith: 4x10-15"
    ]

elif dia == "Día 4":
    rutina = [
        "Press inclinado en Smith: 3x8/6/6",
        "Aperturas en contractora: 3x10-12",
        "Press inclinado en máquina: 3x10-12",
        "Press militar: 2x8",
        "Elevaciones laterales: 3x10-12",
        "Skull crushers: 4x8-10",
        "Press cerrado: 4x8-10"
    ]

for ejercicio in rutina:
    st.write("👉", ejercicio)

if st.button("✅ Entrenamiento completado"):
    st.success("Buen trabajo 💪🔥")
