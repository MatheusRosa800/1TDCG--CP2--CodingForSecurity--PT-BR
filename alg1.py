import time
import escolha

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

def usar():
    inicio = time.time()

    print("-" * 54)
    print("  Bem-vindo ao Algoritmo de Ordenação Quick Sort")
    print("-" * 54)

   # arq = open('mil_senhas.txt', 'r')
    #linhas = arq.readlines()

    #lista = [linha.strip('\n') for linha in linhas]

    escolha.abrir_arquivo()

    lista = quick_sort(lista)

    print("-" * 160)
    print("LISTA ORDENADA COM SUCESSO !!! \n\n", lista)
    print("-" * 160)

    arq.close()

    fim = time.time()

    print("Tempo de execução:", fim - inicio, "segundos")

if __name__ == "__main__":
    usar()