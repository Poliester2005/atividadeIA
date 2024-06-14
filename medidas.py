import pandas as pd 
import os

df = pd.read_csv('datasets/processados/clientes_filtrados.csv')

with open('resultados/Medidas_Dispersao.txt', 'w', encoding='utf-8') as f:
    f.write('----------------Salário-----------------\n')
    # Amplitude
    amplitude_salario = df['salario'].max() - df['salario'].min()

    # Variância
    variancia_salario = df['salario'].var()

    # Desvio Padrão
    desvio_padrao_salario = df['salario'].std()

    f.write("Amplitude: {}\n".format(amplitude_salario))
    f.write("Variância: {}\n".format(variancia_salario))
    f.write("Desvio Padrão: {}\n".format(desvio_padrao_salario))

    f.write('----------------Idade Atual-----------------\n')
    # Amplitude
    amplitude_idade_atual = df['idade_atual'].max() - df['idade_atual'].min()

    # Variância
    variancia_idade_atual = df['idade_atual'].var()

    # Desvio Padrão
    desvio_padrao_idade_atual = df['idade_atual'].std()

    f.write("Amplitude: {}\n".format(amplitude_idade_atual))
    f.write("Variância: {}\n".format(variancia_idade_atual))
    f.write("Desvio Padrão: {}\n".format(desvio_padrao_idade_atual))

    f.write('----------------Peso-----------------\n')
    # Amplitude
    amplitude_peso = df['peso'].max() - df['peso'].min()

    # Variância
    variancia_peso = df['peso'].var()

    # Desvio Padrão
    desvio_padrao_peso = df['peso'].std()

    f.write("Amplitude: {}\n".format(amplitude_salario))
    f.write("Variância: {}\n".format(variancia_salario))
    f.write("Desvio Padrão: {}\n".format(desvio_padrao_salario))
    
    f.write('----------------Altura-----------------\n')
    # Amplitude
    amplitude_altura_cm = df['altura_cm'].max() - df['altura_cm'].min()

    # Variância
    variancia_altura_cm = df['altura_cm'].var()

    # Desvio Padrão
    desvio_padrao_altura_cm = df['altura_cm'].std()

    f.write("Amplitude: {}\n".format(amplitude_altura_cm))
    f.write("Variância: {}\n".format(variancia_altura_cm))
    f.write("Desvio Padrão: {}\n".format(desvio_padrao_altura_cm))