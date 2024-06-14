import pandas as pd 

df = pd.read_csv('datasets/processados/clientes_filtrados.csv')

colunas_numericas = ['idade_atual', 'altura_cm', 'salario', 'peso']
analise_correlacao = df[colunas_numericas].corr()

with open('resultados/Correlacao.txt', 'w', encoding='utf-8') as f:
    f.write('----------------Análise de Correlação-----------------\n')
    f.write(str(analise_correlacao) + '\n\n')
