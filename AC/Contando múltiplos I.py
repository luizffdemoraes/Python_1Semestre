"""
Faça um programa que receba dois inteiros x e n, com x, n > 0 e x < n, e conte o número de múltplos de x menores do que n.



DICA 1: Os múltiplos de um número são obtidos multiplicando-se esse número pelos números naturais (1, 2, 3, 4, 5, ...)

DICA 2: No primeiro exemplo, os múltiplos de são: 7*1, 7*2, 7*3, 7*4, 7*5, .... --> 7, 14, 21, 28, 35, ... Sendo assim,
temos 3 múltiplos que são estritamente menores que 28, já que o quarto múltiplo é o próprio 28 (portanto = e não < ).

DICA 3: Use um laço de repetição para ir percorrendo os números inteiros e um acumulador para contar +1 para cada múltiplo encontrado,
parando quando o múltiplo da vez for igual ao número limite dado (ou seja, deve executar enquando ele for menor).

Formato de entrada

A entrada consiste em dois números inteiros x e n, nessa ordem e separados por uma quebra de linha.

Considere que:

x, n > 0
x < n
Mas não é necessário validar a entrada.

Formato de saída

A saída deve ser a expressão a seguir:

O numero <x> tem <y> multiplos menores que <n>.
Onde os termos entre < > devem ser substituídos pelos valores encontrados para cada caso.
"""

v1 = int(input())
v2 = int(input())
x = 1
while v1 * x < v2:
    x = x + 1

print(f'O numero {v1} tem {x-1} multiplos menores que {v2}.')

