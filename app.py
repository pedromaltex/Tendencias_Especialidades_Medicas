import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from config import CSV_PATH

# --- Carregar CSV ---
dados = pd.read_csv(CSV_PATH)

# --- Título ---
st.title("Colocações Especialidades Médicas🩺")

# --- Sidebar ---
# Escolher especialidades
with st.sidebar.expander("Escolher Especialidades", expanded=True):
    especialidades = sorted(dados["Especialidade"].dropna().unique())
    especialidades.insert(0, "TODAS")
    especialidades_escolhidas = st.multiselect(
        "Especialidades:", 
        especialidades, 
        default=["Medicina Geral Familiar"]
    )

# Escolher local
with st.sidebar.expander("Escolher Local", expanded=False):
    if "TODAS" in especialidades_escolhidas:
        instituicoes = sorted(dados["Local"].dropna().unique())
    else:
        instituicoes = sorted(
            dados[dados["Especialidade"].isin(especialidades_escolhidas)]["Local"].dropna().unique()
        )
    instituicoes.insert(0, "TODAS")
    instituicao = st.selectbox("Local:", instituicoes)

# Posição do utilizador
with st.sidebar.expander("Definir Posição", expanded=False):
    nota_utilizador = st.slider("A minha posição:", 1, 3000, value=1000)

# Botão para gerar gráfico
submit = st.sidebar.button("Mostrar Gráfico")

# --- Gráfico ---
if submit:
    fig = go.Figure()

    # Para cada especialidade selecionada
    for esp in especialidades_escolhidas:
        dados_filtrados = dados.copy()

        if esp != "TODAS":
            dados_filtrados = dados_filtrados[dados_filtrados["Especialidade"] == esp]
        if instituicao != "TODAS":
            dados_filtrados = dados_filtrados[dados_filtrados["Local"] == instituicao]

        if dados_filtrados.empty:
            continue  # ignora se não houver dados

        # Último colocado por ano
        dados_grouped = dados_filtrados.groupby("Ano", as_index=False)["Numero_Ordem"].max()

        fig.add_trace(go.Scatter(
            x=dados_grouped["Ano"],
            y=dados_grouped["Numero_Ordem"],
            mode='lines+markers',
            name=f"Último colocado ({esp})",
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

    # Layout
    titulo = "Evolução últimos colocados"
    if instituicao != "TODAS":
        titulo += f" ({instituicao})"

    fig.update_layout(
        title=titulo,
        xaxis_title="Ano",
        yaxis_title="Número de Ordem",
        legend_title="Legenda"
    )

    # Se quiseres o 1º lugar no topo, ativa esta linha:
    # fig.update_yaxes(autorange="reversed")

    st.plotly_chart(fig)

st.markdown(
    """
    <hr>
    <p style='text-align: center; color: gray; font-size: 12px;'>
        Desenvolvido por Pedro Maltez | Dados de Fábio Fernandes
    </p>
    """,
    unsafe_allow_html=True
)

