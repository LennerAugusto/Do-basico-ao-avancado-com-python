n = int(input('Digite um número de 0 a 10'))
while n > 10:
    print('nota inválida')
    n = int(input('Digite um número de 0 a 10'))
print('A nota é igual a: {}'.format(n))

# else:
#
# while n = 10:
#     print(n)
#     n +=1



# a = int(input('Digite um número'))
# div = 0
# for x in range (1, a+1):
#     resto = a % x
#     if resto == 0:
#         div = div + 1
# if div == 2:
#     print('o Número {} é primo'.format(a))
# else:
#     print('O número {} não é primo'.format(a))