def ficheiro_a_receber(ficheiro):
    t= open (ficheiro.txt, 'r', encoding = 'UTF-8')
    contagem = 0
    linhas= t.readlines()
    t.close(ficheiro)
    for linha in ficheiro:
        print(linha)
        contagem += 1
    return contagem
        