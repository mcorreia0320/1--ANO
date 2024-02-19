def criar_dicionario(dicionario, ficheiro)
t= open(ficheiro, 'w', encoding='UTF-8')
for chave in dicionario:
    t.writelines(str(chave)+':'+str(dicionario[chave])+'\n')
    t.close()
    return ficheiro
    
    