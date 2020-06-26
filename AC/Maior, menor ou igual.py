"""
Dados dois números inteiros A e B, exibir:

- 'A eh maior', se A for maior do que B;

- 'B eh maior', se B for maior do que A;

- 'iguais', se os números forem iguais.

Na primeira linha o número inteiro correspondente ao A; na segunda linha o número inteiro correspondente ao B.

A frase 'A eh maior' (sem aspas) ou 'B eh maior' (sem aspas) ou 'iguais' (sem aspas), de acordo com o caso.
"""

a = int(input())
b = int(input())

if a > b:
    print('A eh maior')
elif b > a:
    print('B eh maior')
else:
    print('iguais')