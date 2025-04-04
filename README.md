[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dashboard-exemplo-zsixv4lka7tdnmgbxbjdar.streamlit.app)

# 📊 Dashboard de Produtividade - Exemplo

Dashboard interativo criado com Streamlit para visualizar métricas de produtividade e atendimento de colaboradores. Esta versão usa dados simulados e é destinada a fins educacionais e demonstração.

## 🚀 Funcionalidades

- Seleção de colaborador
- Visualização de faltas, atrasos e horas extras
- Visualização de tickets finalizados

## 📦 Requisitos

- Python 3.8+
- Bibliotecas: `streamlit`, `pandas`

Instale com:

```bash
pip install -r requirements.txt
```

## ▶️ Como rodar

```bash
streamlit run app.py
```

## 🛡️ Notas de Segurança

Este repositório **não contém nenhuma lógica de autenticação real, nem conexão com banco de dados**. Caso deseje integrar com banco de dados (ex: MySQL), recomenda-se o uso do `st.secrets` do Streamlit e variáveis de ambiente para proteger suas credenciais.

## 📁 Estrutura

```
.
├── app.py               # Código principal do dashboard
├── requirements.txt     # Bibliotecas necessárias
└── README.md            # Instruções e explicações
```

---

Se você gostou, pode dar uma estrela no repositório! ⭐
