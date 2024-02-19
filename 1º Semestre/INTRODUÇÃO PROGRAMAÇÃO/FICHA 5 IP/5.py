#Escreva uma função em Python, com o nome conta_menores que recebe um tuplo contendo números inteiros e um
#número inteiro e que devolve o número de elementos do tuplo que são menores do que esse inteiro. Por exemplo,
#>>> conta_menores((3, 4, 5, 6, 7) , 5)
#2
#>>> conta_menores((3, 4, 5, 6, 7) , 2)
#0

def conta_menores (tuplo, inteiro):
    soma= 0
    for e in tuplo:
        if e < inteiro:
            soma+= 1
    return soma


t1=(3,4,5,6,7)
inteiro1= 5

inteiro2= 2

print(conta_menores(t1, inteiro1))

