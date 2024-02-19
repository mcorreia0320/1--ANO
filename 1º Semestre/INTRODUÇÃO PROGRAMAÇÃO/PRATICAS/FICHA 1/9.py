#1

x= eval(input('Escreva o primeiro nº:'))
y= eval(input('Escreva o segundo nº:'))
z= eval(input('Escreva o terceiro nº:'))

#2

if x > y and x > z:
    print('o nº maior é', x)

elif y > x and y > z:
    print('o nº maior é', y)
    
else: 
    print(' o nº maior é', z)
