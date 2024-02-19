

def separa_tuplos(tuplo, indice_separação):
    tuplo_1= tuplo[:indice_separação]
    tuplo_2= tuplo[indice_separação:]
    return (tuplo_1, tuplo_2)


tuplo_a_separar= (1,2,3,4,'a','b')
resultado = separa_tuplos(tuplo_a_separar, 3)
print(resultado)
print(type(resultado[0]))
print(' O primeiro tuplo é', resultado[0], ' e o segundo tuplo é', resultado[1])
    