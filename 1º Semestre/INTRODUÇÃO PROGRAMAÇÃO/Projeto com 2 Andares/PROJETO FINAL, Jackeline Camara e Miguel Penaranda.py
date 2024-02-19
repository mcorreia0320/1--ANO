from time import time
from datetime import datetime

def ordena_historico(dicionario): #Função que ordena o dicionario por Hora de Entrada, Hora de Salida, Andar, Lugar e Preço, respetivamente.
    for cliente in dicionario:
        if len(dicionario[cliente]) > 3: #Ordena apenas os historicos de veiculos que ja tenham saido
            dicionario[cliente][1], dicionario[cliente][3] = dicionario[cliente][3], dicionario[cliente][1] #Troca as posições
            dicionario[cliente][2], dicionario[cliente][3] = dicionario[cliente][3], dicionario[cliente][2] #Troca as posições
    return

tuplo_menus=( #Menus Interfazes
    """
    _______________________________
   |                               |
   |                               |
   |       Menu Principal          |
   |                               |
   |        1. Estacionar          |
   |        2. Sair                |
   |        3. Administrador       |
   |                               |
   |                               |
   |_______________________________|
    """,
    """
    _______________________________
   |                               |
   |                               |
   |        Menu Estacionar        |
   |                               |
   |        1. Escolher andar      |
   |        0. Sair                |
   |                               |
   |                               |
   |                               |
   |_______________________________|
    """,
    """
    _______________________________
   |                               |
   |                               |
   |       Menu Escolha Andar      |
   |                               |
   |       1. Andar 1              |
   |       2. Andar 2              |
   |       0. Voltar               |
   |                               |
   |                               |
   |_______________________________|
    """,
    """
     ___________________________________________
    |                                           |
    |                                           |
    |             Menu Escolha Lugar            |
    |                                           |
    |             F F F F F F F F F F           |       
    |             F F F F F F F F F F           |
    |                                           |
    |            1-20. Escolha o lugar          |
    |            0. Voltar                      |
    |                                           |
    |                                           |
    |___________________________________________| 
    """,
    """
     ___________________________________________
    |                                           |
    |                                           |
    |             Menu Escolha Lugar            |
    |                                           |
    |                                           |
    |             F F F F F F F F F F           |
    |                                           |
    |             1-10. Escolha o lugar         |
    |             0. Voltar                     |
    |                                           |
    |                                           |
    |___________________________________________| 
    """,
    """
     ___________________________________________
    |                                           |
    |                                           |
    |                 Menu Sair                 |
    |                                           |
    |          1. Escolher andar e lugar        |
    |          0. Voltar                        |
    |                                           |
    |___________________________________________| 
    """,
    """
     ___________________________________________
    |                                           |
    |                                           |
    |                 Menu Pagar                |
    |                                           |
    |            Tem que pagar: F €          |
    |                                           |
    |                                           |
    |             0. Voltar                     |
    |                                           |
    |___________________________________________|
    """,
    """
     ___________________________________________
    |                                           |
    |                                           |
    |                 Talão                     |
    |                                           |
    |         Andar: F                          |
    |         Lugar: F                          |
    |         Hora de Entrada: F         |
    |         Hora de Salida: F          |
    |         Preço: F €                     |
    |                                           |
    |         0. Voltar ao Menu Principal       |
    |___________________________________________| 
    """,    
    """
    _______________________________
   |                               |
   |                               |
   |      Menu Administrador       |
   |                               |
   |      1. Ver andares           |
   |      2. Valor acomulado       |
   |      3. Iniciar/Parar         |        
   |      0. Voltar                |
   |                               |
   |_______________________________|    
    
   """,
   """
     ___________________________________________
    |                                           |
    |                                           |
    |               Menu Andares                |
    |                                           |
    |       Andar 1: F F F F F F F F F F        |       
    |                F F F F F F F F F F        |
    |                                           |
    |       Andar 2: F F F F F F F F F F        |
    |                                           |
    |       0. Voltar                           |
    |                                           |
    |___________________________________________| 
    """,    

)

ocupação_andar_1={ 1:['_','X'], 2:['_','X'], 3:['_','X'], 4:['_','X'], 5:['_','X'], 6:['_','X'], 7:['_','X'], 8:['_','X'],  #Enumeração 
                9:['_','X'], 10:['_','X'], 11:['_','X'], 12:['_','X'], 13:['_','X'], 14:['_','X'], 15:['_','X'],            #de cada lugar e o seu valor,  
                16:['_','X'], 17:['_','X'], 18:['_','X'], 19:['_','X'], 20:['_','X'] }                                      #podendo ser: Disponivel(_) ou Indesponivel(X)

ocupação_andar_2={ 1:['_','X'], 2:['_','X'], 3:['_','X'], 4:['_','X'], 5:['_','X'], #Enumeroção de cada lugar, podendo ser:
                 6:['_','X'], 7:['_','X'], 8:['_','X'], 9:['_','X'], 10:['_','X']}  #Disponivel(_) ou Indesponivel(X)

menu_a_mostrar= 0 #Variavel que ajuda a controlar em todo momento os menu que se monstra

valor_acumulado = 0 #Variavel que guarda o valor acumulado

dicionario_historicos={} #Dicionario que guarda a informação dos carros estacionandos, tais como: Hora de entrada, Andar, Lugar, Saida e Preço

clientes_que_estacionaram= 0 #Variavel que ajuda a criar as chaves para guardar a informação dos clientes que estacionaram no parking

iniciar_ou_parar = True #Ainda não existe funcionalidade, em principio era uma ideia para a opção Iniciar/Parar
senha_do_administrador= 1234

lugares_ocupados_1 = 0
lugares_ocupados_2 = 0

while True: #Ciclo do Programa
    
    if not menu_a_mostrar == 3: #Condição para não imprimir os menus com valores mutaveis 
        if not menu_a_mostrar == 4:
            if not menu_a_mostrar == 9:
                if not menu_a_mostrar == 6:
                    if not menu_a_mostrar == 7:
                        print(tuplo_menus[menu_a_mostrar])
    
    if menu_a_mostrar == 5: # Caso se encontre no Menu Sair
        opção_desejada = eval(input('Escolha a opção desejada: ')) #Opção para usar o Menu Sair
    
    elif menu_a_mostrar == 6: #Caso esteja no Menu Sair, ignora o Escolha Opção para usar um "input" dependete ao menu
        print('')
        print('-------> Moedas aceites: 0.01€, 0.02€, 0.05€, 0.10€, 0.20€, 0.50€') #Mostra moedas aceites
    
    else: #Caso se encontre em qualquer menu; exceto no Menu Sair, Menu Pagar
        
        if menu_a_mostrar == 8: # Condição para mostrar o valor acumulado após o Menu Administrador
            
            if opção_escolhida == 2:
                
                senha= eval(input('Introduza a senha: ')) #Pede ao usuario a senha para verificar que se trata do administrador
                
                if senha == senha_do_administrador: #Verifica se o valor introduzido é igual a senha do administrador                
                    print(tuplo_menus[menu_a_mostrar]) #Imprime o menu
                    print('-------> O valor acumulado é: ', round(valor_acumulado,2),'€') #Imprime o Valor Acumulado
                    print('')
                
        
        elif menu_a_mostrar == 3: #Caso se encontre no Andar 1, apresenta informação ao cliente para facilitar o estacionamento
            print('')
            print('- O andar tem 20 lugares para estacionar - \n- Estacionar neste andar tem um custo de 2 euros por minuto-')
            print('')
        
        
        elif menu_a_mostrar == 4: #Caso se encontre no Andar 2, apresenta informação ao cliente para facilitar o estacionamento
            print('')
            print('- O andar tem 10 lugares para estacionar - \n- Estacionar neste andar tem um custo de 1 euro por minuto-')
            print('')            
        
        
        
        opção_escolhida = eval(input('Escolha a opção: ')) #Opções para transitar pelos menus
        
                
    if menu_a_mostrar == 0: #Menu Principal
        
        if opção_escolhida == 1: #Menu Principal --> Menu Estacionar
            menu_a_mostrar = 1 #Transição ao Menu Estacionar
        
        elif opção_escolhida == 2: #Menu Principal --> Menu Sair
            menu_a_mostrar = 5 #Transição ao Menu Sair
        
        elif opção_escolhida == 3: #Transição ao Menu Administrador
            menu_a_mostrar = 8 #Menu Principal --> Menu Administrador
        
        elif opção_escolhida == -1: #Opção secreta para fechar o parking (Fim do dia) e apresentar um historico dos clientes
            print('Fim do dia')
            print('Historico dos clientes:')
            ordena_historico(dicionario_historicos) #Chama a função que ordena o dicionario
            control = 1  #Ajuda a levar um control das impressoes dos clientes, segundo o numero de chegada
            while control <= len(dicionario_historicos): #Ciclo que imprime o historico
                print(dicionario_historicos[control]) 
                control += 1  #Seguinte historico do cliente
            break  #Quebra o ciclo, acabando o dia
            
        
        else: #Caso escolham uma opção não existente no Menu Principal
            print('')
            print('-------> Opção Invalida \n         Por favor, escolha uma das opções apresentadas no ecrã')
            
              
               
    elif menu_a_mostrar == 1: #Menu Estacionar
        
        if opção_escolhida == 0: #Menu Estacionar --> Menu Principal
            menu_a_mostrar= 0 #Transição ao Menu Principal
        
        elif opção_escolhida == 1: #Menu Estacionar --> Menu Escolha Andar
                menu_a_mostrar= 2 #Transição ao Menu Escolha Andar
        
        else: #Caso escolham uma opção não existente no Menu Estacionar
            print('')
            print('-------> Opção Invalida \n         Por favor, escolha uma das opções apresentadas no ecrã')        
                
    
    elif menu_a_mostrar == 2: # Menu Escolha Andar
          
        if opção_escolhida == 0: #Menu Escolha Andar --> Volta ao Menu Anterior
            menu_a_mostrar= 1 
        
        elif opção_escolhida == 1: #Menu Escolha Andar --> Menu Escolha Lugar 1
            
            if lugares_ocupados_1 >= 20: #Se o Andar estiver cheio, mostra mensagem indicando que esta cheio
                print('')
                print('-------> O andar encontra-se cheio')
            
            else:
                menu_a_mostrar = 3
                if menu_a_mostrar == 3 and ocupação_andar_1 != None: #Menu Escolha Lugar 1
                    controlo_lugares = 1 #Control de cada um dos lugares do Parking
                    for caracter_tuplo in range(0, len(tuplo_menus[menu_a_mostrar]),1): #Percorre cada caracter do Menu Lugar 1
                                        if tuplo_menus[menu_a_mostrar][caracter_tuplo] == 'F': #Condição para substituir os caracteres mutaveis
                                            print(ocupação_andar_1[controlo_lugares][0], end='', flush=True)
                                            controlo_lugares += 1 #Seguinte Lugar
                                        else:
                                            print(tuplo_menus[menu_a_mostrar][caracter_tuplo], end='', flush=True) # Caso não seja um caracter mutavel imprime-lo em str 
           
            
        elif opção_escolhida == 2: #Menu Escolha Andar --> Menu Escolha Lugar 2
            
            if lugares_ocupados_2 >= 10: #Se o Andar estiver cheio, mostra mensagem indicando que esta cheio
                print('')
                print('-------> O andar encontra-se cheio')
            
            else:            
                menu_a_mostrar= 4
                if menu_a_mostrar == 4 and ocupação_andar_2 != None: #Menu Escolha Lugar 2
                    controlo_lugares = 1 #Control de cada um dos lugares do Parking
                    for caracter_tuplo in range(0, len(tuplo_menus[menu_a_mostrar]),1): #Percorre cada caracter do Menu Lugar 2
                                        if tuplo_menus[menu_a_mostrar][caracter_tuplo] == 'F': #Condição para substituir os caracteres mutaveis
                                            print(ocupação_andar_2[controlo_lugares][0], end='', flush=True)
                                            controlo_lugares += 1 #Seguinte Lugar
                                        else:
                                            print(tuplo_menus[menu_a_mostrar][caracter_tuplo], end='', flush=True) # Caso não seja um caracter mutavel imprime-lo em str     
                           
        else: #Caso escolham uma opção não existente no Menu Escolha Andar
            print('')
            print('-------> Opção Invalida \n         Por favor, escolha uma das opções apresentadas no ecrã')        
    
    
    elif menu_a_mostrar == 3: #Menu Escolha Lugar 1
        
        if opção_escolhida == 0: #Menu Escolha Lugar 1 --> Volta ao Menu Escolha Andar
            menu_a_mostrar = 2
        
        elif opção_escolhida >= 1 and opção_escolhida <= 20: #Usuario Escolhe um Lugar 1-20
            
            if ocupação_andar_1[opção_escolhida] == ['_','X']: # Caso o lugar se encontre disponivel
                
                clientes_que_estacionaram += 1 #Entrada de um cliente ao parking, soma ao historico o cliente
                lugares_ocupados_1 += 1
                
                ocupação_andar_1[opção_escolhida] = ['X', time(), clientes_que_estacionaram]  #Ocupação do lugar, atribuição do numero de cliente e inicio da cronometragem
                hora_entrada= datetime.now() #Hora de Entrada
                hora_entrada_formatada = hora_entrada.strftime('%H:%M:%S') #Hora Formatada
                dicionario_historicos[clientes_que_estacionaram] = [hora_entrada_formatada, 1, opção_escolhida,] #Guarda no dicionario_historicos a hora de entrada, o andar e o lugar dos clientes
                
                print('')
                print('-------> O seu vehiculo será aparcado em: \n            Andar: 1 \n            Lugar:',opção_escolhida) #Apresenta confirmação de onde vai ser estacionado o vehiculo
                menu_a_mostrar = 0
                
            else: # Se o lugar não estiver disponivel
                if menu_a_mostrar == 3 and ocupação_andar_1 != None: #Menu Escolha Lugar 1
                    controlo_lugares = 1 #Control de cada um dos lugares do Parking
                    for caracter_tuplo in range(0, len(tuplo_menus[menu_a_mostrar]),1): #Percorre cada caracter do Menu Lugar 1
                                        if tuplo_menus[menu_a_mostrar][caracter_tuplo] == 'F': #Condição para substituir os caracteres mutaveis
                                            print(ocupação_andar_1[controlo_lugares][0], end='', flush=True)
                                            controlo_lugares += 1 #Seguinte Lugar
                                        else:
                                            print(tuplo_menus[menu_a_mostrar][caracter_tuplo], end='', flush=True) # Caso não seja um caracter mutavel imprime-lo em str                
                print('\n --------> Este lugar já se encontra ocupado \n           Escolha outro, por favor')
            
        else: #Caso escolher um lugar que não existe
            print('')
            print('-------> Este lugar não existe \n         Por favor, escolha um lugar existente')
            print('')
            
                    
                
    elif menu_a_mostrar == 4: #Menu Escolha Lugar 2
        
        if opção_escolhida == 0: #Menu Escolha Lugar 2 --> Volta ao Menu Escolha Andar
            menu_a_mostrar = 2 
    
        elif opção_escolhida >= 1 and opção_escolhida <= 10: #Usuario Escolhe Lugar 1-10
              
            if ocupação_andar_2[opção_escolhida] == ['_','X']: # Caso o lugar se encontre disponivel
                
                clientes_que_estacionaram += 1 #Entrada de um cliente ao parking
                lugares_ocupados_2 += 1
                
                ocupação_andar_2[opção_escolhida] = ['X', time(), clientes_que_estacionaram]  #Ocupação do lugar, atribuição do numero de cliente e inicio da cronometragem             
                hora_entrada= datetime.now() #Hora de Entrada
                hora_entrada_formatada = hora_entrada.strftime('%H:%M:%S') #Hora Formatada
                dicionario_historicos[clientes_que_estacionaram] = [hora_entrada_formatada, 2, opção_escolhida] #Guarda no dicionario_historicos a hora de entrada, o andar e o lugar dos clientes                
                
                print('')
                print('-------> O seu vehiculo será aparcado em: \n            Andar: 2 \n            Lugar:',opção_escolhida) #Apresenta confirmação de onde vai ser estacionado o vehiculo              
                menu_a_mostrar = 0
            
            else: # Se o lugar não estiver disponivel
                if menu_a_mostrar == 4 and ocupação_andar_2 != None: #Menu Escolha Lugar 2
                    controlo_lugares = 1 #Control de cada um dos lugares do Parking
                    for caracter_tuplo in range(0, len(tuplo_menus[menu_a_mostrar]),1): #Percorre cada caracter do Menu Lugar 2
                                        if tuplo_menus[menu_a_mostrar][caracter_tuplo] == 'F': #Condição para substituir os caracteres mutaveis
                                            print(ocupação_andar_2[controlo_lugares][0], end='', flush=True)
                                            controlo_lugares += 1 #Seguinte Lugar
                                        else:
                                            print(tuplo_menus[menu_a_mostrar][caracter_tuplo], end='', flush=True) # Caso não seja um caracter mutavel imprime-lo em str                
                print('\n --------> Este lugar já se encontra ocupado \n           Escolha outro, por favor')
            
        else:  #Caso escolher um lugar que não existe
            print('')
            print('-------> Este lugar não existe \n         Por favor, escolha um lugar existente')
            print('')
            
      
    elif menu_a_mostrar == 5: #Menu Sair
        
        if opção_desejada == 0: #Menu Sair --> Volta ao Menu Anterior
            menu_a_mostrar= 0
        
        elif opção_desejada == 1: # Seleciona a opção para indicar o andar  e o lugar em que foi estacionado o veiculo
            
            andar_estacionado = eval(input('Indique o andar: ')) # Indica o andar
            
            if andar_estacionado == 1: # Se a indicação corresponde ao Andar 1
                
                lugar_estacionado = eval(input('Indique o lugar: ')) # Indica o lugar
                
                if lugar_estacionado >= 1 and lugar_estacionado <= 20: # Lugares para estacionar possiveis 1-20
                    
                    for lugar in ocupação_andar_1: # Cada Lugar do Andar 1
                        if lugar == lugar_estacionado and ocupação_andar_1[lugar][0] == 'X': # Verifica se o lugar selecionado, realmente esta ocupado.
                            menu_a_mostrar = 6 # Transição ao Menu Pagar
                            break
                        
                        else:
                            if lugar == lugar_estacionado and ocupação_andar_1[lugar][0] != 'X': # Caso o Lugar não este ocupado
                                print('\n--------> Não se encontra nenhum veiculo estacionado neste lugar \n          Tente de Novo') # Caso indique um lugar que não esta ocupado
                            
                else:
                    print('\n-------> Não Existe o Lugar Indicado \n         Tente de Novo') # Caso indique um lugar que não existe neste parking             
                      
            elif andar_estacionado == 2: # Se a indicação corresponde ao Andar 1     
                
                lugar_estacionado = eval(input('Indique o lugar: ')) # Indica o lugar
                
                if lugar_estacionado >= 1 and lugar_estacionado <= 10: # Lugares para estacionar possiveis 1-20
                    for lugar in ocupação_andar_2: # Cada Lugar do Andar 2
                        if lugar == lugar_estacionado and ocupação_andar_2[lugar][0] == 'X': # Verifica se o lugar selecionado, realmente esta ocupado.
                            menu_a_mostrar = 6 # Transição ao Menu Pagar
                            break
                        
                        else:
                            if lugar == lugar_estacionado and ocupação_andar_1[lugar][0] != 'X': # Caso o Lugar não este ocupado
                                print('\n--------> Não se encontra nenhum veiculo estacionado neste lugar \n          Tente de Novo') # Caso indique um lugar que não esta ocupado
                else:
                    print('\n-------> Não Existe o Lugar Indicado \n         Tente de Novo') # Caso indique um lugar que não existe neste parking
            
            else:
                print('\n-------> Não Existe o Andar Indicado \n         Tente de Novo') # Caso não exista o andar
        
        else: #Caso escolham uma opção não existente no Menu Sair
            print('')
            print('-------> Opção Invalida \n         Por favor, escolha uma das opções apresentadas no ecrã')
            
    
    elif menu_a_mostrar == 6: #Menu Pagar
        
        if andar_estacionado == 1:
            tempo= abs(ocupação_andar_1[lugar_estacionado][1] - time()) #Calcula o tempo que estive o veiculo estacionado
            valor_a_pagar = 0.02 * (tempo / 60) #Calcular o valor a pagar, sabendo que este andar cobra 10€ por minuto
        
        elif andar_estacionado == 2:
            tempo= abs(ocupação_andar_2[lugar_estacionado][1] - time()) #Calcula o tempo que estive o veiculo estacionado
            valor_a_pagar =  0.01 * (tempo / 60) #Calcular o valor a pagar, sabendo que este andar cobra 5€ por minuto
            
        
        valor_introduzido= 0 #Valor introduzido pelo usuario
        
        total_a_pagar = valor_a_pagar # Total que se mostra no Menu a Pagar aos usuarios
        
        
        while menu_a_mostrar == 6: #Ciclo para o Menu Pagar
            
            for caracter_tuplo in range(0, len(tuplo_menus[menu_a_mostrar]),1): #Percorre cada caracter do Menu Pagar
                if tuplo_menus[menu_a_mostrar][caracter_tuplo] == 'F': #Condição para substituir os caracteres mutaveis
                    print(round(total_a_pagar,2), end='', flush=True) #Muda o F pelo Total a Pagar
                    
                else:
                    print(tuplo_menus[menu_a_mostrar][caracter_tuplo], end='', flush=True) # Caso não seja um caracter mutavel imprime-lo em str                          
                  
            if valor_introduzido > valor_a_pagar: # Caso o usuario ja tenha pago o parking
                
                menu_a_mostrar = 7 #Menu pagar -----> Talão
                print('')
                print('-------> O troco é',round((abs(valor_a_pagar - valor_introduzido)),2),'€') #Mostra o troco recibido
                
                valor_acumulado += valor_a_pagar #Soma dos valores pagados pelos usuarios que usaram o parking
                
                
                if menu_a_mostrar == 7: #Talão
                    for caracter_tuplo in range(0, 273,1): #Percorre cada caracter do Talão até o primeiro F
                                        if tuplo_menus[menu_a_mostrar][caracter_tuplo] == 'F': #Condição para substituir os caracteres mutaveis
                                            print(andar_estacionado, end='', flush=True) #Substitui o F pelo andar indicado
                                        else:
                                            print(tuplo_menus[menu_a_mostrar][caracter_tuplo], end='', flush=True) 
                    for caracter_tuplo in range(273, 323,1): #Percorre cada caracter do Talão até o segundo F
                        if tuplo_menus[menu_a_mostrar][caracter_tuplo] == 'F': #Condição para substituir os caracteres mutaveis
                            print(lugar_estacionado, end='', flush=True) #Substitui o F pelo lugar indicado
                        else:
                            print(tuplo_menus[menu_a_mostrar][caracter_tuplo], end='', flush=True)
                    for caracter_tuplo in range(323, 384,1): #Percorre cada caracter do Talão até o terceiro F
                        if tuplo_menus[menu_a_mostrar][caracter_tuplo] == 'F': #Condição para substituir os caracteres mutaveis
                            
                            if andar_estacionado == 1:
                                for chave in dicionario_historicos: 
                                    if chave == ocupação_andar_1[lugar_estacionado][2]: # Verifica se o número de cliente é igual ao seu atribuido
                                            print(dicionario_historicos[chave][0], end='', flush=True)  #Substitui o F pela hora de entrada correspondentes ao numero de cliente
                            
                            elif andar_estacionado == 2:              
                                for chave in dicionario_historicos:
                                    if chave == ocupação_andar_2[lugar_estacionado][2]: # Verifica se o número de cliente é igual ao seu atribuido
                                        print(dicionario_historicos[chave][0], end='', flush=True)  #Substitui o F pela hora de entrada correspondentes ao numero do cliente
                        
                        else:
                            print(tuplo_menus[menu_a_mostrar][caracter_tuplo], end='', flush=True) 
                    
                    for caracter_tuplo in range(384, 432,1): #Percorre cada caracter do Menu Lugar 1
                        if tuplo_menus[menu_a_mostrar][caracter_tuplo] == 'F': #Condição para substituir os caracteres mutaveis
                            hora_saida= datetime.now() #Hora de Saida
                            hora_saida_formatada = hora_saida.strftime('%H:%M:%S') #Hora Saida Formatada                                        
                            print(hora_saida_formatada, end='', flush=True) #Substitui o F pela hora de saida
                                        
                        else:
                            print(tuplo_menus[menu_a_mostrar][caracter_tuplo], end='', flush=True)
                    
                    for caracter_tuplo in range(432, len(tuplo_menus[menu_a_mostrar]),1): #Percorre cada caracter do Menu Lugar 1
                        if tuplo_menus[menu_a_mostrar][caracter_tuplo] == 'F': #Condição para substituir os caracteres mutaveis
                            print(round(valor_a_pagar,2), end='', flush=True)
                        else:
                            print(tuplo_menus[menu_a_mostrar][caracter_tuplo], end='', flush=True)                    
                
                
                if andar_estacionado == 1: #Caso o andar de onde se retira o carro, seja o andar 1
                    
                    for chaves in dicionario_historicos:
                        if chaves == ocupação_andar_1[lugar_estacionado][2]: #Verifica se o número de cliente é igual ao atribuido
                            hora_saida= datetime.now() #Hora de Saida
                            hora_saida_formatada = hora_saida.strftime('%H:%M:%S') #Hora Saida Formatada
                            dicionario_historicos[chaves] += [hora_saida_formatada, round(valor_a_pagar,2)] #Adiciona ao historico a hora de saida e valor que pagou
                            break
                    
                    lugares_ocupados_1 -= 1 #Saida de veiculos presentes no andar 1
                    ocupação_andar_1[lugar_estacionado] = ['_','X'] #Atualiza o lugar ocupado para lugar disponivel
                    
                
                elif andar_estacionado == 2: #Caso o andar de onde se retira o carro, seja o andar 2
                    
                    for chaves in dicionario_historicos:
                        if chaves == ocupação_andar_2[lugar_estacionado][2]: #Verifica se o número de cliente é igual ao atribuido
                            hora_saida= datetime.now() #Hora de Saida
                            hora_saida_formatada = hora_saida.strftime('%H:%M:%S') #Hora Saida Formatada
                            dicionario_historicos[chaves] += [hora_saida_formatada, round(valor_a_pagar,2)] #Adiciona ao historico a hora de saida e valor que pagou                   
                            break
                    
                    lugares_ocupados_2 -= 2 #Saida de veiculos presentes no andar 2  
                    ocupação_andar_2[lugar_estacionado] = ['_','X'] #Atualiza o lugar ocupado para lugar disponivel
                
                break         
                    
            voltar_ou_moedas= eval(input('Escolha voltar ou insira moedas em centimos: ')) / 100 #Escolhe se voltar ou insire as moedas
            print('')
            print('-------> Moedas aceites: 0.01€, 0.02€, 0.05€, 0.10€, 0.20€, 0.50€') #Mostra moedas aceites 
            
            if voltar_ou_moedas == 0: #Volta ao Menu Anterior
                menu_a_mostrar= 5
                break
                    
            elif voltar_ou_moedas == 0.01 or voltar_ou_moedas == 0.02 or voltar_ou_moedas == 0.05 or voltar_ou_moedas == 0.10 or voltar_ou_moedas == 0.20 or voltar_ou_moedas == 0.50: # O usuario vai introduzindo moedas até pagar
                valor_introduzido += voltar_ou_moedas #Soma para mostrar ao cliente o valor que tem introduzido
                total_a_pagar = abs(round(total_a_pagar - voltar_ou_moedas, 2)) #Atualiza o valor que se mostra no Menu a Pagar, mostrando o restante que falta por pagar aos usuarios
                print('')
                print('-------> Introduziu',round(valor_introduzido,2),'€') #Mostra ao usuario o valor que já introduziu
            
            elif voltar_ou_moedas != 0.01 or voltar_ou_moedas != 0.02 or voltar_ou_moedas != 0.05 or voltar_ou_moedas != 0.10 or voltar_ou_moedas != 0.20 or voltar_ou_moedas != 0.50: #Caso introduza um valor não aceite
                print('')
                print('-------> Valor não aceite')
                print('         Tente de Novo')
    
    elif menu_a_mostrar == 7: # Talão
        
        if opção_escolhida == 0: # Escolher voltar ao Menu Principal
            menu_a_mostrar = 0
        
        else: #Caso escolham uma opção não existente no Menu Talão
            print('')
            print('-------> Opção Invalida \n         Por favor, escolha uma das opções apresentadas no ecrã')     
            
    
          
    elif menu_a_mostrar == 8: #Menu Administrador
        
        if opção_escolhida == 0: # #Menu Administrador --> Volta ao Menu principal
                if iniciar_ou_parar == True:
                    menu_a_mostrar = 0
                
                else:
                    print('')
                    print('-------> O parking encontra-se fechado')
        
        elif opção_escolhida == 1: #Menu Administrador --> Menu Andares
                menu_a_mostrar = 9
                if menu_a_mostrar == 9 and ocupação_andar_1 != None and ocupação_andar_2 != None: #Menu Escolha Lugar 1
                    controlo_lugares = 1 #Control de cada um dos lugares do Parking
                    for caracter_tuplo in range(0, 348,1): #Percorre cada caracter do Menu Lugar 1
                                        if tuplo_menus[menu_a_mostrar][caracter_tuplo] == 'F': #Condição para substituir os caracteres mutaveis
                                            print(ocupação_andar_1[controlo_lugares][0], end='', flush=True)
                                            controlo_lugares += 1 #Seguinte Lugar
                                        else:
                                            print(tuplo_menus[menu_a_mostrar][caracter_tuplo], end='', flush=True)
                    controlo_lugares = 1 #Control de cada um dos lugares do Parking
                    for caracter_tuplo in range(348,len(tuplo_menus[menu_a_mostrar]),1): #Percorre cada caracter do Menu Lugar 1
                        if tuplo_menus[menu_a_mostrar][caracter_tuplo] == 'F': #Condição para substituir os caracteres mutaveis
                            print(ocupação_andar_2[controlo_lugares][0], end='', flush=True)
                            controlo_lugares += 1 #Seguinte Lugar
                        else:
                            print(tuplo_menus[menu_a_mostrar][caracter_tuplo], end='', flush=True)
        
        elif opção_escolhida == 3: #Função que abre ou encerra o parking
            
            senha= eval(input('Introduza a senha: ')) #Pede ao usuario a senha para verificar que se trata do administrador
            
            if senha == senha_do_administrador: #Verifica se o valor introduzido é igual a senha do administrador
                
                if iniciar_ou_parar == True: #Se o parking estiver aberto
                    iniciar_ou_parar = False #Encerra o parking
                    print('')
                    print('-------> Parking Fechado')
                
                elif iniciar_ou_parar == False: #Se o parking estiver fechado
                    iniciar_ou_parar = True #Abre o parking
                    print('')
                    print('-------> Parking Aberto')
                
            
        
        else: #Caso escolham uma opção não existente no Menu Principal
            if not opção_escolhida == 2:
                print('')
                print('-------> Opção Invalida \n         Por favor, escolha uma das opções apresentadas no ecrã')        
        
        
    elif menu_a_mostrar == 9:#Ver Andares 
                    
        if opção_escolhida == 0: #Ver Andares --> Volta
            menu_a_mostrar = 8
                    
        else: #Caso escolham uma opção não existente no Menu Andares
            print('')
            print('-------> Opção Invalida \n         Por favor, escolha uma das opções apresentadas no ecrã')        
            print('')
    
    
    
                   

    
            
    
    
    
        
  
            
      
        
    
        
                
                
            
                
                
        
    
                
        
        
                          
            
            
                
            
            
            
