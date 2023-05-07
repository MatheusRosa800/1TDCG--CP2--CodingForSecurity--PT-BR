import time
import escolha

def usar():

    inicio = time.time()

    print("-" * 54)
    print("  Bem-vindo ao Algoritmo de Ordenação Selection Sort")
    print("-" * 54)

    #arq = open('mil_senhas.txt','r+')
    #linhas = arq.readlines()

    #lista = [linha.strip('\n') for linha in linhas]

    escolha.abrir_arquivo()

    new_list = []

    while lista:
        minimum = lista[0]  
        for x in lista: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        lista.remove(minimum)   

    print("-" * 160)
    print("LISTA ORDENADA COM SUCESSO !!! \n\n",new_list)
    print("-" * 160)

    fim = time.time()

    print("Tempo de execução:", fim - inicio, "segundos")


if (__name__ == "__main__"):
    usar()