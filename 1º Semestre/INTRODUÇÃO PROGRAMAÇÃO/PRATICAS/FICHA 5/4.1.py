def junta_ordenados(tuplo1, tuplo2):
    for elemento1 in range(0,len(tuplo1)-1,1):
        for elemento2 in range(0, len(tuplo2)-1,1):
            tuplo_vazio=()
                      
            while indice1 < len(tuplo1) and indice2 < len(tuplo2):
                if tuplo1[elemento1] < tuplo2[elemento2]:
                    tuplo_vazio += (+1,tuplo1[elemento1],)
                    
                else:
                    tuplo_vazio += (+1,tuplo2[elemento2],)
                    
            tuplo_vazio += tuplo1[:] + tuplo2[indice2:]
            return tuplo_vazio

