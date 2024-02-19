#Escreva uma função em Python com o nome soma_quadrados que recebe um número inteiro positivo, n,
#e tem como valor a soma dos quadrados de todos os números inteiros de 1 até n.


def soma_quadrados(n):
    soma= 0
    for numeros in range(1, n+1,1):
        soma += numeros**2
    return soma