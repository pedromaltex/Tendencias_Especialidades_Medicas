# %%
def create_full_csv():
    import pandas as pd
    from config import CSV_FOLDER
    import os

    name_file = "ESCOLHA ESPECIALIDADE - ESCOLHAS 2016.csv"
    path = os.path.join(CSV_FOLDER, name_file)

    name = "ESCOLHA ESPECIALIDADE - ESCOLHAS "

    df = pd.read_csv(path)
    df["Ano"] = 2016

    for i in range(2016, 2025, 1):
        name_file = f"ESCOLHA ESPECIALIDADE - ESCOLHAS {i}.csv"
        path = os.path.join(CSV_FOLDER, name_file)
        df2 = pd.read_csv(path)
        df2["Ano"] = i

        df = pd.concat([df, df2])
    df = df[["Ano", "#", "Especialidade", "Local"]]
    df["Numero_Ordem"] = df["#"]

    return df

# %%
if __name__ == "__main__":
    import pandas as pd
    import os
    from config import CSV_FOLDER

    df = create_full_csv()
    path = os.path.join(CSV_FOLDER, "ALL.csv")
    df.to_csv(path)

# %%