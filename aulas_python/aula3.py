print('Calculadora de médias, as notas só poderão ser digitadas de 0 a 10:')

n1 = int(input('DIGITE A PRIMEIRA NOTA'))
while n1 > 10:
    n1 = int(input('Nota inválida, digite novamente a primneira nota'))
while n1 < 0:
    n1 = int(input('Nota inválida, digite novamente a segunda nota'))

n2 = int(input('DIGITE A SEGUNDA NOTA '))
while n2 > 10:
    n2 = int(input('Nota inválida, digite novamente a segunda nota'))
while n2 < 0:
    n2 = int(input('Nota inválida, digite novamente a segunda nota'))

n3 = int(input('DIGITE A TERCEIRA NOTA'))
while n3 > 10:
    n3 = int(input('Nota inválida, digite novamente a terceira nota'))
while n3 < 0:
    n3 = int(input('Nota inválida, digite novamente a segunda nota'))

n4 = int(input('DIGITE A QUARTA NOTA'))
while n4 > 10:
    n4 = int(input('Nota inválida, digite novamente a quarta nota'))
while n4 < 0:
    n4 = int(input('Nota inválida, digite novamente a segunda nota'))

media = (n1 + n2 + n3 + n4 ) / 4
print('A média final do aluno é: {}'.format(media))




# a = int(input('Digite o primeiro número'))
# b = int(input('Digite o segunbdo número'))
# resto_a = a % 2
# resto_b = a % 2
#
# if resto_a == 0 or resto_b==0:
#     print('Os dois valores digitados são pares')
# else:
#     print('Nenhum número par foi digitado')




# a = int(input('Digite o primeiro valor'))
# # b = int(input('Digite o segundo valor'))
# # c = int(input('Digite o terceiro valor'))
# #
# # if a < b and a < c:
# #     print("A é menor que B e menor que c")
# # else:
# #     print("A é maior que B e maior que c")
# #
# # print('Final do programa')
