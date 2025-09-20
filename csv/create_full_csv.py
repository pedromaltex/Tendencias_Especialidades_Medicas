# %%
def create_full_csv():
    import pandas as pd

    name = "ESCOLHA ESPECIALIDADE - ESCOLHAS "

    df = pd.read_csv(name+str(2016)+".csv")
    df["Ano"] = 2016

    for i in range(2016, 2025, 1):
        df2 = pd.read_csv(name+str(i)+".csv")
        df2["Ano"] = i

        df = pd.concat([df, df2])
    df = df[["Ano", "#", "Especialidade", "Local"]]
    return df

# %%
if __name__ == "__main__":
    import pandas as pd

    df = create_full_csv()
    df.to_csv("ALL.csv")

# %%