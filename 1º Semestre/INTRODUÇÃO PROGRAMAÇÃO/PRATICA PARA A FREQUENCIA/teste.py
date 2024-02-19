def teste(letra, subLetra, array):
    for i in range(len(array)):
        if letra == array[i]:
            array[i] = subLetra
    return array

def somar (num, steps):
    num += steps
    return num

numero = 5

#print(somar(numero,3))
#print(numero)

#lista = ['a','b','c','d','a']


#print(teste('a','y', lista))

#print(lista)

def mul(x,y):
    if y == 1:
        return x
    result = x * mul(x,y-1)
    return result

x = 3
y = 3
result = mul(x,y)



print(result)


    