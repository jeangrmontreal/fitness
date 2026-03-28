import streamlit as st
from supabase import create_client

st.title("🚀 APOLLO v2")

SUPABASE_URL = "https://obhfwfkfeyfoiyuwczbe.supabase.co"
SUPABASE_KEY = "sb_publishable__6hcsOxp7_6blIRz-nOphQ_8RZCKW2d"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.success("✅ Conectado a Supabase")

# 🔥 PROBAR LECTURA
try:
    res = supabase.table("usuarios").select("*").limit(5).execute()
    st.success("✅ Tabla accesible")
    st.write(res.data)
except Exception as e:
    st.error("❌ Error leyendo tabla")
