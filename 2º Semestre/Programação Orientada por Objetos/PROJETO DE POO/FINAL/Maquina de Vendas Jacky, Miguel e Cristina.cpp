//
//  main.cpp
//  PROJETO POO
//
//  Created by Miguel Peñaranda, Jackeline Camara and Cristina Santos on 24/05/2023.
//

#include <iostream>
#include <math.h>
#include <iomanip>
#include <cstdlib>

using namespace std;

int passwordAdmin = 4321;

class stock {
private:
	double precio;
	int quantity;
public:
    char* nome;
    stock(int x, double y, char* z) {
        quantity = x;
        precio = y;
        nome = z;
    }
    
    int getStock() {
    	return quantity;
    }
    
    friend void shop_process(stock& p);
    friend void verificarStock(stock& p);
};


void recibo(char const nome[20], double precio,  double valor_recibido, double Troco){
    cout << " ------------------------------- \n";
    cout << "|                               |\n";
    cout << "|             Recibo            |\n";
    cout << "|                               |\n";
    cout << "|     Produto: " << nome << "        |\n" ;
    cout << "|     Preco: " << precio << "               |\n";
    cout << "|     Valor recibido: " << valor_recibido << "      |\n";
    cout << "|     Troco: " << fixed << setprecision(2) << Troco << "               |\n";
    cout << "|                               |\n";
    cout << " ------------------------------- \n";
}

void devolveMoedas(double valor_a_trocar) {
    double total_a_trocar = valor_a_trocar;
    double listaMoedas[8] = { 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01 };
    int longitud = sizeof(listaMoedas) / sizeof(listaMoedas[0]);
    
    for (int i = 0; i < longitud; i++) {
        double moeda = listaMoedas[i];
        int devolve = 0;
        
        while (total_a_trocar >= moeda) {
            devolve += 1;
            total_a_trocar -= moeda;
        }
        if ((moeda == 1 || moeda == 2) && devolve != 0) {
            cout << devolve << " moedas de " << fixed << setprecision(2) << moeda << " euros \n";
        }
        else if (moeda < 1 && devolve != 0) {
            cout << devolve << " moedas de " << fixed << setprecision(2) << moeda << " centimos \n";
        }
    }
    if (total_a_trocar > 0.00000000000001 && total_a_trocar <= 0.01) {
        cout << 1 << " moedas de " << fixed << setprecision(2) << 0.01 << " centimos \n";
    }
};

void shop_process(stock& p){
    double total_a_pagar = 0;
    double troco;
    double moeda = 0;
    double valor_introduzido = 0;
    char* const nome = p.nome;
    
    if (p.quantity > 0) {
        cout << "Quantidade em stock: " << p.quantity << "\n";
        cout << "Valor a pagar: " << p.precio << "\n";
        total_a_pagar = p.precio;
        while (total_a_pagar > 0) {
            cout << "Insira moedas: ";
            cin >> moeda;
            cout << "\n";
            
            if ( moeda == 0.01 || moeda == 0.02 || moeda == 0.05 || moeda == 0.10 || moeda == 0.20 || moeda == 0.50 || moeda == 1 || moeda == 2) {
                total_a_pagar -= moeda;
                valor_introduzido += moeda;
                if (total_a_pagar > 0) {
                    cout << "Valor restante a pagar: " << total_a_pagar << "\n";
                }
            } else {
                cout << "Moeda nao valida \n\n";
            }
        }
        p.quantity -= 1;
        troco = fabs(p.precio - valor_introduzido);
        
        if (troco > 0) {
            cout << "Troco: " << fixed << setprecision(2) << troco << "\n\n";
            cout << "Moedas devolvidas: \n";
            devolveMoedas(troco);
            system("pause");
            system("cls");
        } else {system("cls");}
        recibo(nome, p.precio, valor_introduzido, troco);
        system("pause");
        system("cls");
    } else {
        cout << "Stock indesponivel do produto selecionado! \n";
        system("pause");
        system("cls");
    }
}

void verificarStock(stock& p) {
	if (p.quantity < 5) {
		cout << "\nProduto selecionado: " << p.nome << "\n";
		cout << "Quantidade em stock: " << p.quantity << "\n";
		cout << "\nEscreva a quantidade a adicionar: "; int quant; cin >> quant;
		
		if ( quant > 0){
		
			if (p.quantity == 4 && quant < 2){
				p.quantity += quant;
			}
			else if (p.quantity == 3 && quant < 3) {
				p.quantity += quant;
			}
			else if (p.quantity == 2 && quant < 4) {
				p.quantity += quant;
			}
			else if (p.quantity == 1 && quant < 5) {
				p.quantity += quant;
			}
			else if (p.quantity == 0 && quant < 6) {
				p.quantity += quant;
			} 
			else {
				cout << "No maximo so podem existir 5 produtos em stock \n";
				system("pause");
			}
		}
		else{
			cout << "O valor introduzido tem de ser um valor positivo.\n";
			system("pause");
		}
		
		system("cls");
	} else {
		cout << "Stock maximo atingido para o produto selecionado \n";
		system("pause");
		system("cls");
	}	
}

int main(){
    stock p11 (2, 1.50, "Coca-Cola");
    stock p12 (2, 1.50, "Pepsi");
    stock p13 (2, 0.90, "Snickers");
    stock p14 (2, 1.20, "Doritos");
    stock p21 (2, 0.90, "KitKat");
    stock p22 (2, 0.90, "Twix");
    stock p23 (2, 1, "M&M's");
    stock p24 (2, 1, "Pringles");
    stock p31 (2, 1.20, "Lays");
    stock p32 (2, 1.50, "Fanta");
    stock p33 (2, 1.50, "Sprite");
    stock p34 (2, 1, "Trident");
    stock p41 (2, 1, "Skittles");
    stock p42 (2, 2, "Oreo");
    stock p43 (2, 2, "Mars");
    stock p44 (2, 1.20, "Ruffles");
    stock p51 (2, 2, "Nutella");
    stock p52 (2, 2, "Red Bull");
    stock p53 (2, 1.50, "Nestea");
    stock p54 (2, 1, "Mentos");
    
    
    int opcao;
        
    do {
        cout << " --------------------------------------------------------------------\n";
        cout << "|                                                                    |\n";
        cout << "|                         Maquinas de Vendas                         |\n";
        cout << "|                                                                    |\n";
        cout << "|   11 - Coca-Cola   12 - Pepsi      13 - Snickers    14 - Doritos   |\n";
        cout << "|                                                                    |\n";
        cout << "|   21 - KitKat      22 - Twix       23 - M&M's       24 - Pringles  |\n";
        cout << "|                                                                    |\n";
        cout << "|   31 - Lays        32 - Fanta      33 - Sprite      34 - Trident   |\n";
        cout << "|                                                                    |\n";
        cout << "|   41 - Skittles    42 - Oreo       43 - Mars        44 - Ruffles   |\n";
        cout << "|                                                                    |\n";
        cout << "|   51 - Nutella     52 - Red Bull   53 - Nestea      54 - Mentos    |\n";
        cout << "|                                                                    |\n";
        cout << "|                                                                    |\n";
        cout << " --------------------------------------------------------------------\n";
        cout << "Qual o produto: "; cin >> opcao;
    
        switch (opcao) {
 			               
        	case 11:
                shop_process(p11);
                break;
            
           	case 12:
               	shop_process(p12);
                break;
            
            case 13:
               shop_process(p13);
                break;
            
            case 14:
                shop_process(p14);
                break;
            
            case 21:
               	shop_process(p21);
                break;
            
            case 22:
                shop_process(p22);
                break;
            
            case 23:
               	shop_process(p23);
                break;
            
            case 24:
               	shop_process(p24);
                break;
                
            case 31:
                shop_process(p31);
                break;
            
            case 32:
               	shop_process(p32);
                break;
            
            case 33:
                shop_process(p33);
                break;
            
            case 34:
                shop_process(p34);
                break;
                
            case 41:
                shop_process(p41);
                break;
            
            case 42:
                shop_process(p42);
                break;
            
            case 43:
               	shop_process(p43);
                break;
            
            case 44:
                shop_process(p44);
                break;
            
            case 51:
                shop_process(p51);
                break;
            
            case 52:
                shop_process(p52);
                break;
            
            case 53:
                shop_process(p53);
                break;
            
            case 54:
               	shop_process(p54);
                break;
                
            case 99:
				system("cls");
				int opcaoAdmin;
				cout << "Insira a passe de administrador: "; int pass; cin >> pass;
				if (passwordAdmin == pass) {
					system("cls");
					do {
				cout << "-----------------------------------------------------------------------\n";
			    cout << "|                                                                       |\n";
			    cout << "|\t\t\t    Maquinas de Vendas \t\t                |\n";
			    cout << "|\t\t\t       Administrador   \t\t                |\n";
			    cout << "|                                                                       |\n";
			    cout << "|   1 - Verificar Stock                                                 |\n";
			    cout << "|                                                                       |\n";
			    cout << "|   0 - Voltar ao menu normal                                           |\n";
			    cout << "|                                                                       |\n";
			    cout << "-----------------------------------------------------------------------\n";
			    cout << "Escoha uma opcao: "; cin >> opcaoAdmin;
			    
			    switch (opcaoAdmin) {
			    	case 1:
			    		system("cls");
						int opcaoStocks;
						do {
							cout << " --------------------------------------------------------------------------------\n";
					        cout << "|                                                                   		 |\n";
					        cout << "|                                Reposicao dos Produtos                        	 |\n";
					        cout << "|                                                                                |\n";
					        cout << "|   11 - Coca-Cola("<<p11.getStock()<<")   12 - Pepsi("<<p12.getStock()<<")      13 - Snickers("<<p13.getStock()<<")    14 - Doritos("<<p14.getStock()<<")   |\n";
					        cout << "|                                                                                |\n";
					        cout << "|   21 - KitKat("<<p21.getStock()<<")      22 - Twix("<<p22.getStock()<<")       23 - M&M's("<<p23.getStock()<<")       24 - Pringles("<<p24.getStock()<<")  |\n";
					        cout << "|                                                                                |\n";
					        cout << "|   31 - Lays("<<p31.getStock()<<")        32 - Fanta("<<p32.getStock()<<")      33 - Sprite("<<p33.getStock()<<")      34 - Trident("<<p34.getStock()<<")   |\n";
					        cout << "|                                                                                |\n";
					        cout << "|   41 - Skittles("<<p41.getStock()<<")    42 - Oreo("<<p42.getStock()<<")       43 - Mars("<<p43.getStock()<<")        44 - Ruffles("<<p44.getStock()<<")   |\n";
					        cout << "|                                                                                |\n";
					        cout << "|   51 - Nutella("<<p51.getStock()<<")     52 - Red Bull("<<p52.getStock()<<")   53 - Nestea("<<p53.getStock()<<")      54 - Mentos("<<p54.getStock()<<")    |\n";
					        cout << "|                                                                                |\n";
					        cout << "|                         0 - Voltar ao menu administrador                       |\n";
					        cout << "|                                                                                |\n";
					        cout << " --------------------------------------------------------------------------------\n";
					        cout << "Escolhe uma opcao: "; cin >> opcaoStocks;
					        
					        switch (opcaoStocks) {
					        	case 11:
					                verificarStock(p11);
					                break;
					            
					           	case 12:
					               	verificarStock(p12);
					                break;
					            
					            case 13:
					               	verificarStock(p13);
					                break;
					            
					            case 14:
					                verificarStock(p14);
					                break;
					            
					            case 21:
					               	verificarStock(p21);
					                break;
					            
					            case 22:
					               	verificarStock(p22);
					                break;
					            
					            case 23:
					               	verificarStock(p23);
					                break;
					            
					            case 24:
					               	verificarStock(p24);
					                break;
					                
					            case 31:
					               	verificarStock(p31);
					                break;
					            
					            case 32:
					               	verificarStock(p32);
					                break;
					            
					            case 33:
					               	verificarStock(p33);
					                break;
					            
					            case 34:
					                verificarStock(p34);
					                break;
					                
					            case 41:
					                verificarStock(p41);
					                break;
					            
					            case 42:
					                verificarStock(p42);
					                break;
					            
					            case 43:
					               	verificarStock(p43);
					                break;
					            
					            case 44:
					                verificarStock(p44);
					                break;
					    
					            case 51:
					                verificarStock(p51);
									 break;					               
					            
					            case 52:
					                verificarStock(p52);
					                break;
					            
					            case 53:
					                verificarStock(p53);
					                break;
					            
					            case 54:
					               	verificarStock(p54);
					                break;
					            
								default:
						    		if (opcaoStocks != 0){
						    			cout << "A opcao escolhida nao existe, tente novamente \n";
						    			system("pause");
						    		}
						    		system("cls");
						    		break;
					        }
						} while (opcaoStocks != 0);
						system("cls");
			    		break;
			    	
			    	default:
			    		if (opcaoAdmin != 0){
			    			cout << "A opcao escolhida nao existe, tente novamente \n";
			    		}
			    		system("cls");
			    		break;
			    }
			    } while (opcaoAdmin != 0);
				}
				else {
					cout << "Palavra-passe errada \n";
					system("pause");
				}
			    system("cls");
				                
            default:
                if (opcao != -1 & opcao != 99){
                	cout << " A opcao escolhida nao existe \n";
	                system("pause");
	                system("cls");
                }
                break;
				        }
	} while (opcao != -1);
}



