import time

def usar():

    inicio = time.time()

    print("-" * 54)
    print("  Bem-vindo ao 2º Algoritmo de Ordenação Alfabética")
    print("-" * 54)

    arq = open('mil_senhas.txt','r+')
    linhas = arq.readlines()

    lista = [linha.strip('\n') for linha in linhas]

    invers = True
    while invers:
        invers = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                c = lista[i+1]
                lista[i+1] = lista[i]
                lista[i] = c
                invers = True

    print("-" * 160)
    print("LISTA ORDENADA COM SUCESSO !!! \n\n",lista)
    print("-" * 160)

    arq.close()

    fim = time.time()

    print("Tempo de execução:", fim - inicio, "segundos")

if (__name__ == "__main__"):
    usar()