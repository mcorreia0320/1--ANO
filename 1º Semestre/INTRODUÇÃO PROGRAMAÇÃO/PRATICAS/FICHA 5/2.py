#Um número d é divisor de n se o resto da divisão de n por d for 0. Escreva uma função com o nome
#num_divisores que recebe um número inteiro positivo n, e tem como valor o número de divisores de n. No
#caso de n ser 0 deverá devolver 0. Por exemplo,
#>>> num_divisores(20)
#6
#>>> num_divisores (13)
#2

def num_divisores(n):
    divisores= 0
    for teste in range(1,n+1,1):
        if n == 0:
            return 0
        elif n % teste == 0:
            divisores += 1
    return divisores 

            
        