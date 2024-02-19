#Escreva um programa que lê um número inteiro e determina quantas vezes aparecem dois zeros seguidos. Por exemplo,
#Escreva um inteiro
#? 98007640003
#O número tem 3 zeros seguidos

#1

inteiro= eval(input('Escreva um inteiro \n? '))
resultado= 0

while inteiro >= 10:
    digito= inteiro % 10
    inteiro //= 10
    digito_siguiente= inteiro % 10
    
    if digito == 0 and digito_siguiente == 0:
        resultado = resultado + 1
        
print('O número tem',resultado,'zeros seguidos')        
        
    
    
