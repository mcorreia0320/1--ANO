def remove_multiplos (lista, numero):
    lista_vazia=[]
    for l in lista:
        if l % numero != 0:
            lista_vazia += [l]
    return lista_vazia

lista1= [1,4,3,6,7,8,5,3,4,5,6,7,8,9,0,12,2,3,34,55,6,7,88,9]
numero1 = 2

print(remove_multiplos(lista1, numero1))