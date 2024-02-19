def criar_lista(lista, ficheiro):
    t= open (ficheiro, 'a', encoding= 'UTF-8')
    for elemento in lista:
        t.write(str(elemento)+'\n')
    t.close()
    return ficheiro

def le_lista(ficheiro):
    t= open(ficheiro, 'r', encoding='UTF-8')
    linhas= t.readlines()
    t.close()
    lista_a_retornar=[]
    for linhas in linhas:
        lista_a_retornar += [int(linha)]
    return lista_a_retornar