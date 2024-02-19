#1

while True:
    lista_de_nomes= []
    lista_de_numeros= []
    nome_do_aluno= input('Indique o nome do aluno:')
    lista_de_nomes += [nome_do_aluno]
    numero_do_aluno= eval(input('Indique o numero do aluno:'))
    lista_de_numeros += [numero_do_aluno]
    print(lista_de_nomes)
    print(lista_de_numeros)

    
#6
    
def guarda_lista_em_dicionario(lista_nomes, lista_numeros):
    dicionario= {}
    for elementos in lista_numeros:
        dicionario += [elementos]
        for valores in lista_nomes:
            dicionario[elementos] += [valores]
    return dicionario
    
    
    
    