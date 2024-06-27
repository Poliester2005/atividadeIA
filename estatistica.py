import pandas as pd 
import os

df = pd.read_csv('datasets/clientes.csv')

with open('resultados/Estatistica_descritiva.txt', 'w', encoding='utf-8') as f:
    f.write('----------------Idade Atual-----------------\n')
    describe_idade = df['idade'].describe().rename({
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

    mode_idade = df['idade'].mode()[0]
    f.write("Moda idade: " + str(mode_idade) + '\n')

    median_idade = df['idade'].median()
    f.write("Mediana idade: " + str(median_idade) + '\n')

    f.write('----------------Altura-----------------\n')
    describe_altura = df['altura_cm'].describe().rename({
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

    mode_altura = df['altura_cm'].mode()[0]
    f.write("Moda Altura: " + str(mode_altura) + '\n')

    median_altura = df['altura_cm'].median()
    f.write("Mediana Altura: " + str(median_altura) + '\n')

    f.write('----------------Salário-----------------\n')
    describe_salario = df['salario'].describe().rename({
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

    mode_salario = df['salario'].mode()[0]
    f.write("Moda Salário: " + str(mode_salario) + '\n')

    median_salario = df['salario'].median()
    f.write("Mediana Salário: " + str(median_salario) + '\n')

    f.write('----------------Peso-----------------\n')
    describe_peso = df['peso'].describe().rename({
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

    mode_peso = df['peso'].mode()[0]
    f.write("Moda Peso: " + str(mode_peso) + '\n')

    median_peso = df['peso'].median()
    f.write("Mediana Peso: " + str(median_peso) + '\n')

    f.write('----------------Gênero Musical-----------------\n')
    colunas_codificadas_one_hot = df.filter(like='genero_musical_favorito')
    distribuicao_frequencia = colunas_codificadas_one_hot.sum(numeric_only=True)
    
    total_sum = distribuicao_frequencia.sum(numeric_only=True)
    distribuicao_normalizada = distribuicao_frequencia / total_sum
    
    f.write("Distribuição de Frequência para as Colunas de Gênero Musical:\n")
    f.write(str(distribuicao_normalizada) + '\n')
    
    f.write('----------------Sexo-----------------\n')
    colunas_codificadas_one_hot = df.filter(like='sexo')
    distribuicao_frequencia = colunas_codificadas_one_hot.sum(numeric_only=True)

    total_sum = distribuicao_frequencia.sum(numeric_only=True)
    distribuicao_normalizada = distribuicao_frequencia / total_sum

    f.write("Distribuição de Frequência para as Colunas de Sexo:\n")
    f.write(str(distribuicao_normalizada) + '\n')
    
    f.write('----------------Cidade-----------------\n')
    colunas_codificadas_one_hot = df.filter(like='cidade')
    distribuicao_frequencia = colunas_codificadas_one_hot.sum(numeric_only=True)
    
    total_sum = distribuicao_frequencia.sum(numeric_only=True)
    distribuicao_normalizada = distribuicao_frequencia / total_sum

    f.write("Distribuição de Frequência para as Colunas de Cidade:\n")
    f.write(str(distribuicao_normalizada) + '\n')
    
    f.write('----------------Profissão-----------------\n')
    colunas_codificadas_one_hot = df.filter(like='profissao')
    distribuicao_frequencia = colunas_codificadas_one_hot.sum(numeric_only=True)
    
    total_sum = distribuicao_frequencia.sum(numeric_only=True)
    distribuicao_normalizada = distribuicao_frequencia / total_sum
    
    f.write("Distribuição de Frequência para as Colunas de Profissão:\n")
    f.write(str(distribuicao_normalizada) + '\n')