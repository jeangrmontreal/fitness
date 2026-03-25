# 🍽️ DIETA PRO COMPLETA
if menu == "🍽️ Dieta":

    st.subheader("🍽️ Plan nutricional APOLLO")

    comida = st.selectbox("Selecciona comida", ["Comida 1", "Comida 2", "Comida 3"])

    if comida == "Comida 1":

        opcion = st.radio("Opciones", [
            "Tostada integral + jamón + tomate + aceite + fruta",
            "Tostada integral + huevos + guacamole + fruta",
            "Tortitas avena + chocolate + fresas",
            "Leche + corn flakes + cacao + fruta"
        ])

        if opcion.startswith("Tostada integral + jamón"):
            st.write("Pan 100g | Jamón 50g | Tomate 50g | Aceite 8ml | Fruta")
        elif opcion.startswith("Tostada integral + huevos"):
            st.write("Pan 100g | Huevo 100g | Guacamole 20g | Fruta")
        elif opcion.startswith("Tortitas"):
            st.write("Avena 50g | Huevo 60g | Claras 80g | Plátano 100g | Fresas 80g | Chocolate 5g | Aceite 5g")
        else:
            st.write("Leche 300g | Corn flakes 50g | Cacao 10g | Fruta")

        st.write("🔥 500 kcal")

    elif comida == "Comida 2":

        opcion = st.radio("Opciones", [
            "Ensalada patata + atún + huevo",
            "Arroz + pollo + champiñones",
            "Espaguetis + carne + tomate",
            "Macarrones + salmón + verduras"
        ])

        if opcion.startswith("Ensalada"):
            st.write("Patata 300g | Atún 160g | Huevo 120g | Pimiento | Aceite 8ml")
        elif opcion.startswith("Arroz"):
            st.write("Arroz 85g | Pollo 150g | Champiñones | Aceite 10ml | Queso")
        elif opcion.startswith("Espaguetis"):
            st.write("Espaguetis 100g | Carne 200g | Tomate | Pimiento | Queso")
        else:
            st.write("Macarrones 100g | Salmón 220g | Verduras | Aceite 10ml")

        st.write("🔥 850 kcal")

    else:

        opcion = st.radio("Opciones", [
            "Pasta + pollo + tomate",
            "Merluza + puré de patata",
            "Arroz + atún + verduras",
            "Pavo + quinoa + judías"
        ])

        if opcion.startswith("Pasta"):
            st.write("Macarrones 120g | Pollo 200g | Verduras")
        elif opcion.startswith("Merluza"):
            st.write("Patata 300g | Merluza 200g | Mantequilla 25g | Aceite 10ml")
        elif opcion.startswith("Arroz"):
            st.write("Arroz 120g | Atún 160g | Verduras | Aceite 10ml")
        else:
            st.write("Quinoa 120g | Pavo 200g | Judías | Aceite 10ml")

        st.write("🔥 800 kcal")

    st.markdown("---")

    st.subheader("📊 Resumen diario")
    st.write("🔥 2150 kcal")
    st.write("💪 Proteínas: 190–200 g")
    st.write("🍚 Hidratos: 290–305 g")
    st.write("🥑 Grasas: 70–75 g")

    st.markdown("---")

    st.write("💧 Agua: 3–4L diarios")
    st.write("⚡ Creatina: 7g diarios")

    if st.button("✅ Día completado"):
        st.success("🔥 Dieta cumplida — vas perfecto")
