def usar():

    print("-" * 54)
    print("  Bem-vindo ao 3º Algoritmo de Ordenação Alfabética")
    print("-" * 54)

    data_list = open('mil_senhas.txt','r+')
    linhas = data_list.readlines()

    data_list = [linha.strip('\n') for linha in linhas]
    new_list = []

    while data_list:
        minimum = data_list[0]  
        for x in data_list: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)   

    print("-" * 160)
    print("LISTA ORDENADA COM SUCESSO !!! \n\n",new_list)
    print("-" * 160)


if (__name__ == "__main__"):
    usar()