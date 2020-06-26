"""
Descrição
Escreva um programa em Python3 que receba a altura de 4 pessoas, calcule e imprima a média final.

Formato de entrada

As entradas serão números reais positivos não nulos. Não deve ser impresso nenhum texto para pedir os dados de entrada.

Formato de saída

A saída devera ser formatada conforme o exemplo:

A media das alturas eh: <valor>
onde <valor> será substituído pelo resultado calculado.

OBS.: Atenção aos acentos no texto de saída.

o The Huxley não aceita caracteres acentuados mesmo nas strings
"""

a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())

media = (a1 + a2 + a3 + a4) / 4


print(f'A media das alturas eh: {media}')
