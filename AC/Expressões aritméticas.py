"""
Escreva um programa em Python3 que receba quatro números reais (a, b, c, d) e reproduza as seguintes expressões algébricas:

As entradas poderão ser quaisquer números reais, positivos ou negativos mas não nulos.

Não imprima nenhum texto para pedir os dados de entrada.

A saída deve conter o número do item e o valor calculado arredondado para a 4a. casa de precisão, para todos os itens.

Para arredondar um número em Python3 usamos a função:

Que retorna o valor de n arredondado para d casas após a vírgula. Se d for omitido, é feito o arredondamento para um número inteiro.

Obs.: Essa função não faz parte do módulo de matemática, podendo ser acessada diretamente.

"""

import math
a = float(input())
b = float(input())
c = float(input())
d = float(input())

resp1 = round((a ** 2 + 3 * b) / c + d, 4)
resp2 = round(math.log10(a) + math.exp(1) ** (-b/c) - d**2/math.pi, 4)
resp3 = round((math.pow(a**2, (1/3)) * b**(1/3) + c * d) / (a + b + c + d), 4)
resp4 = round(((a+b)*(c+d))/(a*b*c*d), 4)
resp5 = round(((a**2 + b**2)/(c*d))-((c**2+d**2)/(a*b)), 4)
resp6 = round(math.pow(a+b+c+d, 2), 4)
resp7 = round(math.pow(a, 2) + math.pow(b, 2) + math.pow(c, 2) + math.pow(d, 2), 4)
resp8 = round(math.pow((a*b*c*d), (1/3)), 4)

print(f'i) {resp1}')
print(f'ii) {resp2}')
print(f'iii) {resp3}')
print(f'iv) {resp4}')
print(f'v) {resp5}')
print(f'vi) {resp6}')
print(f'vii) {resp7}')
print(f'viii) {resp8}')