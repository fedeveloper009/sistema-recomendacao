import pandas as pd

def carregar_dados(dados, sep):
    """
    Carrega os dados de um arquivo CSV e retorna um DataFrame do pandas.

    Parâmetros:
    dados (str): O caminho para o arquivo CSV.
    sep (str): O separador usado no arquivo CSV.

    Retorna:
    pd.DataFrame: Um DataFrame contendo os dados carregados.
    """
    try:
        df = pd.read_csv(dados, sep=sep)
        return df
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

def processar_dados(df):
    """
    Processa os dados do DataFrame, realizando operações de limpeza e transformação.

    Parâmetros:
    df (pd.DataFrame): O DataFrame a ser processado.

    Retorna:
    pd.DataFrame: Um DataFrame processado.
    """
    df = df.dropna()
    df = df.drop_duplicates()
    
    
    df = df.rename(columns=lambda x: x.strip().lower())
    
    return df

def unir_tabelas(df1, df2, chave):
    """
    Une dois DataFrames com base em uma chave comum.

    Parâmetros:
    df1 (pd.DataFrame): O primeiro DataFrame.
    df2 (pd.DataFrame): O segundo DataFrame.
    chave (str): A coluna usada como chave para a união.

    Retorna:
    pd.DataFrame: Um DataFrame resultante da união.
    """
    try:
        df_unido = pd.merge(df1, df2, on=chave)
        return df_unido
    except Exception as e:
        print(f"Erro ao unir as tabelas: {e}")
        return None
