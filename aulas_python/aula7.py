# class Calculadora:
#     def__init__(self, n1, n2):
#         self.a = n2
#         self.b = n2
#
#
#     def soma(a, b):
#         return a + b                                 #EVITA GERAÇÃO REPETIDAS DE CÓDIGO
#
#     def sub (a, b)
#         return a + b
#
#     def mult (a, b)
#         return a * b
#
#     def div (a, b)
#         return a / b
#
#
# n1 = int(input('Digite um numero'))
# n2 = int(input('Digite o segundo número'))
#
# print(soma(n1, n2))
# print(sub(n1, n2))
# print(mult(n1, n2))
# print(div(n1, n2))

class Televisao:
    def __init__(self):
        self.ligada = false

    def power(self):
        if self.ligada:
            self.ligada = false
        else:
            self.ligada = true

televisao = Televisao()
print(televisao.ligada = false)
televisao.power()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
