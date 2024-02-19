#Escreva uma função em Python com o nome junta_ordenadas que recebe como argumentos duas listas
#ordenadas por ordem crescente e devolve uma lista também ordenada com os elementos das duas listas. Não é
#necessário validar os argumentos da sua função. Por exemplo,
#junta_ordenadas ( [ 2, 5, 90], [ 3, 5, 6, 12])
#[2, 3, 5, 5, 6, 12, 90]

def junta_ordenados(l1, l2):
    indice_l1, indice_l2= 0, 0
    resultado= []
    while indice_l1 < len(l1) and indice_l2 < len(l2):
        if l1[indice_l1] <= l2[indice_l2]:
            resultado += (l1[indice_l1],)
            indice_l1 += 1
        else:
            resultado += (l2[indice_l2])
            indice_l2 += 1
    resultado += l1[indice_l1:] + l2[indice_l2:]
    return resultado

lista1= [2, 5, 90]
lista2= [3, 5, 6, 12]

print(junta_ordenados(lista1, lista2))

