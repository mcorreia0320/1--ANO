#Escreva uma função em Python com o nome soma_quadrados que recebe um número inteiro positivo, n,
#e tem como valor a soma dos quadrados de todos os números inteiros de 1 até n.

def somas_quadrados(inteiro):
    soma= 0
    for e in range(inteiro+1):
        soma+= e**2
    return soma
