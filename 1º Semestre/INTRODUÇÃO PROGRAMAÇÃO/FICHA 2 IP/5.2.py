inteiros= int(input('Escreva um inteiro entre 1 e 15:' ))

def calcular_soma(elementos):
    soma=0
    
    
    while elementos <= 15:
        soma+=elementos
        elementos+= 1
    
    return soma

print('soma dos elementos:', calcular_soma(inteiros))
