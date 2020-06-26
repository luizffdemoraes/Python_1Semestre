"""
Descrição
O objetivo desse problema é a implementação de funções que indiquem se um determinado ano é ou não bissexto.

Para cada ano fornecido ao programa, faz-se necessário, primeiro, identificar se o ano fornecido é um valor inteiro de 4 dígitos e, segundo, dado que o ano é um número válido, informar se é ou não um ano bissexto.

Um ano é bissexto se ele satisfaz as seguintes condições:

É divisível por 4 e,
Não é divisível por 100 ou é divisível por 400.
A sua tarefa é construir uma solução com três funções (3): contaDigitos, ehBissexto e Mensagem.
Formato de entrada

A entrada consiste numa lista de valores separados por um espaço em branco.

Formato de saída

Para cada valor da entrada uma mensagem deve ser exibida.

Se o valor é um ano bissexto mas for um ano anterior ao ano atual: O ano xxxx foi bissexto
Se o valor é um ano bissexto mas for um ano posterior ao ano atual: O ano xxxx serah bissexto
Se o valor não é um ano bissexto: O ano xxxx NAO eh bissexto
Se o número não é um ano de 4 dígitos: Ano invalido
"""

def verificacao(year, atual):
    numero = len(year)
    for item in range(numero):
        x = int(year[item])
        lista.append(x)
    for item in range(numero):
        if lista[item] < 1000:
            print("Ano invalido")
        elif lista[item] < atual and lista[item] % 4 == 0 and lista[item]  % 100 != 0 or lista[item]  % 400 == 0:
            print("O ano {} foi bissexto".format(lista[item]))
        elif lista[item] >= atual and lista[item] % 4 == 0 and lista[item]  % 100 != 0 or lista[item]  % 400 == 0:
            print("O ano {} serah bissexto".format(lista[item]))
        else:
            print("O ano {} NAO eh bissexto".format(lista[item]))



from datetime import date
data_atual = date.today().year

lista = []
ano = input().split()
verificacao(ano, data_atual)
