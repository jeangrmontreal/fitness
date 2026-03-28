import streamlit as st
import json
from datetime import datetime
import pandas as pd
import time
import os

st.set_page_config(page_title="APOLLO", layout="centered")

# -------- PWA CONFIG --------
st.markdown("""
<link rel="manifest" href="static/manifest.json">
<meta name="theme-color" content="#556b2f">
<link rel="apple-touch-icon" href="static/icon.png">
""", unsafe_allow_html=True)

# -------- SPLASH SCREEN --------
if "loaded" not in st.session_state:
    st.session_state.loaded = True
    st.markdown("# 💪 APOLLO")
    st.markdown("### Cargando...")
    time.sleep(1.5)
    st.rerun()

# -------- ESTILO OLIVA --------
st.markdown("""
<style>
body {background-color: #0c0f0a; color: #e5e7eb;}
h1, h2, h3 {color: #d1d5db;}
.stButton>button {
    width: 100%;
    border-radius: 18px;
    height: 55px;
    font-size: 15px;
    font-weight: 600;
    background: linear-gradient(135deg, #556b2f, #6b8e23);
    color: white;
    border: none;
}
.stNumberInput input {
    border-radius: 12px;
    background-color: #1a1f14;
    color: white;
}
</style>
""", unsafe_allow_html=True)

FILE = "data.json"

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({"entrenos": [], "dietas": [], "pesos": []}, f)

with open(FILE, "r") as f:
    data = json.load(f)

st.markdown("# 💪 APOLLO")

menu = st.radio("", ["🏋️", "🍽️", "📊"], horizontal=True)

# ---------------- ENTRENAMIENTO ----------------
if menu == "🏋️":

    dia = st.selectbox("Día", ["Día 1", "Día 2", "Día 3", "Día 4"])

    rutina = {
        "Día 1": [
            ("Press inclinado Smith", "3x6-8"),
            ("Press convergente", "3x10-12"),
            ("Aperturas contractora", "3x10-12"),
            ("Elevaciones laterales", "4x12-15"),
            ("Fondos tríceps", "4x8-12"),
        ],
        "Día 2": [
            ("Remo barra", "4x12/10/10/8"),
            ("Dominadas", "4x6-8"),
            ("Remo mancuerna", "3x12/10/8"),
            ("Remo inclinado", "3x10-12"),
            ("Pájaros", "3x10-12"),
            ("Curl predicador", "3x10-12"),
            ("Curl martillo", "2x10-8"),
        ],
        "Día 3": [
            ("Sentadilla", "2x6 + 3x10"),
            ("Prensa", "3x8-10"),
            ("Curl femoral", "3x10"),
            ("Extensión cuádriceps", "3x10"),
            ("Peso muerto rumano", "3x10-12"),
            ("Gemelo Smith", "4x10-15"),
        ],
        "Día 4": [
            ("Press inclinado Smith", "3x8/6/6"),
            ("Aperturas", "3x10-12"),
            ("Press máquina", "3x10-12"),
            ("Press militar", "2x8"),
            ("Laterales", "3x10-12"),
            ("Skull crushers", "4x8-10"),
            ("Press cerrado", "4x8-10"),
        ]
    }

    if "timer" not in st.session_state:
        st.session_state.timer = 0

    timer = st.empty()
    registro = []

    for i, (ej, info) in enumerate(rutina[dia]):

        st.markdown(f"**{ej}**  \n_{info}_")

        col1, col2 = st.columns([2,1])

        with col1:
            peso = st.number_input("Peso", 0.0, step=2.5, key=f"p{i}")
        with col2:
            if st.button("⏱️", key=f"t{i}"):
                st.session_state.timer = 60

        registro.append({"ejercicio": ej, "peso": peso})

        st.markdown("---")

    if st.session_state.timer > 0:
        timer.markdown(f"## ⏳ {st.session_state.timer}s")
        time.sleep(1)
        st.session_state.timer -= 1
        st.rerun()

    if st.button("💾 Guardar entreno"):
        data["entrenos"].append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "dia": dia,
            "ejercicios": registro
        })
        with open(FILE, "w") as f:
            json.dump(data, f)
        st.success("Entreno guardado 🔥")

# ---------------- DIETA ----------------
elif menu == "🍽️":

    st.markdown("### 🍽️ Dieta (2150 kcal)")

    dieta = {
        "Desayuno": [
            ("Tostada integral + jamón + tomate + aceite + fruta", 
             "Pan 100g, jamón 50g, tomate 50g, aceite 8ml + fruta", 500),
            ("Pan + huevos + guacamole + fruta",
             "Pan 100g, huevo 100g, guacamole 20g + fruta", 500),
            ("Tortitas avena + chocolate + fresas",
             "Avena 50g, huevo, claras, plátano, fresas, chocolate", 500),
            ("Leche + corn flakes + cacao + fruta",
             "Leche 300g, corn flakes 50g, cacao 10g + fruta", 500),
        ],
        "Comida": [
            ("Patata + atún + huevo + pimiento",
             "Patata 300g, atún 160g, huevo 120g, pimiento 50g", 850),
            ("Arroz + pollo + champiñones",
             "Arroz 85g, pollo 150g, champiñones, tomate", 850),
            ("Espaguetis + carne + tomate",
             "Pasta 100g, carne 200g, tomate", 850),
            ("Macarrones + salmón + verduras",
             "Macarrones 100g, salmón 220g, verduras", 850),
        ],
        "Cena": [
            ("Pasta + pollo + verduras",
             "Macarrones 120g, pollo 200g, verduras", 800),
            ("Merluza + puré de patata",
             "Patata 300g, merluza 200g", 800),
            ("Arroz + atún + verduras",
             "Arroz 120g, atún 160g, verduras", 800),
            ("Pavo + quinoa + judías",
             "Quinoa 120g, pavo 200g, judías", 800),
        ]
    }

    total = 0
    seleccion = {}

    for comida, opciones in dieta.items():

        st.markdown(f"#### {comida}")

        nombres = [o[0] for o in opciones]
        opcion = st.selectbox(comida, nombres, key=comida)

        detalle = next(o for o in opciones if o[0] == opcion)

        st.caption(detalle[1])
        st.write(f"🔥 {detalle[2]} kcal")

        seleccion[comida] = opcion
        total += detalle[2]

        st.markdown("---")

    st.success(f"🔥 TOTAL: {total} kcal")

    if st.button("💾 Guardar dieta"):

        hoy = datetime.now().strftime("%Y-%m-%d")
        data["dietas"] = [d for d in data["dietas"] if d["fecha"] != hoy]

        data["dietas"].append({
            "fecha": hoy,
            "comidas": seleccion,
            "kcal": total
        })

        with open(FILE, "w") as f:
            json.dump(data, f)

        st.success("Dieta guardada 🔥")

# ---------------- PROGRESO ----------------
elif menu == "📊":

    st.markdown("### 📊 Progreso")

    peso = st.number_input("Peso actual")

    if st.button("Guardar peso"):
        data["pesos"].append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "peso": peso
        })
        with open(FILE, "w") as f:
            json.dump(data, f)

    if data["pesos"]:
        df = pd.DataFrame(data["pesos"])
        st.line_chart(df.set_index("fecha")["peso"])

    st.markdown("---")

    st.markdown("### 🍽️ Historial dieta")

    if data["dietas"]:
        df_dieta = pd.DataFrame(data["dietas"])
        st.line_chart(df_dieta.set_index("fecha")["kcal"])

        for d in reversed(data["dietas"]):
            st.markdown(f"**📅 {d['fecha']}**")
            st.write(f"🔥 {d['kcal']} kcal")

            if d.get("comidas"):
                for comida, opcion in d["comidas"].items():
                    st.write(f"- {comida}: {opcion}")

            st.markdown("---")
