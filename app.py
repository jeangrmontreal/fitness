import streamlit as st

st.title("💪 Mi Fitness App")

st.write("Rutina simple para perder grasa y mantenerte activo")

objetivo = st.selectbox(
    "¿Cuál es tu objetivo?",
    ["Perder grasa", "Mantenerte", "Ganar fuerza"]
)

st.subheader("🔥 Rutina de hoy")

if objetivo == "Perder grasa":
    rutina = [
        "Flexiones — 3 x 10",
        "Sentadillas — 3 x 15",
        "Plancha — 30 segundos",
        "Burpees — 3 x 8"
    ]
elif objetivo == "Mantenerte":
    rutina = [
        "Flexiones — 3 x 8",
        "Sentadillas — 3 x 10",
        "Plancha — 20 segundos"
    ]
else:
    rutina = [
        "Flexiones — 4 x 12",
        "Sentadillas — 4 x 20",
        "Plancha — 40 segundos",
        "Zancadas — 3 x 12"
    ]

for ejercicio in rutina:
    st.write("👉", ejercicio)

if st.button("✅ Rutina completada"):
    st.success("¡Bien hecho! 💪 Sigue así")
