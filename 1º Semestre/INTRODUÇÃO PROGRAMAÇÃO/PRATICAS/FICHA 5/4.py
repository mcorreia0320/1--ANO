#Defina uma função, junta_ordenados, que recebe dois tuplos contendo inteiros, ordenados por ordem
#crescente, e devolve um tuplo também ordenado com os elementos dos dois tuplos. Por exemplo,
#>>> junta_ordenados((2, 34, 200, 210) , (1, 23))
#(1, 2, 23, 34, 200, 210)

def junta_ordenados(tuplo1, tuplo2):
    indice_1= 0
    indice_2= 0
    tuplo_vazio=()
    while indice_2 < len(tuplo2) and indice_1 < len(tuplo1):
        if tuplo1[indice_1] > tuplo2[indice_2]:
            tuplo_vazio += (tuplo2[indice_2],)
            indice_2 += 1
        else:
            tuplo_vazio += (tuplo1[indice_1],)
            indice_1 += 1
    tuplo_vazio += tuplo1[indice_1:] + tuplo2[indice_2:]
    return tuplo_vazio
                    
                
                    
            
                    
            
    