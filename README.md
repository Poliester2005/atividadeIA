# Análise Completa da Base de Dados de Clientes

> Repositório para Pré Processamento de Dados de uma Base de Dados de Clientes para a realização de atividade complementar para Nota N2 da matéria de Inteligência Artificial e Apredizagem de Máquina da FATEC São Caetano do Sul - Antonio Russo

## Introdução

Para a realização de aprenizagem de máquina, é necessário de uma base de dados com dados mais claros possivel de acordo com o objetivo a ser alcançado para sua máquina ter maior porcentagem de acerto ao realizar a tarefa atribuída.

## Importando a Base

Ao pegar a base de dados atribuída a nossa equipe, utilizamos a biblioteca <a href="https://pandas.pydata.org/">Pandas</a> presente no Pacote de Bibloteca do <a href="https://python.org/">Python</a> para visualizar como a base se encontrava antes de fazer toda a parte de Pré Processamento dos Dados, utilizando o código abaixo:

```python
import pandas as pd
df = pd.read_csv('datasets/clientes.csv')

# Mudando a quantidade do máximos de linhas, colunas e tamanhos da base para ser mostrada.

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(df) # Mostrando a base
```

E o resultado obtido foi:



Com o resultado acima, concluímos que a base se encontrava ireegular para prosseguir, com diversos registros com valores ausentes, dados redundantes com duplicatas e dados incosistentes como idade negativa. Com isso, decidimos fazer toda a limpeza da base de dados utilizando métodos de limpeza dos dados.

## Limpeza dos Dados





## Nossa Equipe

Apresentamos nossa equipe, na qual contribuiu para esta atividade:

<table>
  <tr>
  <td align="center">
      <a href="https://github.com/brunocmartins11" title="Bruno Martins">
        <img src="https://avatars.githubusercontent.com/u/101012137?v=4" width="100px;" alt="Foto de Bruno Martins"/><br>
        <sub>
          <b>Bruno Martins</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Poliester2005" title="Eduardo Pielich">
        <img src="https://avatars.githubusercontent.com/u/107966984?v=4" width="100px;" alt="Foto de Eduardo Pielich"/><br>
        <sub>
          <b>Eduardo Pielich</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/RenatoAC2004" title="Renato Carvalho">
        <img src="https://avatars.githubusercontent.com/u/108144847?v=4" width="100px;" alt="Foto de Renato Carvalho"/><br>
        <sub>
          <b>Renato Carvalho</b>
        </sub>
      </a>
    </td>
  </tr>
</table>