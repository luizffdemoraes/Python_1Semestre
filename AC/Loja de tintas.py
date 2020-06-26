"""
Imagine que você fora contratado para fazer um programa para uma loja de tintas, com o objetivo de calcular quantas latas de tinta são necessárias para pintar uma determinada área e calcular o preço final da compra.

A loja trabalha com latas de tinta de:
24 litros, vendidas a R$91,00 cada e,
5.4 litros, vendidas a R$23,00 cada.
Sabe-se ainda que cada litro de tinta cobre uma superfície de 7 metros quadrados.

Faça um programa que receba o valor da área a ser pintada em metros quadrados, calcule e imprima:

a) A quantidade de latas de tinta e o preço final, considerando apenas latas de 24 litros.
b) A quantidade de latas de tinta e o preço final, considerando apenas latas de 5.4 litros.
c) A quantidade de latas de tinta e o preço final, considerando ambas as latas, de 24 e 5.4 litros.

A entrada será um número real positivo não nulo, não deve ser impresso nenhum texto para pedir os dados de entrada.

Com o número de latas impresso como número inteiro e o custo final impresso com duas casas decimais.

Dicas:

Usem as funções math.ceil(n) e math.floor(n) para arredondar os números para os inteiros acima e abaixo de n, respectivamente.
Usem o método str.format() para formatar a string e definir o número de casas decimais dos números a serem impressos.
"""

import math
area = float(input())
lata_G  = math.ceil(area / 168)
lata_Pq = math.ceil(area / 37.8)
# floor da um numero inteiro com arredondamento
lata_Gt  = math.floor(area / 168)
# ceil ele da um numero arredondando para em numeros fracionados antes do .
lata_Pqt = math.ceil((area - (lata_Gt * 168)) / 37.8)

print(f'a) {lata_G} lata(s) de 24 litros: R$ {lata_G * 91}.00')
print(f'b) {lata_Pq} lata(s) de 5.4 litros: R$ {lata_Pq * 23}.00')
print(f'c) {lata_Gt} lata(s) de 24 litros e {lata_Pqt} lata(s) de 5.4 litros: R$ {(lata_Gt * 91) + (lata_Pqt * 23)}.00')
