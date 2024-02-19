#Escreva um programa que deve calcular o desconto a efectuar e o montante a pagar após o desconto,
#supondo que uma empresa vende um produto, cujo preço base por unidade é fornecido pelo utilizador. No
#entanto, se a quantidade comprada atingir ou ultrapassar as 500 unidades, será efectuado um desconto de
#5% e, se essa quantidade ultrapassar as 1000 unidades, o desconto é de 8%. A quantidade a comprar é um
#dado pedido ao utilizador.

preço_base_por_unidade = eval(input('Defina o preço base do produto:'))
quantidade_a_comprar = eval(input('Escreva a quantidade comprada:'))

preço_a_pagar_sem_desconto= 0
preço_a_pagar_com_desconto= 0

if quantidade_a_comprar >= 500 and quantidade_a_comprar <= 1000:
    preço_a_pagar_sem_desconto= (preço_base_por_unidade * quantidade_a_comprar)
    preço_a_pagar_com_desconto= (preço_a_pagar_sem_desconto - (preço_a_pagar_sem_desconto * 0.05))
    print('O preço a pagar é de', preço_a_pagar_com_desconto,'€ com um desconto de 5%')

elif quantidade_a_comprar >= 1000:
    preço_a_pagar_sem_desconto= (preço_base_por_unidade * quantidade_a_comprar)
    preço_a_pagar_com_desconto= (preço_a_pagar_sem_desconto - (preço_a_pagar_sem_desconto * 0.08))
    print('O preço a pagar é de', preço_a_pagar_com_desconto,'€ com um desconto de 8%')
    

    