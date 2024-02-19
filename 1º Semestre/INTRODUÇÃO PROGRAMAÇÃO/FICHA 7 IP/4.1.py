#Suponha que bib é uma lista cujos elementos são dicionários e que contém a informação sobre os livros
#existentes numa biblioteca. Cada livro é caracterizado pelos seus autores, título, casa editora, cidade de
#publicação, ano de publicação, número de páginas e ISBN. Escreva um programa em Python que recebe a
#informação de uma biblioteca e devolve o título do livro mais antigo. 

def mais_antigo(lista_de_dicionario):
    indice_antigo= 0
    for indice_atual in range (1, len(lista_de_dicionario)):
        if lista_de_dicionario[indice_antigo]["ano"] > lista_de_dicionario[indice_atual]["ano"]:
            indice_antigo = indice_atual
    return lista_de_dicionario[indice_antigo]["titulo"]
        
        
        
    
    
lista_de_dicionario= [{"titulo": "IP", "autores":["Joao", "Andres"], "ano": 2010, "ISBN":9781234},
                      {"titulo": "AD", "autores":["Carla"], "ano": 2005, "ISBN":9781333},
                      {"titulo": "SOR", "autores":["Pedro", "Carlos"], "ano": 2020, "ISBN":9781111}]

