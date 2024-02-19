#Escreva um programa em Python que lê um número inteiro positivo e calcula o número obtido do número lido que apenas
#contém os seus dígitos ímpares. Por exemplo,
#Escreva um inteiro
#? 785554
#Resultado: 7555

#1 

nº_interio= int(input('Escreva um inteiro \n? '))
resultado=''

#2 

while nº_interio > 0:
    
    digito= nº_interio % 10 #isolar digito
    
    if digito % 2 != 0: #testar se é par ou impar
        resultado += str(digito)
        
    nº_interio //= 10 #eliminar ultimo digito
        
#4 retornar, mostrar e inverter resultado

print('Resultado:',resultado[::-1])
        
        
    
        
        



