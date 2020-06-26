"""
Descrição
Dada duas listas encadeadas A e B, escreva uma função para verificar se B é um subconjunto de A.

Formato de entrada
A primeira linha de entrada será o tamanho da primeira lista (número inteiro). Em seguida, uma lista com n números inteiros. A terceira linha de entrada é o tamanho da segunda lista (número inteiro). Por fim, uma lista com m números inteiros. Nesse caso, m e n podem assumir valores iguais ou diferentes.

Formato de saída

0 caso não seja subconjunto; 1 caso contrário.
"""

def validacao(numero):
    lista = []
    inteiro = input().split()

    for item in range(numero):
        if inteiro[item].isnumeric():
            number = inteiro[item]
            lista.append(int(number))

    return(lista)


listaA = []
listaB = []
n = int(input())

listaA = validacao(n)
while listaA is None or listaA == [] or len(listaA) < n:
    listaA = validacao(n)

n = int(input())
listaB = validacao(n)
while listaB is None or listaB == [] or len(listaB) < n:
    listaB = validacao(n)

if (all([z in listaA for z in listaB])) == True:
    print("1")
else:
    print("0")
