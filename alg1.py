def usar():

    print("-" * 54)
    print("  Bem-vindo ao 1º Algoritmo de Ordenação Alfabética")
    print("-" * 54)

    arq = open('mil_senhas.txt','r+')
    linhas = arq.readlines()

    arr = [linha.strip('\n') for linha in linhas]

    for i in range(len(arr)):
        indice_minimo = i
        for j in range(i+1, len(arr)):
            if arr[indice_minimo] > arr[j]:
                indice_minimo = j
        
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

    print("-" * 160)
    print("LISTA ORDENADA COM SUCESSO !!! \n\n",arr)
    print("-" * 160)

    arq.close()

if (__name__ == "__main__"):
    usar()
