import pandas as pd
import os
import sklearn.preprocessing as skl

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


df = pd.read_csv('datasets/clientes.csv')
os.makedirs('datasets/processados', exist_ok=True)

df.isnull().sum()   


# Resetando o índice para obter uma sequência numérica como novo ID
df['id'] = range(1, len(df) + 1)
df.drop(columns=['nome'], inplace=True)
df.fillna(df.mean(), inplace=True)
df.dropna(subset=['genero_musical_favorito', 'cidade', 'profissao', 'data_de_nascimento','sexo'], inplace=True)
df_filtrado = df[
    (df['idade'] >= 18) & (df['idade'] <= 70) & 
    (df['altura_cm'] >= 120) & (df['altura_cm'] <= 210) & 
    (df['sexo'].isin(['Masculino', 'Feminino', 'Outro']))
]

df_filtrado.to_csv('datasets/processados/seu_arquivo_filtrado.csv', index=False)

linhas_removidas = len(df) - len(df_filtrado)
print(f'{linhas_removidas} linhas foram removidas.')