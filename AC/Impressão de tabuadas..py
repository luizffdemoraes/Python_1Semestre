"""
Descrição
Faça um programa de resolução de tabuada. O programa deve inicialmente receber 2 números que indicam de quais números
devem ser impressas a tabuada. Por exemplo, se forem recebidos os valores 2 e 5, seu programa deve imprimir a tabuada de 2, 3, 4 e 5.
O programa só deve aceitar valores entre 1 e 9. Enquanto o usuário digitar valores que não sejam esses, emita uma mensagem de erro.

Formato de entrada

Dois números em 2 linhas distintas indicando o intervalos dos números das tabuadas.

Formato de saída

As tabuadas dos números dentro do intervalo.

"""

msgInicialInvalida = "Insira um número inicial entre 1 e 9"
msgFinalInvalida = "Insira um número final entre 1 e 9"
msgValor7e8 = "Nenhuma tabuada nesse intervalo"

valorInicial = int(input())
while(valorInicial < 1 or valorInicial > 9):
    print(msgInicialInvalida)
    valorInicial = int(input())


valorFinal = int(input())
while(valorFinal < 1 or valorFinal > 9):
    print(msgFinalInvalida)
    valorFinal = int(input())

if valorInicial >= 7 and valorInicial <= 8 and valorFinal >= 7 and valorFinal <= 8:
    print(msgValor7e8)
else:
    while(valorInicial <= valorFinal):
        for x in range(1, 10):
            print("{} x {} = {}".format(valorInicial, x, valorInicial * x))
        print()
        valorInicial = valorInicial + 1
