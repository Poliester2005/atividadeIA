from datetime import datetime
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

scaler = MinMaxScaler()
encoder = OneHotEncoder(sparse_output=False)

def escolher_letra(x):
    # Dicionário de mapeamento de números para letras
    mapeamento_numeros_para_letras = {
        '1': 'A',
        '2': 'A',
        '3': 'B',
        '4': 'B',
        '5': 'C',
        '6': 'C',
        '7': 'D',
        '8': 'D',
        '9': 'E',
        '10': 'E'
    }
    # Verifica se x está no intervalo esperado
    if x in mapeamento_numeros_para_letras:
        return mapeamento_numeros_para_letras[x]
    else:
        return 'F'  # Retorna 'F' para valores fora do intervalo esperado


# Função para converter datas por extenso para o formato numérico
def converter_data_para_padrao(string_data):
    meses = {
        'janeiro': '01', 'fevereiro': '02', 'março': '03', 'abril': '04', 'maio': '05', 'junho': '06',
        'julho': '07', 'agosto': '08', 'setembro': '09', 'outubro': '10', 'novembro': '11',
        'dezembro': '12'
    }
    
    if '/' in string_data:
        dia, mes, ano = string_data.split('/')
        return f'{int(dia):02d}/{int(mes):02d}/{ano}'

    dia, nome_mes, ano = string_data.split(' de ')
    mes = meses[nome_mes.lower()]

    return f'{int(dia):02d}/{mes}/{int(ano)}'

df = pd.read_csv('datasets/clientes.csv')
os.makedirs('datasets/processados', exist_ok=True)

# Calculando a média das colunas selecionadas
colunas_para_media = ['altura_cm', 'salario', 'peso']
media = round(df[colunas_para_media].mean(), 0)

df.isnull().sum()

# Resetando o índice para obter uma sequência numérica como novo ID
# Definindo os novos IDs
df['id'] = range(1, len(df) + 1)

# Preenchendo os valores nulos com as médias correspondentes
df[colunas_para_media] = df[colunas_para_media].fillna(media)

# Dropando as linhas com valores nulos em colunas específicas
df.dropna(subset=['genero_musical_favorito', 'cidade', 'profissao', 'data_de_nascimento', 'sexo', 'nome'], inplace=True)

# Removendo duplicatas, mantendo a primeira ocorrência e considerando a coluna 'nome'
df = df.drop_duplicates(subset=['nome'], keep='first')

df.drop(columns=['idade'], inplace=True)

# Filtrando os dados conforme as condições especificadas
df_filtrado = df

df_filtrado['data_de_nascimento'] = df_filtrado['data_de_nascimento'].apply(converter_data_para_padrao)

# Substituir os números por letras na coluna 'coluna1' e escolher aleatoriamente uma letra correspondente
df_filtrado['score_bom_pagador'] = df_filtrado['score_bom_pagador'].apply(escolher_letra)

df_filtrado['data_de_nascimento'] = pd.to_datetime(df_filtrado['data_de_nascimento'], format='%d/%m/%Y')

current_date = pd.Timestamp.now()

df_filtrado['idade_atual'] = ((current_date - df_filtrado['data_de_nascimento']).dt.days / 365.25).astype(int)

df_filtrado = df_filtrado[
    (df['idade_atual'] >= 18) & (df['idade_atual'] <= 70) & 
    (df['altura_cm'] >= 120) & (df['altura_cm'] <= 210) & 
    (df['sexo'].isin(['Masculino', 'Feminino', 'Outro']))
]

# One-hot encode categorical columns
df_filtrado = pd.get_dummies(df_filtrado, columns=['sexo', 'genero_musical_favorito', 'cidade', 'profissao'], dtype=int)

# Limpeza do Dataset- Parte 4
colunas_numericas = ['idade_atual', 'altura_cm', 'salario', 'peso']
df_filtrado[colunas_numericas] = scaler.fit_transform(df_filtrado[colunas_numericas])

# Limpeza do Dataset- Parte 5

df_filtrado.to_csv('datasets/processados/clientes_filtrados.csv', index=False)

linhas_removidas = len(df) - len(df_filtrado)
print(f'{linhas_removidas} linhas foram removidas.')
