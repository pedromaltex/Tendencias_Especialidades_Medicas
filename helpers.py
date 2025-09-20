
def ultimos_colocados(df, esp="TODAS", local="TODAS"):
    ul_coloc = {}

    # Criar uma cópia para não mexer no original
    df_copy = df.copy()

    '''# Filtro local
    if local != "TODAS":
        df_copy = df_copy[df_copy["Local"] == local]'''

    # Filtro especialidade
    if esp != "TODAS":
        df_copy = df_copy[df_copy["Especialidade"] == esp]

    # Iterar por ano e calcular último colocado
    for ano in sorted(df_copy["Ano"].unique()):
        # pegar a linha com maior Numero_Ordem
        ultimo = df_copy[df_copy["Ano"] == ano]["Numero_Ordem"].max()
        ul_coloc[ano] = ultimo

    return ul_coloc




