'''''
Integrantes:
- Matheus Rosa
- Jorge Ricci
- Pedro Augusto
- Eduardo Almeida
'''

import alg1
import alg2
import alg3


def abrir_arquivo():
    arq = open('mil_senhas.txt','r+')
    linhas = arq.readlines()

    lista = [linha.strip('\n') for linha in linhas]

def escolher_alg():
    print("-" * 35)
    print("     Algoritmos de ordenação    ")
    print("-" * 35)

    print("    (1)    |   (2)   |   (3)  \n")

    alg = int(input('Escolha qual algoritmo você deseja usar \n 1 - Quick Sort \n 2 - Bubble Sort \n 3 - Selection Sort2 \n '))

    if (alg == 1):
        print("-" * 35)
        print('  Iniciando o Algoritmo 1  ')
        print("-" * 35)
        alg1.usar()

    elif (alg == 2):
        print("-" * 35)
        print("  Iniciando o Algoritmo 2  ")  
        print("-" * 35)
        alg2.usar() 

    elif (alg == 3):
        print("-" * 35)
        print("  Iniciando o Algoritmo 3  ")  
        print("-" * 35)
        alg3.usar() 

if (__name__ == "__main__"):
    escolher_alg()
