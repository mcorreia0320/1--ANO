#Defina a função juntos que recebe um tuplo contendo inteiros e tem como valor o número de elementos
#iguais adjacentes. Por exemplo,
#>>> juntos((1,2,2,3,4,4))
#2
#>>> juntos((1,2,2,3,4))
#1

def juntos(tuplo):
    controlo= 0
    for elementos in range(0, len(tuplo) -1, 1):
        if tuplo[elementos] == tuplo[elementos + 1]:
            controlo += 1
    return controlo


    