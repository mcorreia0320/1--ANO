valor = eval(input('Indique o valor a trocar: '))
moedas_e_notas = (50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.02, 0.01)

for moedas_e_notas in moedas_e_notas:
    devolve = 0
    
    while valor >= moedas_e_notas:
        devolve += 1
        valor -= moedas_e_notas
    
    if moedas_e_notas > 2:
        print('Devolve', devolve, 'nota(s) de', moedas_e_notas)
    elif moedas_e_notas >= 1:
        print('Devolve', devolve, 'moeda(s) de', moedas_e_notas)
    else:
        print('Devolve', devolve, 'moeda(s) de', moedas_e_notas*100,'centimos')
        