"""
Integrantes:
- Matheus Rosa
- Jorge Ricci
- Pedro Augusto
- Eduardo Almeida
"""

import alg1
import alg2
import alg3
import time
import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd

def abrir_arquivo():
    arq = open('mil_senhas.txt','r+')
    linhas = arq.readlines()

    lista = [linha.strip('\n') for linha in linhas]

    arq.close()

    return lista


def escolher_alg():

    print("-" * 55)
    print("           Algoritmos de ordenação crescente    ")
    print("-" * 55)

    print("   Quick Sort   |   Bubble Sort   |   Selection Sort  \n")

    # Entrada de dado do usuário
    while True:

        print('Digite o número de qual algoritmo você deseja testar:')
        print(' 1 - Quick Sort \n 2 - Bubble Sort \n 3 - Selection Sort \n 4 - Testar todos os algoritmos \n ')

        try:
            alg = input('Resposta: ')
            alg = int(alg)

            if alg > 4 or alg < 1:
                print("-" * 70)
                print('[ ERRO ] Opção inválida, digite apenas entre os números: 1 | 2 | 3')
                print("-" * 70)
            else:
                break

        except ValueError:
            print("-" * 55)
            print('[ ERRO ] Por favor, digite apenas números inteiros.')
            print("-" * 55)

    # Leitura do arquivo de senhas
    lista = abrir_arquivo()

    # Validação de opção do usuário
    if alg == 1:
        print("-" * 30)
        print('  Iniciando o Algoritmo 1  ')
        print("-" * 30)

        inicio = time.time()
        alg1.usar(lista)
        fim = time.time()

        print("Tempo de execução:", fim - inicio, "segundos")

    elif alg == 2:
        print("-" * 30)
        print("  Iniciando o Algoritmo 2  ")  
        print("-" * 30)

        inicio = time.time()
        alg2.usar(lista)
        fim = time.time()

        print("Tempo de execução:", fim - inicio, "segundos")

    elif alg == 3:
        print("-" * 30)
        print("  Iniciando o Algoritmo 3  ")  
        print("-" * 30)

        inicio = time.time()
        alg3.usar(lista)
        fim = time.time()

        print("Tempo de execução:", fim - inicio, "segundos")

    elif alg == 4:

        results = {'Bubble Sort': [], 'Quick Sort': [], 'Selection Sort': []}

        for i in range(10):

            print("-" * 55)
            print(f"{str(i + 1)}° teste realizado:")
            print("-" * 55)
            inicio = time.time()
            lista_ordenada = alg1.quick_sort(lista.copy())
            fim = time.time()

            print('Quick sort')
            print(lista_ordenada)

            results['Quick Sort'].append(fim - inicio)

            inicio = time.time()
            lista_ordenada = alg2.bubble_sort(lista.copy())
            fim = time.time()

            print('\n Bubble sort')
            print(lista_ordenada)

            results['Bubble Sort'].append(fim - inicio)

            inicio = time.time()
            lista_ordenada = alg3.selection_sort(lista.copy())
            fim = time.time()

            print('\n Selection sort')
            print(lista_ordenada)

            results['Selection Sort'].append(fim - inicio)

        # Cria um DataFrame com os resultados
        df = pd.DataFrame.from_dict(results)

        # Cria um gráfico de barras com os resultados
        data = [go.Bar(x=df.columns, y=df.iloc[i], name=f'Teste {i + 1}') for i in range(10)]
        layout = go.Layout(title='Comparação de Algoritmos de Ordenação', xaxis=dict(title='Algoritmo'),
                           yaxis=dict(title='Tempo (s)'))
        fig = go.Figure(data=data, layout=layout)

        # Exibe o dashboard com o gráfico
        pyo.plot(fig, filename='sorting-algorithms.html')


if __name__ == "__main__":
    escolher_alg()
