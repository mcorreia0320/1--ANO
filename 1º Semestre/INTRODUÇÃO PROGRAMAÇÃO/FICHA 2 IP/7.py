#Escreva um programa que deve calcular o desconto a efectuar e o montante a pagar após o desconto,
#supondo que uma empresa vende um produto, cujo preço base por unidade é fornecido pelo utilizador. No
#entanto, se a quantidade comprada atingir ou ultrapassar as 500 unidades, será efectuado um desconto de
#5% e, se essa quantidade ultrapassar as 1000 unidades, o desconto é de 8%. A quantidade a comprar é um
#dado pedido ao utilizador.

#1 

preço= eval(input('valor por unidade: '))
quantidade= eval(input('quantidade de unidades: '))
valor_com_desconto= 0

#2

pagamento= preço * quantidade
desconto_5 = pagamento * 0.05
desconto_8 = pagamento * 0.08


#3

if quantidade > 0 and quantidade <= 500: 
    valor_com_desconto= pagamento - desconto_5
    print('O precio a pagar é', valor_com_desconto,'€ com um desconto de 5%') 
    
elif quantidade > 500 and quantidade <=1000:
    valor_com_desconto= pagamento - desconto_8
    print('O precio a pagar é', valor_com_desconto,'€ com um desconto de 8%')     
    