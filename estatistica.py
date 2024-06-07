import pandas as pd 
import os

df = pd.read_csv('datasets/processados/clientes_filtrados.csv')

colunas_interesse = ['salario']

amplitude = df[colunas_interesse].max() - df[colunas_interesse].min()

print(amplitude)

df['salario'].mean()
df['salario'].plot.kde()
df['salario'].plot.box()