import pandas as pd


def convert_K_to_number(value):
    if "K" in value:
        number = float(value.replace("K", "")) * 1000
        return int(number)
    else:
        return int(value)


# Ler o arquivo Csv
df = pd.read_csv(
    r"C:\Data Science\data_games\arquivos_separados\games_separado_por_ponto_e_virgula.csv",
    delimiter=";",
)

# Aplicar a função convert_K_to_number nas colunas desejadas
colunas_tratadas = [
    "Times Listed",
    "Number of Reviews",
    "Plays",
    "Playing",
    "Backlogs",
    "Wishlist",
]
df[colunas_tratadas] = df[colunas_tratadas].applymap(convert_K_to_number)

# Salvar o arquivo tratado em um novo arquivo Excel
df.to_excel(
    r"C:\Data Science\data_games\arquivos_transformados\dataset_transformado.xlsx",
    index=False,
)
