#Escreva um programa em Python que lê um número inteiro positivo e produz o número correspondente a inverter a ordem
#dos seus dígitos. Por exemplo,
#Escreva um inteiro positivo
#? 7633256
#O número invertido é 6523367

#1 

inteiro= int(input('Escreva um inteiro positivo \n? '))
invertido= str(inteiro)

#2

print('O número invertido é',invertido[::-1])

