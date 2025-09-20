
def ultimos_colocados(df, esp="TODAS", local="TODAS"):
    # Filtrar dados
    if esp != "TODAS":
        df_filtered = df[df["Especialidade"] == esp]
    else:
        df_filtered = df.copy()

    if local != "TODAS":
        df_filtered = df_filtered[df_filtered["TODAS"] == local]
    
    

    ul_coloc = {}

    # Criar uma cópia para não mexer no original
    df_copy = df_filtered.copy()


    # Iterar por ano e calcular último colocado
    for ano in sorted(df_copy["Ano"].unique()):
        # pegar a linha com maior Numero_Ordem
        ultimo = df_copy[df_copy["Ano"] == ano]["Numero_Ordem"].max()
        ul_coloc[ano] = ultimo

    return ul_coloc




