import pandas as pd

# Ler o arquivo Excel
df = pd.read_excel(
    r"C:\Data Science\data_games\arquivos_transformados\dataset_transformado.xlsx"
)

# Deletar as linhas com valores nulos em qualquer coluna
df = df.dropna()

# Salvar o DataFrame em um novo arquivo Excel
df.to_excel(
    r"C:\Data Science\data_games\linhas_em_branco_deletadas\dataset_final.xlsx",
    index=False,
)
