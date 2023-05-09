def bubble_sort(lista):
    invers = True
    while invers:
        invers = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                c = lista[i + 1]
                lista[i + 1] = lista[i]
                lista[i] = c
                invers = True

    return lista


def usar(lista):

    print("-" * 54)
    print("  Bem-vindo ao Algoritmo de Ordenação Bubble Sort")
    print("-" * 54)

    lista = bubble_sort(lista)

    print("-" * 160)
    print("LISTA ORDENADA COM SUCESSO !!! \n\n", lista)
    print("-" * 160)
