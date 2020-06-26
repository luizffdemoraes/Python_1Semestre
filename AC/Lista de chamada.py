"""
Descrição
Tia Joana é uma respeitada professora e tem vários alunos. Em sua última aula, ela prometeu que iria sortear um aluno para ganhar um bônus especial na nota final: ela colocou N pedaços de papel numerados de 1 a N em um saquinho e sorteou um determinado número K; o aluno premiado foi o K-ésimo aluno na lista de chamada.
O problema é que a Tia Joana esqueceu o diário de classe, então ela não tem como saber qual número corresponde a qual aluno. Ela sabe os nomes de todos os alunos, e que os números deles, de 1 até N, são atribuídos de acordo com a ordem alfabética, mas os alunos dela estão muito ansiosos e querem logo saber quem foi o vencedor.
Dado os nomes dos alunos da Tia Joana e o número sorteado, determine o nome do aluno que deve receber o bônus.

Formato de entrada

A primeira linha contém dois inteiros N e K separados por um espaço em branco (1 <= K <= N <= 100). Cada uma das N linhas seguintes contém uma cadeia de caracteres de tamanho mínimo 1 e máximo 20 representando os nomes dos alunos. Os nomes são compostos apenas por letras minúsculas de 'a' a 'z'.

Formato de saída

Seu programa deve imprimir uma única linha, contendo o nome do aluno que deve receber o bônus.
"""

def Valid(n1, k2):
    return n1 >= 1 and k2 <= 100

def verificacao(N, K):
    while N > 100 and K < 1:
        valor1, valor2 = input().split(" ", 1)
        N = int(valor1)
        K = int(valor2)
        return(N, K)

def ordenar(l):
    l1 = sorted(l)
    return l1


lista = []
lista_ordenada = []
nek = []

valor1, valor2 = input().split(" ", 1)
n = int(valor1)
k = int(valor2)

while not(Valid(n, k)):
    valor1, valor2 = input().split(" ", 1)
    n = int(valor1)
    k = int(valor2)

for item in range(n):
    lista.append(input())

lista_ordenada = ordenar(lista)

print(lista_ordenada[k - 1])

