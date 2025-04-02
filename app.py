# app.py

import streamlit as st
import pandas as pd
from datetime import timedelta

st.set_page_config(page_title="Dashboard Exemplo RH", layout="wide")

st.title("📊 Dashboard de Produtividade - Exemplo")

# Simula dados de ponto e atendimento
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

# Seleção de colaborador
colab_sel = st.selectbox("Selecione um colaborador", ponto_df["nome"].tolist())

# Exibe dados de ponto
st.subheader("📌 Registro de Ponto")
colab_data = ponto_df[ponto_df["nome"] == colab_sel].iloc[0]
col1, col2, col3 = st.columns(3)
col1.metric("❌ Faltas", colab_data["faltas"])
col2.metric("🕒 Atrasos", colab_data["atrasos"])
col3.metric("⏰ Horas Extras", colab_data["hora_extra_total"])

# Exibe dados de atendimento
st.subheader("📞 Atendimento")
atendimentos = atendimento_df[atendimento_df["nome"] == colab_sel]["Tickets finalizados"].values[0]
st.write(f"**Tickets finalizados por {colab_sel}:** {atendimentos}")
