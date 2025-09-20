# %%

# ---
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
from helpers import ultimos_colocados
from config import CSV_PATH

# Carregar CSV
dados = pd.read_csv(CSV_PATH)
dados["Numero_Ordem"] = dados["#"]

# --- Interface Streamlit ---
st.title("Colocações Especialidades")

with st.sidebar.form("params_form"):
    st.header("Parâmetros")

    # Especialidades
    especialidades = sorted(dados["Especialidade"].dropna().unique())
    especialidades.insert(0, "TODAS")
    especialidade = st.selectbox("Especialidade:", especialidades)

    # Posição do utilizador
    nota_utilizador = st.number_input("A minha posição:", 0, value=100)

    # Instituições
    instituicoes = ["TODAS"] + sorted(dados["Local"].dropna().unique())
    instituicao = st.selectbox("Local:", instituicoes)

    submit = st.form_submit_button("Mostrar Gráfico")

if submit:
    # Filtrar dados
    if especialidade != "TODAS":
        df_filtered = dados[dados["Especialidade"] == especialidade]
    else:
        df_filtered = dados.copy()

    if instituicao != "TODAS":
        df_filtered = df_filtered[df_filtered["TODAS"] == instituicao]

    # Extrair dados
    anos = df_filtered["Ano"].values
    y = df_filtered["Numero_Ordem"].values   # coluna com posição do último colocado
    y = ultimos_colocados(df_filtered, especialidade, instituicao).values()
    # --- Gráfico ---
    fig = go.Figure()

    # Linha de evolução
    fig.add_trace(go.Scatter(
        x=anos,
        y=y,
        mode='lines+markers',
        name=f"Último colocado ({especialidade})",
        opacity=0.8
    ))

    # Linha horizontal da posição do utilizador
    fig.add_hline(
        y=nota_utilizador,
        line_dash="dot",
        line_color="red",
        annotation_text="Minha posição",
        annotation_position="bottom right"
    )

    # Título dinâmico
    titulo = f"Último colocado - {especialidade}"
    if instituicao != "TODAS":
        titulo += f" ({instituicao})"

    # Layout
    fig.update_layout(
        title=titulo,
        xaxis_title="Ano",
        yaxis_title="Número de Ordem",
        legend_title="Legenda"
    )

    # Inverter eixo Y (1º lugar é melhor que 1000º, etc.)
    fig.update_yaxes(autorange="reversed")

    # Mostrar gráfico
    st.plotly_chart(fig)
