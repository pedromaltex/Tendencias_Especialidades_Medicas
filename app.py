import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from config import CSV_PATH

# --- Carregar CSV ---
dados = pd.read_csv(CSV_PATH)

# --- Título ---
st.title("Colocações Especialidades Médicas🩺")

# --- Sidebar ---
# Seleção de especialidades
especialidades = sorted(dados["Especialidade"].dropna().unique())
especialidades.insert(0, "TODAS")
especialidades_escolhidas = st.sidebar.multiselect(
    "Especialidades:", 
    especialidades, 
    default=["Medicina Geral Familiar"]
)

# Seleção de local
if "TODAS" in especialidades_escolhidas:
    instituicoes = sorted(dados["Local"].dropna().unique())
else:
    instituicoes = sorted(
        dados[dados["Especialidade"].isin(especialidades_escolhidas)]["Local"].dropna().unique()
    )
instituicoes.insert(0, "TODAS")
instituicao = st.sidebar.selectbox("Local:", instituicoes)

# Slider da posição do utilizador
nota_utilizador = st.sidebar.slider("A minha posição:", 1, 3000, value=1000)

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
            continue

        # Último colocado por ano
        dados_grouped = dados_filtrados.groupby("Ano", as_index=False)["Numero_Ordem"].max()

        fig.add_trace(go.Scatter(
            x=dados_grouped["Ano"],
            y=dados_grouped["Numero_Ordem"],
            mode='lines+markers',
            name=f"{esp}",
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
        xaxis=dict(tickangle=0),  # labels na horizontal
        #yaxis=dict(autorange="reversed"),  # 1º lugar em cima
        margin=dict(l=50, r=50, t=70, b=120),  # espaço para legenda em baixo
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.4,  # ajusta para ficar abaixo do gráfico
            xanchor="center",
            x=0.5
        )
    )

    # Mostrar gráfico full width
    st.plotly_chart(fig, use_container_width=True)

# --- Créditos ---
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: gray; font-size: 12px;'>
        Desenvolvido por Pedro Maltez | Dados de Fábio Fernandes
    </p>
    """,
    unsafe_allow_html=True
)
