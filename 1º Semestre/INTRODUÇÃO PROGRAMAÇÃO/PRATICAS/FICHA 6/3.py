#Escreva uma função com o nome duplica_elementos que recebe uma lista e devolve a lista obtida da
#lista original em que todos os elementos são duplicados. Não necessita de verificar a validade dos argumentos.
#Por exemplo,
#>>> duplica_elementos ( ['a', ['b', 'c'], 5])
#['a', 'a', ['b, 'c'], ['b', 'c'], 5, 5]
#>>> duplica_elementos ( [])
#[]

def duplica_elementos(lista):
    lista_vazia=[]
    for elementos in lista:
        lista_vazia += (elementos, elementos,)
    return lista_vazia