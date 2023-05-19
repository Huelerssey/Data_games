import pandas as pd
import pathlib

# Define o caminho onde estão localizados os arquivos CSV
caminho_bases = pathlib.Path("dataset")

# Define o caminho onde serão salvos os arquivos de saída
caminho_output = pathlib.Path("arquivos_tratados")

# Loop para ler cada arquivo CSV e salvar em um arquivo separado por ";"
for arquivo in caminho_bases.iterdir():
    df = pd.read_csv(caminho_bases / arquivo.name, low_memory=False)
    nome_arquivo_saida = f"{arquivo.stem}_separado_por_ponto_e_virgula.csv"
    caminho_arquivo_saida = caminho_output / nome_arquivo_saida
    df.to_csv(caminho_arquivo_saida, sep=";", index=False)
