#Suponha que bib é uma lista cujos elementos são dicionários e que contém a informação sobre os livros
#existentes numa biblioteca. Cada livro é caracterizado pelos seus autores, título, casa editora, cidade de
#publicação, ano de publicação, número de páginas e ISBN. Escreva um programa em Python que recebe a
#informação de uma biblioteca e devolve o título do livro mais antigo. 

def mais_antigo(lista_de_dicionario):
    indice_antigo= lista_de_dicionario[0]
    for livro_lista in lista_de_dicionario:
        if indice_antigo["ano"] > livro_lista["ano"]:
            indice_antigo= livro_lista
    return indice_antigo["titulo"]
            
        
        
        
    
    
lista_de_dicionario= [{"titulo": "IP", "autores":["Joao", "Andres"], "ano": 2010, "ISBN":9781234},
                      {"titulo": "AD", "autores":["Carla"], "ano": 2005, "ISBN":9781333},
                      {"titulo": "SOR", "autores":["Pedro", "Carlos"], "ano": 2020, "ISBN":9781111}]

