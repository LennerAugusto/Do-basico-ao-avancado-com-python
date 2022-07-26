conjunto = {1, 2, 3, 4}
conjunto.add(5)
conjunto.remove(2)
print(conjunto)


conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {5, 6, 7, 8, 9}

conjunto_uniao = conjunto_1.union(conjunto_2)
print(conjunto_uniao)

conjunto_intersescao = conjunto_1.intersection(conjunto_2)
print(conjunto_intersescao)

conjunto_diferenca = conjunto_1.difference(conjunto_2)
print(conjunto_diferenca)

conjunto_dif_simetrica = conjunto_2.symmetric_difference(conjunto_1)
print(conjunto_dif_simetrica)

                                                           CONVERSÂO
lista_animais = ['gato', 'cachorro', 'elefante']
conjunto_animais = set(lista_animais)
print(type(conjunto_animais), conjunto_animais)