"""
Descrição
Tia Joana é uma respeitada professora e tem vários alunos. Em sua última aula, ela prometeu que iria sortear um aluno
para ganhar um bônus especial na nota final: ela colocou N pedaços de papel numerados de 1 a N em um saquinho e sorteou
um determinado número K; o aluno premiado foi o K-ésimo aluno na lista de chamada do diário de classe, a qual contém os nomes em ordem alfabética.

O problema é que a Tia Joana esqueceu o diário de classe, então ela não tem como saber quem é o K-ésimo aluno na lista de presença.
 Porém, os alunos dela estão muito ansiosos e querem logo saber quem foi o vencedor. Por isso eles decidiram fazer um programa de
  computador para ler os dados de suas carteiras de estudante (nome e matrícula) e colocar todos os alunos em ordem alfabética.
  Desta forma eles poderiamdescobrir quem é o K-ésimo aluno na lista, isto é, quem foi o ganhador.

Portanto, seu trabalho é criar um programa de computador, que a partir das matrículas e nomes dos alunos da Tia Joana e do número sorteado,
determine a matrícula e o nome do aluno que deve receber o bônus.

Formato de entrada

A primeira linha contém dois inteiros N e K separados por um espaço em branco (1 ≤ K ≤ N ≤ 100).
Cada uma das N linhas seguintes contém uma matrícula (até 6 dígitos) e uma cadeia de caracteres de tamanho mínimo 1
e máximo 20 representando os nomes dos alunos. Os nomes são compostos apenas por letras minúsculas de 'a' a 'z'.

Formato de saída

Seu programa deve imprimir duas linhas, a primeira contendo o número de matrícula e outra o nome do aluno, seguindo a formatação contida no exemplo.
"""

# Parte 1
def Valid(n1, k2):
    return n1 >= 1 and k2 <= 100


def Valid_Matricula(mat):
    return len(mat) > 0 and len(mat) < 7


def Valid_Nome(name):
    return len(name) > 0 and len(name) < 21


def ordenar(l):
    l1 = sorted(l)
    return l1


lista = []
lista_nome = []
lista_ordenada = []
lista_matricula = []
# Parte 1
valor1, valor2 = input().split(" ", 1)
n = int(valor1)
k = int(valor2)

while not(Valid(n, k)):
    valor1, valor2 = input().split(" ", 1)
    n = int(valor1)
    k = int(valor2)

# Parte 2
for item in range(n):
    matricula, nome = input().split("-", 1)

    if Valid_Matricula(matricula):
        lista_matricula.append(matricula)
    if Valid_Nome(nome):
        lista_nome.append(nome)

# Parte 3
lista_ordenada = ordenar(lista_nome)
posicao = lista_ordenada[k - 1]

# Parte 4
for item in range(len(lista_nome)):
    if posicao == lista_nome[item]:
        posicao_number = item


print(f'Matricula: {lista_matricula[posicao_number]}')
print(f'Nome: {lista_ordenada[k - 1]}')

