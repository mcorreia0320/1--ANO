valor = eval(input('Indique o valor a trocar: '))
devolve = 0
devolve1= 0
devolve2= 0
devolve3= 0

while valor >= 50:
    devolve += 1
    valor -=50
    
print('Devolveu',devolve,'notas de 50 €')


while valor >= 20:
    devolve1 += 1
    valor -= 20
print('Devolveu', devolve1, 'notas de 20 €')

while valor >= 2:
    devolve2 += 1
    valor= -2
print('Devolveu', devolve2, 'moedas de 2 €')

while valor >= 0.2:
    devolve2 += 1
    valor= -0.2
print('Devolveu', devolve3, 'moedas de 0.2 €')
