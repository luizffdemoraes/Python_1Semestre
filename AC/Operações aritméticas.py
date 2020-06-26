"""
Escreva um programa em Python3 que receba um número real positivo e não nulo,
calcule e imprima o resultado das seguintes operações aritméticas:

A entrada será um número real positivo e não nulo. Não imprima nenhum texto para pedir o dado de entrada.



"""


n = float(input())

import math

i    = n ** 2
ii   = n ** math.exp(1)
iii  = n ** (1/2)
iv   = n ** (1/3)
v    = n ** (1/n)
vi   = math.exp(1) * n
vii  = math.pi / n
viii = math.log(n,7)
ix   = math.log(n, math.exp(1))
x    = math.log(n, math.pi)



print(f'i) {i}')
print(f'ii) {ii}')
print(f'iii) {iii}')
print(f'iv) {iv}')
print(f'v) {v}')
print(f'vi) {vi}')
print(f'vii) {vii}')
print(f'viii) {viii}')
print(f'ix) {ix}')
print(f'x) {x}')