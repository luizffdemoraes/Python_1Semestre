"""
Descrição
Luíz Carlos é um carteiro muito comprometido com seu trabalho. Ele participou de uma reunião recente em que foi informado de que deveria entregar pelo menos 100 correspondências por dia para dar conta do grande fluxo de envios na época de Natal.

Escreva um programa que receba como entrada a quantidade de correspondências entregues por ele em cada um dos sete dias da semana, e exiba em quantos dias ele cumpriu a meta, e a média de entregas diárias que ele fez no período.



Formato de entrada

Valores inteiros

Formato de saída

Um valor inteiro para a quantidade de dias, e outro valor inteiro para a média de entregas
"""

cartas = []
soma = 0
total = 0
i = 0
for x in range(1, 8):
    cartas = int(input())
    total = total + cartas
    if cartas >= 100:
        i = i + 1
        soma = soma + cartas
print(i)
print(f'{total / 7:.0f}')