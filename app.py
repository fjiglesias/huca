import streamlit as st

st.set_page_config(page_title="Previsión de accidentes", layout="wide")

# Título
st.title("Previsión de accidentes en entornos hospitalarios v0.1")

# Texto descriptivo
st.write(
    "Esta herramienta se empleará para realizar la previsión de accidentes "
    "en entornos hospitalarios."
)

# Sliders en dos columnas
col1, col2 = st.columns(2)

with col1:
    probabilidad = st.slider("Probabilidad", 0, 10, 5)

with col2:
    severidad = st.slider("Severidad", 0, 10, 5)

# Cálculo del riesgo
riesgo = probabilidad * severidad

# Color en gradiente de verde a rojo
# 0 -> verde (0,255,0)
# 100 -> rojo (255,0,0)
rojo = int((riesgo / 100) * 255)
verde = int((1 - riesgo / 100) * 255)
color = f"rgb({rojo}, {verde}, 0)"

# Barra visual de riesgo
st.markdown("### Escala de riesgo")

st.markdown(
    f"""
    <div style="width: 100%; background-color: #eeeeee; border-radius: 10px; height: 35px; position: relative;">
        <div style="
            width: {riesgo}%;
            background-color: {color};
            height: 35px;
            border-radius: 10px;
            text-align: center;
            line-height: 35px;
            color: black;
            font-weight: bold;">
            {riesgo}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Resultado final
st.markdown(f"**El riesgo es {riesgo}**")