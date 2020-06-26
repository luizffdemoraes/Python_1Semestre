"""
Descrição
Leia um valor de ponto flutuante com duas casas decimais, que representa um valor em dinheiro. A seguir,
calcule o menor número de notas e moedas no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2.
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Formato de entrada

A entrada será um valor em ponto flutuante N, com 0 < N ≤ 1000000.00. (Não é necessário validar)

Formato de saída

Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplos dados.
Note que são impressas apenas as linhas cujo número de notas ou moedas é diferente de zero.



DICA: Se o seu programa calcula errado o número das moedas menores, pense em trabalhar os valores mudando a unidade,
assim não precisamos lidar com números decimais. É o que fazemos na prática,
 falando em números inteiros tanto pros reais quanto pros centavos.
"""

import math

valor = float(input())

n100 = math.floor(valor / 100)
valor = valor - (n100 * 100)
if n100 > 0:
    print(f'{n100} nota(s) de R$ 100.00')
n50 = math.floor(valor / 50)
valor = valor - (n50 * 50)
if n50 > 0:
    print(f'{n50} nota(s) de R$ 50.00')
n20 = math.floor(valor / 20)
valor = valor - (n20 * 20)
if n20 > 0:
    print(f'{n20} nota(s) de R$ 20.00')
n10 = math.floor(valor / 10)
valor = valor - (n10 * 10)
if n10 > 0:
    print(f'{n10} nota(s) de R$ 10.00')
n5 = math.floor(valor / 5)
valor = valor - (n5 * 5)
if n5 > 0:
    print(f'{n5} nota(s) de R$ 5.00')
n2 = math.floor(valor / 2)
valor = valor - (n2 * 2)
if n2 > 0:
    print(f'{n2} nota(s) de R$ 2.00')

m1 = math.floor(valor / 1)
valor = valor - (m1 * 1)
if m1 > 0:
    print(f'{m1} moeda(s) de R$ 1.00')
m050 = math.floor(valor / 0.50)
valor = valor - (m050 * 0.50)
if m050 > 0:
    print(f'{m050} moeda(s) de R$ 0.50')
m025 = math.floor(valor / 0.25)
valor = valor - (m025 * 0.25)
if m025 > 0:
    print(f'{m025} moeda(s) de R$ 0.25')
m010 = math.floor(round(valor / 0.1, 2))
valor = valor - (m010 * 0.1)
if m010 > 0:
    print(f'{m010} moeda(s) de R$ 0.10')
m005 = math.floor(round(valor / 0.05, 2))
valor = valor - (m005 * 0.05)
if m005 > 0:
    print(f'{m005} moeda(s) de R$ 0.05')
m001 = math.floor(round(valor / 0.01, 2))
valor = valor - (m001 * 0.01)
if m001 > 0:
    print(f'{m001} moeda(s) de R$ 0.01')
