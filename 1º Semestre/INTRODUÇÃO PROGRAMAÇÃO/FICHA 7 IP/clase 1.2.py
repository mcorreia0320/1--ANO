def criar_lista(lista, ficheiro):
    t= open (ficheiro, 'a', encoding= 'UTF-8')
    for elemento in lista:
        t.write(str(elemento)+'\n')
    t.close()
    return ficheiro

def le_lista_read(ficheiro):
    t= open(ficheiro, 'r', encoding='UTF-8')
    caracteres= t.read()
    t.close()
    lista_a_retornar=[]
    for caracter in caracteres:
        if caracter != '\n':
            lista_a_retornar += [int(caracter)]
    return lista_a_retornar