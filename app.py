import streamlit as st
from supabase import create_client

st.title("🚀 ROCIO TE AMO")

SUPABASE_URL = "https://obhfwfkfeyfoiyuwczbe.supabase.co"
SUPABASE_KEY = "sb_publishable__6hcsOxp7_6blIRz-nOphQ_8RZCKW2d"

# conectar
try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    st.success("✅ Conectado a Supabase")
except:
    st.error("❌ Error conexión")
