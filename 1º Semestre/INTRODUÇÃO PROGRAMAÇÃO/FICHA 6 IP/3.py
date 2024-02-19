#Escreva uma função com o nome duplica_elementos que recebe uma lista e devolve a lista obtida da
#lista original em que todos os elementos são duplicados. Não necessita de verificar a validade dos argumentos.
#Por exemplo,
#>>> duplica_elementos ( ['a', ['b', 'c'], 5])
#['a', 'a', ['b, 'c'], ['b', 'c'], 5, 5]
#>>> duplica_elementos ( [])
#[]

def duplica_elementos(lista_recibida):
    lista_vazia=[]
    for elemento in lista_recibida:
        lista_vazia= [elemento, elemento]
        
    return lista_vazia

lista1= ['a', ['b', 'c'], 5]

print(duplica_elementos(lista1))

