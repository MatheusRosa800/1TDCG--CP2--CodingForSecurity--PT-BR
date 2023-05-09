def selection_sort(lista):
    nova_lista = []
    while lista:
        minimum = lista[0]
        for x in lista:
            if x < minimum:
                minimum = x
        nova_lista.append(minimum)
        lista.remove(minimum)

    return nova_lista


def usar(lista):

    print("-" * 54)
    print("  Bem-vindo ao Algoritmo de Ordenação Selection Sort")
    print("-" * 54)

    lista = selection_sort(lista)

    print("-" * 160)
    print("LISTA ORDENADA COM SUCESSO !!! \n\n", lista)
    print("-" * 160)
