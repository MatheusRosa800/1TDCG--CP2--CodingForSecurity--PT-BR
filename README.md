# FIAP - 2° Checkpoint - Conding for Security - DataShield

## Repositório em EN-US
[Link para o GitHub](https://github.com/MatheusRosa800/CP2---CodingForSecurity---EN-US)

## Introdução
Checkpoint realizado com o intuito de colocar em prática todos os conhecimentos manipulação de listas e estruturas de repetição adquiridos na matéria de Conding for Security, ministrada pelo [Professor Fábio Cabrini](https://www.linkedin.com/in/fabio-cabrini/).

## Participantes
- Eduardo dos Santos
- Jorge Gabriel
- Matheus Rosa
- Pedro Augusto

## Desafio
O desafio consiste criar um programa capaz de ler um arquivo de senhas e gerar uma lista de 1000 dados. A partir dessa lista, realizaremos a organização em ordem crescente utilizando algoritmos de mercado, tais como o ***Selection Sort***, ***Bubble Sort*** e ***Quick Sort***. Nosso objetivo final é avaliar a eficiência de cada algoritmo e identificar qual deles apresenta a maior velocidade de resposta.

## O que são algoritmos de ordenação?
Algoritmo de ordenação, em ciência da computação, é um algoritmo que coloca os elementos de uma dada sequência em uma certa ordem. Em outras palavras efetua sua ordenação completa ou parcial. O objetivo da ordenação é facilitar a recuperação dos dados de uma lista.

### Bubble Sort
O Bubble Sort é um algoritmo simples de ordenação que funciona percorrendo um vetor várias vezes. A cada iteração, ele compara o elemento atual com o elemento seguinte, e, caso esteja em uma ordem incorreta, troca de posição com o elemento seguinte.

O processo continua até que não haja mais trocas a serem realizadas, o que indica que a lista está ordenada.

Em nossos resultados esse algoritmo se mostrou o menos eficiente devido a quantidade de iteração dos elementos.

### Selection Sort
O Selection Sort é um algoritmo de ordenação simples que percorre um vetor de dados várias vezes, a cada passagem selecionando o menor elemento e colocando-o na posição correta. Ele funciona selecionando o menor elemento de uma lista e trocando-o com o primeiro elemento da lista. Em seguida, ele seleciona o segundo menor elemento e o troca com o segundo elemento da lista, e assim por diante, até que a lista esteja completamente ordenada.

### Quick Sort
O Quick Sort é um algoritmo de ordenação que utiliza o conceito de divisão e conquista para ordenar um conjunto de elementos. O algoritmo é conhecido por ser rápido e eficiente em relação a outros algoritmos de ordenação, especialmente para conjuntos de dados grandes.

O Quick Sort funciona dividindo o conjunto de dados em duas partes menores, de acordo com um elemento escolhido como pivô. Todos os elementos menores que o pivô são colocados à esquerda do pivô, e os elementos maiores são colocados à direita do pivô. Em seguida, o algoritmo é aplicado recursivamente a cada uma das partes menores, até que o conjunto esteja completamente ordenado.

A escolha do pivô é um fator crítico para a eficiência do algoritmo. O pivô ideal é o elemento mediano do conjunto, mas na prática é difícil encontrá-lo. Uma estratégia comum é escolher o primeiro ou o último elemento do conjunto como pivô, ou escolher um elemento aleatório.

Com base nas evidências (encontradas logo abaixo) esse algortimo é o mais eficiente
## Passo a passo para executar o programa

### 1° Passo - Abrir o terminal

### 2° Passo - Obter o projeto do github
Para obter os arquivos digite o comando: 
```
git clone https://github.com/MatheusRosa800/CP2---Coding-for-Security---PT-BR.git
cd CP2---Coding-for-Security---PT-BR
```
### 3° Passo - Execute o comando abaixo para abrir o programa Python
```
python3 escolha.py
```
### 4° Passo - Escreva a quantidade de números que deseja ver
![Imagem do programa](https://i.ibb.co/JCs59J3/cod.png)
## Youtube
[Link para o Youtube](https://www.youtube.com/watch?v=wFsU3rTPcH8&ab_channel=PedroAugusto)

## Dashboard de avaliação de performance dos algoritmos
Todos os algoritmos propostos foram submetidos a dez testes exaustivos, com os resultados sendo registrados para posterior análise do nível de entrega da lista.

### Ambiente
Sistema operacional: Windows 10
Processador: Intel Pentium G4560 3.5Ghz
RAM: 16GB
SSD: 128GB

### Resultados
Com base nos resultados, é notório a performance do algoritmo ***Quick Sort*** que está a frente dos outros dois.

Seguem as evidências:

Evidência 01
![Imagem do programa](https://github.com/MatheusRosa800/CP2---CodingForSecurity---PT-BR/blob/main/evidencia-1.png)

Evidência 02
![Imagem do programa](https://github.com/MatheusRosa800/CP2---CodingForSecurity---PT-BR/blob/main/evidencia-2.png)
