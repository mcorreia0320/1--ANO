#1 - pedir numero

inteiro= eval(input('Escreva um nº inteiro \n?'))
resultado= ""

#2 - Descobrir par ou impar 
while inteiro > 0:
    #2.1 Isolar digito
    digito= inteiro % 10
    #2.2 Testar digito
    #2..2.1
    if digito % 2 !=0:
        #2.2.2 guardar digito impar
        resultado += str(digito)
    #2.3 Eliminar digito
    inteiro //=10
    
#3 retornar resultado 
#3.1 mostrar resultado
#3.2 inverter resultado
print("Resultado:" + resultado [::-1])


    
    
    
    
    
    

