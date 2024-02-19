def calcular_devoluçoes(moedas_e_notas,valor):
    devoluções= ()
    for moedas_e_notas in moedas_e_notas:
        devolve = 0
        while valor >= moedas_e_notas:
            devolve += 1
            valor -= moedas_e_notas
        devoluções+= (devolve,)
    return devoluções
            
valor_a_testar= eval(input('Indique o valor a trocar: '))
moedas_e_notas_a_testar = (50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.02, 0.01)
print(calcular_devoluçoes(moedas_e_notas_a_testar,valor_a_testar))

def mostra_resultado(moedas_e_notas,moedas_e_notas_a_imprimir):
    for in 
    if moedas_e_notas > 2:
        print('Devolve', devolve, 'nota(s) de', moedas_ou_notas)
    elif moedas_e_notas >= 1:
        print('Devolve', devolve, 'moeda(s) de', moedas_ou_notas)
    else:
        print('Devolve', devolve, 'moeda(s) de', moedas_ou_notas*100,'centimos')    
