import streamlit as st
import plotly.graph_objects as go

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Market Scope Audit", layout="centered")

# Ocultar elementos por defecto de Streamlit para que parezca una App nativa
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stApp {background-color: #0E1117;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- DATOS DEL CLIENTE (Aquí cambias los datos antes de entrar) ---
cliente = "El Poch del Huach"
score = 8.0
problema_principal = "Sin Web Propia (Dependencia de Apps)"
fuga_dinero = "30% de Margen perdido"
solucion_oferta = "Sistema de Pedidos Directo"

# --- ENCABEZADO ---
st.markdown(f"<h1 style='text-align: center; color: white;'>📍 Auditoría Express</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: #FF4B4B;'>{cliente}</h3>", unsafe_allow_html=True)

st.write("---")

# --- SECCIÓN 1: EL SCORE (VELOCÍMETRO) ---
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = score,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Health Score", 'font': {'size': 24, 'color': "white"}},
    number = {'font': {'size': 50, 'color': "white"}},
    gauge = {
        'axis': {'range': [None, 10], 'tickwidth': 1, 'tickcolor': "white"},
        'bar': {'color': "#00CC96" if score >= 8 else "#FFA15A" if score >= 5 else "#EF553B"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 4], 'color': '#330000'},
            {'range': [4, 7], 'color': '#332200'},
            {'range': [7, 10], 'color': '#003300'}],
        'threshold': {
            'line': {'color': "white", 'width': 4},
            'thickness': 0.75,
            'value': score}}))

fig.update_layout(paper_bgcolor="#0E1117", font={'color': "white", 'family': "Arial"}, height=300, margin=dict(l=20, r=20, t=50, b=20))
st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN 2: DIAGNÓSTICO RÁPIDO ---
col1, col2 = st.columns(2)

with col1:
    st.error("❌ DEBILIDAD")
    st.caption("Sitio Web / Canal Propio")
    st.markdown(f"**Inexistente**")

with col2:
    st.success("✅ FORTALEZA")
    st.caption("Reputación Google Maps")
    st.markdown("**4.6 Estrellas (Líder)**")

st.write("---")

# --- SECCIÓN 3: EL DOLOR Y LA SOLUCIÓN (TU VENTA) ---
st.subheader("💡 Oportunidad Detectada")

# Tarjeta de alerta
st.warning(f"⚠️ **Problema:** {problema_principal}")
st.markdown(f"Estás regalando aprox. **{fuga_dinero}** en cada pedido por delivery.")

# Botón simulado de solución
st.markdown("### 🚀 Solución Activada:")
st.info(f"👉 **{solucion_oferta}**")

with st.expander("Ver detalle de la solución"):
    st.write("""
    1. Creación de Menú Digital QR (Propio).
    2. Enlace directo en Google Maps y Facebook.
    3. Campaña "Pide directo y recibe bebida gratis" (Financiada con el ahorro de comisión).
    """)

# --- BOTÓN DE CIERRE ---
if st.button('Agendar Demo Técnica'):
    st.balloons()
    st.success("¡Perfecto! Analicemos los números.")