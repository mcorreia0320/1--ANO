#Escreva uma função em Python com o nome junta_ordenadas que recebe como argumentos duas listas
#ordenadas por ordem crescente e devolve uma lista também ordenada com os elementos das duas listas. Não é
#necessário validar os argumentos da sua função. Por exemplo,
#junta_ordenadas ( [ 2, 5, 90], [ 3, 5, 6, 12])
#[2, 3, 5, 5, 6, 12, 90]

def junta_ordenadas(lista1, lista2):
    indice1= 0
    indice2= 0
    lista_vazia=[]
    while indice1 < len(lista1) and indice2 < len(lista2):
        if lista1[indice1] < lista2[indice2]:
            lista_vazia += (lista1[indice1],)
            indice1 += 1
        else:
            lista_vazia += (lista2[indice2],)
            indice2 += 1
    lista_vazia += lista1[indice1:] + lista2[indice2:]
    return lista_vazia