"""
Descrição
Faça um programa que leia a idade (valor inteiro) de uma pessoa e informe sua classe eleitoral:

nao eleitor (abaixo de 16 anos)
eleitor obrigatorio (maior e igual a 18 ou menor e igual a 65 anos)
eleitor facultativo (entre 16 e 18 anos ou acima dos 65 anos)

Formato de entrada

Consiste de um número inteiro indicando a idade da pessoa.

Formato de saída

Uma linha escrito:

"nao eleitor", "eleitor obrigatorio" ou "eleitor facultativo" (sem as aspas) de acordo com o critério da descrição.
"""

idade = int(input())
if idade < 16:
    print('nao eleitor')
elif idade >= 18 and idade <= 65:
    print('eleitor obrigatorio')
else:
    print('eleitor facultativo')
