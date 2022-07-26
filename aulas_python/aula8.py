print('Bem vindo a caluladora')
print('MENU')
menu = int(input('DIGITE O NÚMERO CORRESPONDENTE PARA A OPERAÇÃO DESEJADA \n1 - SOMA \n2 - SUBTRAÇÃO \n3 - MULTIPICAÇÃO\n4 - DIVISÃO '))
n1 = int(input('DIGITE O PRIMEIRO NÚMERO A SER CALCULADO'))
n2 =  int(input('DIGITE O SEGUNDO NÚMERO A SER CALCULADO'))

def soma(a, b):
    som = a + b
    return som

def subtracaoo(a, b):
    sub = a - b
    return sub

def multiplicacao(a, b):
    multi = a * b
    return multi

def divisao(a, b):
    div = a/ b
    return div

if menu == 1:
    print(soma(n1, n2))

if menu == 2:
    print(subtracaoo(n1, n2))

if menu ==3:
    print(multiplicacao(n1, n2))

if menu == 4:
    print(divisao(n1, n2))

print('OBRIGADO POR UTILIZAR A CALULADORA EM PYTHON')
# print('DESEJA REALIZAR MAIS ALGUMA OPERAÇÃO ?')
#
# reiniciar = int(input('DIGITE 1 PARA SIM E 2 PARA NÃO '))
#
# if reiniciar == 1:
#

