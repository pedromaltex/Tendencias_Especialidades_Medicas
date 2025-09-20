import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from config import CSV_PATH

# Carregar CSV
dados = pd.read_csv(CSV_PATH)

st.title("Colocações Especialidades")

# Expander para escolher especialidade
with st.sidebar.expander("Escolher Especialidade", expanded=False):
    especialidades = sorted(dados["Especialidade"].dropna().unique())
    especialidades.insert(0, "TODAS")
    especialidade = st.selectbox("Especialidade:", especialidades)

# Expander para escolher local
with st.sidebar.expander("Escolher Local", expanded=False):
    if especialidade == "TODAS":
        instituicoes = sorted(dados["Local"].dropna().unique())
    else:
        instituicoes = sorted(
            dados.loc[dados["Especialidade"] == especialidade, "Local"].dropna().unique()
        )
    instituicoes.insert(0, "TODAS")
    instituicao = st.selectbox("Local:", instituicoes)

# Expander para posição
with st.sidebar.expander("Definir Posição", expanded=True):
    nota_utilizador = st.slider("A minha posição:", 1, 3000, value=1000)

# Botão fora do form
submit = st.sidebar.button("Mostrar Gráfico")

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

    fig.add_trace(go.Scatter(
        x=anos,
        y=y,
        mode='lines+markers',
        name=f"Último colocado ({especialidade})",
        opacity=0.8
    ))

    fig.add_hline(
        y=nota_utilizador,
        line_dash="dot",
        line_color="red",
        annotation_text="Minha posição",
        annotation_position="bottom right"
    )

    titulo = f"Último colocado - {especialidade}"
    if instituicao != "TODAS":
        titulo += f" ({instituicao})"

    fig.update_layout(
        title=titulo,
        xaxis_title="Ano",
        yaxis_title="Número de Ordem",
        legend_title="Legenda"
    )

    st.plotly_chart(fig)
