"""
Escreva um programa em Python3 que peça o valor do lado de um hexágono regular, calcule e imprima sua área e seu perímetro.

Sabemos que um hexágono regular é o polígono de 6 lados iguais e com todos os ângulos internos iguais entre si.

Sabemos ainda que um hexágono regular de lado L é formado por 6 triângulos equiláteros de lado L,
e que a área de 1 triângulo equilátero de lado L é dada por:

A entrada poderá ser qualquer número real positivo.

Sendo valor 1, 2 e 3 respectivamente os valores do lado, da área e do perímetro do hexágono.

Dica: Usem um print() para cada linha da resposta, não usem o '\n'.
"""

import math
valor1 = float(input())
valor2 = round(6 * valor1 ** 2 * math.pow(3, 1/2) / 4, 20)
valor3 = valor1 * 6


print(f'Lado do hexagono: {valor1} metros,')
print(f'Area: {valor2} metros quadrados,')
print(f'Perimetro: {valor3} metros.')