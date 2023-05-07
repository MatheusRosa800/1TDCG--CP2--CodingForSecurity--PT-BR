import alg1
import alg2
import alg3

def escolher_alg():
    print("-" * 35)
    print("     Algoritmos de ordenação ")
    print("-" * 35)

    print("    (1)    |   (2)   |   (3)  \n")

    alg = int(input('Escolha qual algoritmo você deseja usar (1, 2, 3): '))

    if (alg == 1):
        print("-" * 35)
        print('  Iniciando o Algoritmo 1')
        print("-" * 35)
        alg1.usar()
    elif (alg == 2):
        print("-" * 35)
        print("  Iniciando o Algoritmo 2")  
        print("-" * 35)
        alg2.usar() 
    elif (alg == 3):
        print("-" * 35)
        print("  Iniciando o Algoritmo 3")  
        print("-" * 35)
        alg3.usar() 

if (__name__ == "__main__"):
    escolher_alg()
