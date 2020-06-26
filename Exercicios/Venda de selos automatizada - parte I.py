"""
Você foi contratado por uma agência dos correios para programar uma máquina de venda de selos automática que será instalada para diminuir as filas na agência. Ela terá uma balança para pesar o pacote e um conjunto de sensores para escanear e calcular as suas dimensões.
Tal máquina só servirá para o envio de cartas e pacotes que respeitem os limites de peso e dimensões abaixo:
Peso máximo de 500.0 g.
Tamanho máximo da maior dimensão: 28.0 cm.
Valor máximo da soma de todas as dimensões: 52.0 cm.
Qualquer pacote que ultrapasse qualquer desses limites deverá ser encaminhado para o atendimento no balcão.

Eventualmente pode ocorrer algum erro na leitura dos sensores ou da balança e estes retornarem um valor inválido (negativo ou nulo), portanto, quando isto acontecer, a leitura deve ser realizada novamente.
Sendo assim, escreva um programa em Python 3 que:
Receba o peso do pacote e os valores de comprimento, largura e profundidade e verifique se os valores lidos são válidos (positivos e não nulos). O programa deve receber o peso do pacote e realizar a sua validação antes de receber as entradas das dimensões. Em relação às dimensões, se uma for inválida, todas as 3 devem ser lidas novamente até que todas sejam válidas.
O programa deve imprimir as mensagens: "Peso valido!", "Peso invalido!", "Dimensoes validas!" e "Dimensoes invalidas!", conforme o caso em questão (Note que as palavras estão sem acentos).
Após concluir a validação dos dados de entrada, verifique se os limites para processamento no caixa automático são atendidos. Em caso afirmativo, o programa deve seguir para o item 3), caso contrário, deve imprimir a seguinte mensagem (sem as aspas e sem quebra de linha) e encerrar: "Este pacote nao atende os limites para envio no caixa de autoatendimento, dirija-se ao balcao de atendimento para posta-lo!"
Calcule o custo (C) da postagem e imprima-o com a seguinte formatação: "Custo total do envio: RS 0.00". O cálculo do custo é composto de duas parcelas, uma devido ao peso e outra devido ao tamanho do pacote, conforme segue:

A parcela do custo referente ao peso (P) é dada por:
E a parcela do custo referente ao tamanho do pacote é dada por:
Onde S representa a soma das três dimensões do pacote (comprimento, largura e profundidade)

Formato de entrada

A entrada do problema consiste de uma sequência de números reais, separados por quebra de linha, representando os valores lidos pela balança e pelos sensores de dimensão.

Atentem-se para a diferença entre valores válidos (quando há uma leitura incorreta dos sensores) e pacotes que não podem ser processados automaticamente. Um pacote de 1kg é válido, só não pode ser processado pela máquina de selos.

Formato de saída

A saída deverá conter as mensagens de validade ou não dos valores, conforme os dados de entrada para cada caso, e em seguida a mensagem referente ao processamento do pacote (se deve ser encaminhado ao balcão de atendimento ou o custo final de envio).
"""

# Felipe
mensagemDimensaoValida = "Dimensoes validas!"
mensagemDimensaoInvalida = "Dimensoes invalidas!"

def isValid(value):
    return value > 0

def showMessage(mensagem):
    print(mensagem)

def isValidSizing(comprimento, largura, profundidade):
    return isValid(comprimento) and isValid(largura) and isValid(profundidade)


lista = list(range(0, -500, -1))
lista1 = map(float, lista)
p = float(input())
while p < 1:
    print("Peso invalido!")
    p = float(input())
print("Peso valido!")

lista = list(range(0, -500, -1))
lista1 = map(float, lista)
z = int(0)
n = 0
valor = []
s = float(0)
cp = float(0)
cd = float(0)
cf = float(0)


comprimento = float(input())
largura = float(input())
profundidade = float(input())

while(not isValidSizing(comprimento, largura, profundidade)):
    showMessage(mensagemDimensaoInvalida)
    comprimento = float(input())
    largura = float(input())
    profundidade = float(input())

showMessage(mensagemDimensaoValida)


s = comprimento + largura + profundidade

if p > 500 or (comprimento > 28 or largura > 28 or profundidade > 28 or s > 52):
    print('Este pacote nao atende os limites para envio no caixa de autoatendimento, dirija-se ao balcao de atendimento para posta-lo!')
elif p <= 100 and s <= 22:
    cp = 0.50 + (0.50 // 10) / 10
    cd = 0.20 + (0.20 // 2) / 10
    cf = cp + cd
    print(f'Custo total do envio: R$ {cf:.2f}')
elif p <= 100 and s <= 52:
    cp = 0.50 + (0.50 // 10) / 10
    cd = 0.20 + (s - 22) // 2 / 10
    cf = cp + cd
    print(f'Custo total do envio: R$ {cf:.2f}')
elif p <= 500 and s <= 22:
    cp = 0.50 + (p - 100) // 10 / 10
    cd = 0.20 + (0.20 // 2) / 10
    cf = cp + cd
    print(f'Custo total do envio: R$ {cf:.2f}')
elif p <= 500 and s <= 52:
    cp = 0.50 + ((p - 100) // 10) / 10
    cd = 0.20 + ((s - 22) // 2)/ 10
    cf = cp + cd
    print(f'Custo total do envio: R$ {cf:.2f}')



