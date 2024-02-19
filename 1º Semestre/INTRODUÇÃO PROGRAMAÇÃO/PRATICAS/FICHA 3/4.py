#Usando um ciclo for, escreva uma função em Python que recebe uma quantia em Euros e calcula o número de
#notas de 50€, 20€, 10€, 5€ e moedas de 2€, 1€, 50 cêntimos, 20 cêntimos, 10 cêntimos, 5 cêntimos, 2 cêntimos
#e 1 cêntimo, necessário para perfazer, essa quantia, utilizando sempre o máximo número de notas e moedas para
#cada quantia, da mais elevada para a mais baixa. 

Valor_a_trocar= eval(input('Escreva o valor a trocar:'))
moedas_e_notas=(50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05,0.02, 0.01)

for moedas_e_notas in moedas_e_notas:
    devolve = 0
    while Valor_a_trocar >= moedas_e_notas:
        devolve += 1
        Valor_a_trocar -= moedas_e_notas

    if moedas_e_notas > 2:
            print('Devolve', devolve, 'notas de', moedas_e_notas, '€')
    elif moedas_e_notas >= 1:
            print('Devolve', devolve, 'moedas de', moedas_e_notas, '€')
    else:
            print('Devolve', devolve, 'moedas de', moedas_e_notas*100,'centimos')
            
            
    