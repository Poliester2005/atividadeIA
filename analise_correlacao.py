import pandas as pd

# Carregando os dados do arquivo CSV
try:
        df = pd.read_csv('datasets/processados/clientes_filtrados.csv')
except FileNotFoundError:
    print("Arquivo clientes_filtrados.csv não encontrado. Verifique o caminho do arquivo.")

# Colunas numéricas para análise de correlação
colunas_numericas = ['idade_atual', 'altura_cm', 'salario', 'peso']

# Verificar se as colunas numéricas estão presentes no DataFrame
colunas_presentes = [col for col in colunas_numericas if col in df.columns]

if len(colunas_presentes) != len(colunas_numericas):
    print("Algumas colunas numéricas especificadas não foram encontradas no DataFrame.")

# Calculando a matriz de correlação
analise_correlacao = df[colunas_numericas].corr()

# Definindo o limiar de correlação forte
limiar_correlacao_forte = 0.7

# Identificando pares com correlação forte
pares_correlacao_forte = []

for i in range(len(colunas_numericas)):
    for j in range(i + 1, len(colunas_numericas)):
        if abs(analise_correlacao.iloc[i, j]) >= limiar_correlacao_forte:
            par = (colunas_numericas[i], colunas_numericas[j], analise_correlacao.iloc[i, j])
            pares_correlacao_forte.append(par)

# Salvando os resultados em um arquivo de texto
with open('resultados/Correlacao.txt', 'w', encoding='utf-8') as f:
    f.write('----------------Análise de Correlação-----------------\n')
    f.write(str(analise_correlacao) + '\n\n')

    f.write('----------------Análise de Correlação Forte-----------------\n')
    if pares_correlacao_forte:
        for par in pares_correlacao_forte:
            f.write(f'{par[0]} e {par[1]}: {par[2]}\n')
    else:
        f.write('Nenhum par de atributos com correlação forte encontrada.\n')

print("Análise de correlação concluída e resultados salvos em resultados/Correlacao.txt.")
