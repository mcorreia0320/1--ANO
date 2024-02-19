#Partindo do programa realizado anteriormente, crie um novo programa que calcula a soma de todos os
#números apresentados ao utilizador. 


inteiro = eval(input('Escreva um inteiro:'))
soma= 0

while inteiro <= 15:
    print('n=',inteiro)
    soma += inteiro
    inteiro += 1

print('soma dos elementos:', soma)
    
