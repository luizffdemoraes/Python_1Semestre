"""
Descrição
Crie um programa que tenha uma única função, além da principal, que receberá como parâmetro uma string não vazia s (com no máximo 50 caracteres de conteúdo) e exibirá a quantidade de caracteres de s. Observações: (a) apenas um laço de repetição; (b) sem matrizes auxiliares; (c) não usar funções prontas; (d) função iterativa.

Formato de entrada

A casa amarela

Formato de saída

14
"""

def contarLetras(s):
    vogais = int(0)
    consoantes = int(0)
    space = int(0)
    total = int(0)

    for caracter in s:
        if caracter in 'aeiou':
            vogais = vogais + 1
        elif caracter in ' ':
            space = space + 1
        else:
            consoantes = consoantes + 1
        total = vogais + consoantes + space

    return(total)


s = str(input())
resp = contarLetras(s)

if resp > 50:
    s = str(input())
    resp = contarLetras(s)

print(resp)

