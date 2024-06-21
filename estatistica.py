import pandas as pd 
import os

df2 = pd.read_csv('datasets/processados/clientes_filtrados.csv')
df = pd.read_csv('datasets/clientes.csv')

with open('resultados/Estatistica_descritiva.txt', 'w', encoding='utf-8') as f:
    f.write('----------------Idade Atual-----------------\n')
    describe_idade = df2['idade'].describe().rename({
        'count': 'contagem',
        'mean': 'média',
        'std': 'desvio padrão',
        'min': 'mínimo',
        '25%': '1º quartil',
        '50%': 'mediana',
        '75%': '3º quartil',
        'max': 'máximo'
    })
    f.write(str(describe_idade) + '\n')

    mode_idade = df2['idade'].mode()[0]
    f.write("Moda idade: " + str(mode_idade) + '\n')

    median_idade = df2['idade'].median()
    f.write("Mediana idade: " + str(median_idade) + '\n')

    f.write('----------------Altura-----------------\n')
    describe_altura = df2['altura_cm'].describe().rename({
        'count': 'contagem',
        'mean': 'média',
        'std': 'desvio padrão',
        'min': 'mínimo',
        '25%': '1º quartil',
        '50%': 'mediana',
        '75%': '3º quartil',
        'max': 'máximo'
    })
    f.write(str(describe_altura) + '\n')

    mode_altura = df2['altura_cm'].mode()[0]
    f.write("Moda Altura: " + str(mode_altura) + '\n')

    median_altura = df2['altura_cm'].median()
    f.write("Mediana Altura: " + str(median_altura) + '\n')

    f.write('----------------Salário-----------------\n')
    describe_salario = df2['salario'].describe().rename({
        'count': 'contagem',
        'mean': 'média',
        'std': 'desvio padrão',
        'min': 'mínimo',
        '25%': '1º quartil',
        '50%': 'mediana',
        '75%': '3º quartil',
        'max': 'máximo'
    })
    f.write(str(describe_salario) + '\n')

    mode_salario = df2['salario'].mode()[0]
    f.write("Moda Salário: " + str(mode_salario) + '\n')

    median_salario = df2['salario'].median()
    f.write("Mediana Salário: " + str(median_salario) + '\n')

    f.write('----------------Peso-----------------\n')
    describe_peso = df2['peso'].describe().rename({
        'count': 'contagem',
        'mean': 'média',
        'std': 'desvio padrão',
        'min': 'mínimo',
        '25%': '1º quartil',
        '50%': 'mediana',
        '75%': '3º quartil',
        'max': 'máximo'
    })
    f.write(str(describe_peso) + '\n')

    mode_peso = df2['peso'].mode()[0]
    f.write("Moda Peso: " + str(mode_peso) + '\n')

    median_peso = df2['peso'].median()
    f.write("Mediana Peso: " + str(median_peso) + '\n')

    f.write('----------------Gênero Musical-----------------\n')
    # Calculating the frequency distribution for one-hot encoded columns
    colunas_codificadas_one_hot = df.filter(like='genero_')
    distribuicao_frequencia = colunas_codificadas_one_hot.sum()
    
    # Normalizing the frequency distribution
    total_sum = distribuicao_frequencia.sum()
    distribuicao_normalizada = distribuicao_frequencia / total_sum
    
    # Writing the normalized frequency distribution to the file
    f.write("Distribuição de Frequência para as Colunas de Gênero Musical:\n")
    f.write(str(distribuicao_normalizada) + '\n')
    
    f.write('----------------Sexo-----------------\n')
    # Calculating the frequency distribution for one-hot encoded columns
    colunas_codificadas_one_hot = df.filter(like='sexo_')
    distribuicao_frequencia = colunas_codificadas_one_hot.sum()
    
    # Normalizing the frequency distribution
    total_sum = distribuicao_frequencia.sum()
    distribuicao_normalizada = distribuicao_frequencia / total_sum
    
    # Writing the normalized frequency distribution to the file
    f.write("Distribuição de Frequência para as Colunas de Sexo:\n")
    f.write(str(distribuicao_normalizada) + '\n')
    
    f.write('----------------Cidade-----------------\n')
    # Calculating the frequency distribution for one-hot encoded columns
    colunas_codificadas_one_hot = df.filter(like='cidade_')
    distribuicao_frequencia = colunas_codificadas_one_hot.sum()
    
    # Normalizing the frequency distribution
    total_sum = distribuicao_frequencia.sum()
    distribuicao_normalizada = distribuicao_frequencia / total_sum
    
    # Writing the normalized frequency distribution to the file
    f.write("Distribuição de Frequência para as Colunas de Cidade:\n")
    f.write(str(distribuicao_normalizada) + '\n')
    
    f.write('----------------Profissão-----------------\n')
    # Calculating the frequency distribution for one-hot encoded columns
    colunas_codificadas_one_hot = df.filter(like='profissao_')
    distribuicao_frequencia = colunas_codificadas_one_hot.sum()
    
    # Normalizing the frequency distribution
    total_sum = distribuicao_frequencia.sum()
    distribuicao_normalizada = distribuicao_frequencia / total_sum
    
    # Writing the normalized frequency distribution to the file
    f.write("Distribuição de Frequência para as Colunas de Profissão:\n")
    f.write(str(distribuicao_normalizada) + '\n')