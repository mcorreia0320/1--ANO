#Escreva a função agrupa_por_chave que dada uma lista de pares chave valor (k, v) (representados
#por tuplos de dois elementos) devolve um dicionário que a cada chave k associa uma lista com os valores v, para
#essa chave encontrados na lista passada como argumento. Por exemplo,
#>>> agrupa_por_chave ([('a', 8), ('b', 9), ('a', 3)])
#{'a': [8,3], 'b': [9]}

def agrupa_por_chave(dicionario):
    dicionario_a_retornar= {}
    for elemento in dicionario:
        chave = elemento[0]
        valor= elemento[1]
        if chave in dicionario_a_retornar:
            dicionario_a_retornar[chave] += [valor]
        else:
            dicionario_a_retornar[chave] = [valor]
    return dicionario_a_retornar
        