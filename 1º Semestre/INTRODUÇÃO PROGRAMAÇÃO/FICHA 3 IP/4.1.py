valor = eval(input('Indique o valor a trocar: '))
devolve = 0

while valor >= 20:
    devolve += 1
    valor -=20
    
print('Devolveu',devolve,'notas de 20 €')
