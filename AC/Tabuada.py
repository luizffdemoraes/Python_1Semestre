"""
Descrição
Faça um programa que leia um número inteiro e imprima a tabuada de multiplicação deste número. Suponha que o número lido da entrada é maior que zero.

Formato de entrada

Um número inteiro.

Formato de saída

A tabuada de multiplicação correspondente ao número digitado. Verifique o exemplo de saída para a especificação do formato.

"""

n = int(input())
x = 1
for x in range(1,10):
    print("{} X {} = {}".format(n, x, n*x))

