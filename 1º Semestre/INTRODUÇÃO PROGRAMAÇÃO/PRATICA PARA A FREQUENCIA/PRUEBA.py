nota = eval(input('Introduza uma nota: '))

if nota < 9.5:
    print('Insuficiente')
    
elif nota < 13:
    print('Suficiente')
    
elif nota < 17: 
    print('Bom')

else:
    if nota < 20:
        print('Muito Bom')