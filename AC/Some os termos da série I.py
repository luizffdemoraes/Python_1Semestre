"""
Escreva um programa em Python 3 para somar os n primeiros termos da seguinte série:

DICA: Aqui todas as frações são somadas, mas como calcular o denominador? Tente primeiro fazer a exibição apenas dos denominadores.

Os denominaores são: 1, 4, 9, 16, 25, 36, .... qual a relação entre eles e a posição dos números?

Compare com a posição: 1, 2, 3, 4, 5, 6, ....

Formato de entrada

A entrada será um número natural n > 0.

Formato de saída

A saída deve ser uma unica linha contendo apenas o resultado da somatória formatado para exibir 6 casas de precisão.

"""

n = int(input())
x = 1
soma = []
total = 0

while x <= n:
    soma.append(float(1/(x * x)))
    x = x + 1

total = sum(soma)
print(f'{total:.6f}')
