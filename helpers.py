# %%
def ultimos_colocados_na_especialidade(df, esp:str, local=None):
    # Filtrar dados
    if esp == "TODAS":
        raise ValueError("Não Podes colocar TODAS na especialidade. " \
        "helpers.py, ultimos_colocados")

    if local is not None:
        raise ValueError("Não podes colocar local. " \
        "helpers.py, ultimos_colocados")
    
    ul_coloc = []

    # Criar uma cópia para não mexer no original
    df_copy = df.copy()

    if esp:
        df_copy = df_copy[df_copy["Especialidade"] == esp]

    # Iterar por ano e calcular último colocado
    for ano in sorted(df_copy["Ano"].unique()):
        # pegar a linha com maior Numero_Ordem

        ultimo = df_copy[df_copy["Ano"] == ano]["Numero_Ordem"].max()

        ul_coloc.append({"Ano":ano,"especialidade":esp, "ultimo_colocado":ultimo})

    return ul_coloc

# %%
if __name__ == "__main__":
    import pandas as pd
    from config import CSV_PATH

    dados = pd.read_csv(CSV_PATH)

    # Especialidades
    especialidades = sorted(dados["Especialidade"].dropna().unique())
    especialidades.insert(0, "TODAS")
    especialidade = "Radiologia"
    print(especialidades)
    
    # Instituições
    instituicoes = sorted(dados["Local"].dropna().unique())
    instituicoes.insert(0, "TODAS")
    instituicao = instituicoes[10]
    print(instituicoes)


    y = ultimos_colocados_na_especialidade(dados, especialidade)
    y = pd.DataFrame(y)
    print(y)


# %%
