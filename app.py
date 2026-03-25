# 🍽️ DIETA PRO REAL
elif menu == "🍽️ Dieta":

    st.header("🍽️ Dieta detallada")

    comida = st.selectbox("Selecciona comida", ["Comida 1", "Comida 2", "Comida 3"])

    if comida == "Comida 1":

        opcion = st.radio("Opciones", [
            "Tostada jamón",
            "Tostada huevos",
            "Tortitas avena",
            "Leche + cereales"
        ])

        if opcion == "Tostada jamón":
            st.write("Pan integral 100g")
            st.write("Jamón serrano 50g")
            st.write("Tomate 50g")
            st.write("Aceite oliva 8ml")
            st.write("Fruta 1 pieza")

        elif opcion == "Tostada huevos":
            st.write("Pan integral 100g")
            st.write("Huevo 100g")
            st.write("Guacamole 20g")
            st.write("Fruta 1 pieza")

        elif opcion == "Tortitas avena":
            st.write("Harina avena 50g")
            st.write("Huevo 60g")
            st.write("Claras 80g")
            st.write("Plátano 100g")
            st.write("Fresas 80g")
            st.write("Chocolate 5g")
            st.write("Aceite 5g")

        else:
            st.write("Leche 300g")
            st.write("Corn flakes 50g")
            st.write("Cacao 10g")
            st.write("Fruta 1 pieza")

        st.success("🔥 500 kcal")

    elif comida == "Comida 2":

        opcion = st.radio("Opciones", [
            "Patata + atún",
            "Arroz + pollo",
            "Pasta + carne",
            "Macarrones + salmón"
        ])

        if opcion == "Patata + atún":
            st.write("Patata 300g")
            st.write("Atún 160g")
            st.write("Huevo 120g")
            st.write("Pimiento 50g")
            st.write("Aceite 8ml")

        elif opcion == "Arroz + pollo":
            st.write("Arroz 85g")
            st.write("Pollo 150g")
            st.write("Champiñones 50g")
            st.write("Aceite 10ml")

        elif opcion == "Pasta + carne":
            st.write("Espaguetis 100g")
            st.write("Carne 200g")
            st.write("Tomate 100g")

        else:
            st.write("Macarrones 100g")
            st.write("Salmón 220g")
            st.write("Verduras")
            st.write("Aceite 10ml")

        st.success("🔥 850 kcal")

    else:

        opcion = st.radio("Opciones", [
            "Pasta + pollo",
            "Merluza + patata",
            "Arroz + atún",
            "Pavo + quinoa"
        ])

        if opcion == "Pasta + pollo":
            st.write("Macarrones 120g")
            st.write("Pollo 200g")
            st.write("Verduras 150g")

        elif opcion == "Merluza + patata":
            st.write("Patata 300g")
            st.write("Merluza 200g")
            st.write("Mantequilla 25g")
            st.write("Aceite 10ml")

        elif opcion == "Arroz + atún":
            st.write("Arroz 120g")
            st.write("Atún 160g")
            st.write("Verduras")
            st.write("Aceite 10ml")

        else:
            st.write("Quinoa 120g")
            st.write("Pavo 200g")
            st.write("Judías 200g")
            st.write("Aceite 10ml")

        st.success("🔥 800 kcal")

    st.markdown("---")

    st.subheader("📊 Totales")
    st.write("🔥 2150 kcal")
    st.write("💪 Proteínas: 190–200g")
    st.write("🍚 Hidratos: 290–305g")
    st.write("🥑 Grasas: 70–75g")

    st.markdown("---")

    st.write("💧 Agua: 3–4L")
    st.write("⚡ Creatina: 7g")
