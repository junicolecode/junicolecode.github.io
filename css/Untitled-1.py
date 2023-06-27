# numeros = [4, 9, 8, 2, 7, 0]


# def quickSort(lista):
#     if len(lista) == 0:
#         return []
    
#     ref = lista[0]
#     esquerda = []
#     direita = []
    
#     for n in lista:
#         if n < ref:
#             esquerda.append(n)
#         elif n > ref:
#             direita.append(n)
#     return quickSort(esquerda) + [ref] + quickSort(direita)

# print(quickSort(numeros))



numeros = [8, 6, 0, 4, 9]

def ordenar(lista):
    if len(lista) <= 1:
        return lista
    
    primeiro = lista[0]
    menores = []
    maiores = []

    for n in lista:
        if n < primeiro:
            menores.append(n)
        elif n > primeiro:
            maiores.append(n)

    return ordenar(menores) + [primeiro] + ordenar(maiores)

var = ordenar(numeros)
print(var)