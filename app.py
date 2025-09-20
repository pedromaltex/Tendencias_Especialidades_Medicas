import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
from config import CSV_PATH

# Carregar CSV
dados = pd.read_csv(CSV_PATH)

# --- Interface Streamlit ---
st.title("Colocações Especialidades")

with st.sidebar.form("params_form"):
    st.header("Parâmetros")

    # Especialidades
    especialidades = sorted(dados["Especialidade"].dropna().unique())
    especialidades.insert(0, "TODAS")
    especialidade = st.selectbox("Especialidade:", especialidades)



    # 🔑 Filtrar apenas locais onde a especialidade existe
    if especialidade == "TODAS":
        instituicoes = sorted(dados["Local"].dropna().unique())
    else:
        instituicoes = sorted(
            dados.loc[dados["Especialidade"] == especialidade, "Local"].dropna().unique()
        )
    submit_filtro_locais= st.form_submit_button("Filtrar Locais com esta Especialidade")


    instituicoes.insert(0, "TODAS")
    instituicao = st.selectbox("Local:", instituicoes)

    # Posição do utilizador
    nota_utilizador = st.slider("A minha posição:", 1, 3000, value=1000)

    submit = st.form_submit_button("Mostrar Gráfico")

if submit:
    # Filtrar dados conforme parâmetros
    dados_filtrados = dados.copy()
    if especialidade != "TODAS":
        dados_filtrados = dados_filtrados[dados_filtrados["Especialidade"] == especialidade]
    if instituicao != "TODAS":
        dados_filtrados = dados_filtrados[dados_filtrados["Local"] == instituicao]

    # Pegar o último colocado por ano
    dados_grouped = dados_filtrados.groupby("Ano", as_index=False)["Numero_Ordem"].max()
    anos = dados_grouped["Ano"].values
    y = dados_grouped["Numero_Ordem"].values

    # --- Gráfico ---
    fig = go.Figure()

    # Linha evolução dos últimos colocados
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
        line_color="black",
        annotation_text="Minha posição",
        annotation_position="bottom right"
    )

    # Pontos do utilizador em cada ano (vermelho ou verde)
    cores = ["green" if nota_utilizador <= limite else "red" for limite in y]

    fig.add_trace(go.Scatter(
        x=anos,
        y=[nota_utilizador] * len(anos),
        mode='markers',
        marker=dict(color=cores, size=10, symbol="circle"),
        name="Minha posição"
    ))

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

    # Inverter eixo Y (1º lugar em cima)
    fig.update_yaxes(autorange="reversed")

    st.plotly_chart(fig)
