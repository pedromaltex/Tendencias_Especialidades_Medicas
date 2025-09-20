# %%
# ---
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd

ultimos_colocados = pd.read_csv("csv\ALL.csv")

# --- Interface Streamlit ---
st.title("Colocações Especialidades")

with st.sidebar.form("params_form"):
    st.header("Parâmetros")
    especialidades = sorted(ultimos_colocados["Especialidade"].dropna().unique())
    especialidades.insert(0, "TODAS")

    especialidade = st.selectbox("Especialidade:", especialidades)

    nota_utilizador = st.number_input("A minha posição:", 0, value=100)

    instituicoes = ["Todas"] + sorted(ultimos_colocados["Local"].dropna().unique())
    freq_contribuitions = st.selectbox("Local:", instituicoes)

    submit = st.form_submit_button("Mostrar Gráfico")

if submit:
    # Filtrar dados
    df_filtered = ultimos_colocados[ultimos_colocados["Especialidade"] == especialidade]

    if freq_contribuitions != "Todas":
        df_filtered = df_filtered[df_filtered["Local"] == freq_contribuitions]

    anos = df_filtered["Ano"].values
    y = df_filtered["Numero_Ordem"].values   # <-- aqui usas a coluna real da nota

    # --- Gráfico ---
    fig = go.Figure()


    fig.add_trace(go.Bar(
            x=anos,
            y=y,
            name=f"Último colocado ({especialidade})",
            opacity=0.7
        ))

    fig.add_trace(go.Scatter(
        x=anos,
        y=y,
        mode='lines+markers',
        name=f"Último colocado ({especialidade})",
        opacity=0.8
    ))

    # Linha horizontal da nota do utilizador
    fig.add_hline(
        y=nota_utilizador,
        line_dash="dot",
        line_color="red",   # <-- this makes it red
        annotation_text="Minha nota",
        annotation_position="bottom right"
    )

    fig.update_layout(
        title=f"Nota último colocado - {especialidade}",
        xaxis_title="Ano",
        yaxis_title="Nota",
        legend_title="Legenda"
    )

    st.plotly_chart(fig)
