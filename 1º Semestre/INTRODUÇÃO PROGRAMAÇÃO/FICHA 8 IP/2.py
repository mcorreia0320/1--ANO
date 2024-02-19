#Escreva uma função existe_algarismo que recebe um número n e um algarismo a, e devolve True
#se a aparece no número n, e False no caso contrário.
#Por exemplo, existe_algarismo(123234, 2) deverá retornar True. 

def existe_algarismo(numero, algarismo):
    
    while numero > 0:
        if numero % 10 == algarismo:
            resultado= True
            break
        else:
            resultado= False
        numero= numero // 10
    return resultado
            
   
        
            
        
        
        
    
      
        
        
   