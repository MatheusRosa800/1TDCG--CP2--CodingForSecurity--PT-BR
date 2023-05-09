def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


def usar(lista):

    print("-" * 54)
    print("  Bem-vindo ao Algoritmo de Ordenação Quick Sort")
    print("-" * 54)

    lista = quick_sort(lista)

    print("-" * 160)
    print("LISTA ORDENADA COM SUCESSO !!! \n\n", lista)
    print("-" * 160)

