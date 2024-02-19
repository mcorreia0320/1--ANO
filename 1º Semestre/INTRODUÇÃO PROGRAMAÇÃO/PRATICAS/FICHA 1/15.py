#Escreva um programa que lê um número inteiro e determina quantas vezes aparecem dois zeros seguidos. Por exemplo,
#Escreva um inteiro
#? 98007640003
#O número tem 3 zeros seguidos

#1

inteiro= eval(input('Escreva um inteiro: \n? '))
veces1= 0

#2 

while inteiro > 0:

    
    digito= inteiro % 10
    
    if digito == 0:
        
        veces1+= 1 
   

    


        
    