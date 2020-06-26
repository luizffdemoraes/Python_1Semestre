"""
Escreva um programa que receba as notas e a presença de um aluno, calcule a média e imprima a situação final do aluno.

No semestre são feitas 3 provas, p1, p2 e p3, e faz-se a média ponderada com pesos 2, 2 e 3, respectivamente.

Os critérios para aprovação são:

1 - Frequência mínima de 75%.

2 - Média final mínina de 6.0 (calculada com uma casa de precisão).

E devem ser considerados os casos especiais descritos para a impressão dos resultados, com uma mensagem personalizada para cada situação.

A entrada serão três números reais no intervalo de 0 a 10, representando as notas do aluno, e um número real no intervalo de 0 a 1 representando a frequência.

Não imprima nenhum texto para pedir os dados ao usuário.

A saída do programa será um texto com a frequência e a média final do aluno, seguido de uma mensagem referente a sua situação no curso. Exemplo:

Frequencia: 78%
Media final: 6.5
<mensagem>
Se o aluno for reprovado por faltas, a mensagem deve ser:

Aluno reprovado por faltas!
Caso contrário, temos 4 possibilidades de mensagens:

a) aluno aprovado com média superior a 9 (não inclusivo):

Aluno aprovado com louvor!
b) aluno aprovado com média superior a 6 (inclusivo) e inferior a 9 (inclusivo):

Aluno aprovado!
c) aluno reprovado com média superior a 4 (inclusivo) e inferior a 6 (não inclusivo):

Aluno de recuperação!
b) aluno reprovado com média inferior a 4 (não inclusivo):

Aluno reprovado!
"""

n1 = float(input())
n2 = float(input())
n3 = float(input())
f = float(input())
fq = round(f * 100, 0)

m = round(((n1 * 2) + (n2 * 2) + (n3 * 3)) / 7, 1)

print('Frequencia: {:.0f}%'.format(f * 100))
print(f'Media: {m}')

if fq < 75:
	print('Aluno reprovado por faltas!')
elif m >  9:
	print('Aluno aprovado com louvor!')
elif m >= 6:
	print('Aluno aprovado!')
elif m >= 4:
	print('Aluno de recuperação!')
else:
	print('Aluno reprovado!')
