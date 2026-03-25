import streamlit as st

st.title("💪 Mi Rutina Personal")

dia = st.selectbox(
    "Selecciona el día",
    ["Día 1", "Día 2", "Día 3", "Día 4"]
)

st.subheader("🏋️ Rutina")

if dia == "Día 1":
    rutina = [
        "Press inclinado Smith 3x6-8",
        "Press convergente 3x10-12",
        "Aperturas 3x10-12",
        "Laterales 4x12-15",
        "Fondos 4x8-12"
    ]

elif dia == "Día 2":
    rutina = [
        "Remo barra 4 series",
        "Dominadas 4x6-8",
        "Remo mancuerna 3 series",
        "Remo inclinado 3 series",
        "Pájaros 3 series",
        "Curl predicador 3 series",
        "Curl martillo 2 series"
    ]

elif dia == "Día 3":
    rutina = [
        "Sentadilla 5 series",
        "Prensa 3 series",
        "Curl femoral 3 series",
        "Extensión 3 series",
        "Peso muerto rumano 3 series",
        "Gemelos 4 series"
    ]

else:
    rutina = [
        "Press inclinado Smith",
        "Aperturas",
        "Press máquina",
        "Press militar",
        "Laterales",
        "Skull crushers",
        "Press cerrado"
    ]

# checkboxes
completados = 0

for ejercicio in rutina:
    hecho = st.checkbox(ejercicio)
    if hecho:
        completados += 1

st.write(f"Progreso: {completados}/{len(rutina)}")

if completados == len(rutina):
    st.success("🔥 Entrenamiento completado 💪")
