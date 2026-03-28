import streamlit as st
from supabase import create_client

st.title("🚀 APOLLO v3")

SUPABASE_URL = "https://obhfwfkfeyfoiyuwczbe.supabase.co"
SUPABASE_KEY = ""

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.success("✅ Conectado a Supabase")

# 🔥 LOGIN SIMPLE
nombre = st.text_input("👤 Tu nombre")

if st.button("Entrar"):

    # buscar usuario
    res = supabase.table("usuarios").select("*").eq("nombre", nombre).execute()

    if res.data:
        st.success(f"Bienvenido de nuevo {nombre} 🔥")
        user = res.data[0]
    else:
        # crear usuario
        supabase.table("usuarios").insert({
            "nombre": nombre,
            "historial": [],
            "pesos": []
        }).execute()

        st.success(f"Usuario {nombre} creado 🚀")

        res = supabase.table("usuarios").select("*").eq("nombre", nombre).execute()
        user = res.data[0]

    st.write(user)
