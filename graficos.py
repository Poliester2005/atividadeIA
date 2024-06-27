import matplotlib.pyplot as plt
import pandas as pd

# ATRIBUTOS NUMÉRICOS

colunas_numericas = ['idade', 'altura_cm', 'salario', 'peso']

# REPRESENTAÇÃO GRÁFICA ---- HISTOGRAMA

try:
    df = pd.read_csv('datasets/clientes.csv')
except FileNotFoundError:
    print("Arquivo clientes_filtrados.csv não encontrado. Verifique o caminho do arquivo.")


# Configuração do layout dos subplots
fig, axs = plt.subplots(nrows=1, ncols=len(colunas_numericas), figsize=(15, 5))

# Criando os histogramas para cada coluna
for i, col in enumerate(colunas_numericas):
    axs[i].hist(df[col], bins=8, color='blue', alpha=0.7)
    axs[i].set_xlabel(col)
    axs[i].set_ylabel('Frequência')
    axs[i].set_title(f'Histograma de {col}')
    axs[i].grid(True)

# Ajuste de layout
plt.tight_layout()
plt.show()

# REPRESENTAÇÃO GRÁFICA ---- BOXPLOT
def boxplot():
    fig, axs = plt.subplots(nrows=1, ncols=len(colunas_numericas), figsize=(15, 5))

    # Criando os box plots para cada coluna
    for i, col in enumerate(colunas_numericas):
        axs[i].boxplot(df[col])
        axs[i].set_xlabel(col)
        axs[i].set_ylabel('Valor')
        axs[i].set_title(f'Box Plot de {col}')
        axs[i].grid(True)

    # Ajuste de layout
    plt.tight_layout()
    plt.show()

boxplot()