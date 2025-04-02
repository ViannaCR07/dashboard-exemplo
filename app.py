import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Exemplo RH", layout="wide")

# ========================
# ESTILO PERSONALIZADO
# ========================
st.markdown("""
    <style>
    /* Fonte e fundo */
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f7f9fc;
    }

    /* Cabeçalho */
    .app-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 1.5rem;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    }

    .app-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2c3e50;
    }

    .logo {
        height: 60px;
    }

    /* Métricas */
    .metric-box {
        text-align: center;
        padding: 1rem;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    }
    </style>
""", unsafe_allow_html=True)

# ========================
# CABEÇALHO
# ========================
st.markdown("""
    <div class="app-header">
        <div class="app-title">🔍 Dashboard RH - Exemplo Público</div>
        <img src="https://cdn-icons-png.flaticon.com/512/2922/2922522.png" class="logo">
    </div>
    <br>
""", unsafe_allow_html=True)

# ========================
# DADOS EXEMPLO
# ========================
ponto_df = pd.DataFrame({
    "id": [1, 2, 3],
    "nome": ["Ana", "Bruno", "Carlos"],
    "faltas": [0, 1, 2],
    "atrasos": ["00:15:00", "00:35:00", "00:05:00"],
    "hora_extra_total": ["01:00:00", "00:00:00", "00:30:00"]
})

atendimento_df = pd.DataFrame({
    "id": [1, 2, 3],
    "nome": ["Ana", "Bruno", "Carlos"],
    "Tickets finalizados": [24, 30, 12]
})

# ========================
# SELEÇÃO
# ========================
colab_sel = st.selectbox("Selecione um colaborador", ponto_df["nome"].tolist())

# ========================
# MÉTRICAS DE PONTO
# ========================
st.subheader("📌 Registro de Ponto")
colab_data = ponto_df[ponto_df["nome"] == colab_sel].iloc[0]
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="metric-box">
            <h4>❌ Faltas</h4>
            <p style='font-size: 1.6rem; font-weight: bold;'>{colab_data["faltas"]}</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-box">
            <h4>🕒 Atrasos</h4>
            <p style='font-size: 1.6rem; font-weight: bold;'>{colab_data["atrasos"]}</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-box">
            <h4>⏰ Horas Extras</h4>
            <p style='font-size: 1.6rem; font-weight: bold;'>{colab_data["hora_extra_total"]}</p>
        </div>
    """, unsafe_allow_html=True)

# ========================
# MÉTRICAS DE ATENDIMENTO
# ========================
st.subheader("📞 Atendimento")
atendimentos = atendimento_df[atendimento_df["nome"] == colab_sel]["Tickets finalizados"].values[0]
st.markdown(f"""<div class="metric-box" style="width: 200px; margin: auto;">
    <h4>💼 Tickets Finalizados</h4>
    <p style='font-size: 1.6rem; font-weight: bold;'>{atendimentos}</p>
</div>""", unsafe_allow_html=True)
