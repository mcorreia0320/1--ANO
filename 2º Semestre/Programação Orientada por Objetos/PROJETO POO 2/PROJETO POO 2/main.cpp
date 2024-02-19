//
//  main.cpp
//  PROJETO POO
//
//  Created by Miguel Angel Correia Penaranda on 24/05/2023.
//

#include <iostream>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <iomanip>
#include <cmath>

using namespace std;

class stock {
public:
    int quantity;
    double precio;
    stock(int x, double y) {
        quantity = x;
        precio = y;
    }
};

void recibo(char const nome[20], double precio,  double valor_recibido, double Troco){
    cout << " ------------------------------- \n";
    cout << "|                               |\n";
    cout << "|             Recibo            |\n";
    cout << "|                               |\n";
    cout << "|     Produto: " << nome << "        |\n" ;
    cout << "|     Preco: " << precio << "              |\n";
    cout << "|     Valor recibido: " << valor_recibido << "       |\n";
    cout << "|     Troco: " << fixed << setprecision(2) << Troco << "                |\n";
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



int main(){
    stock p11 (2, 1.50);
    stock p12 (2, 1.50);
    stock p13 (2, 0.90);
    stock p14 (2, 1.20);
    stock p21 (2, 0.90);
    stock p22 (2, 0.90);
    stock p23 (2, 1);
    stock p24 (2, 1);
    stock p31 (2, 1.20);
    stock p32 (2, 1.50);
    stock p33 (2, 1.50);
    stock p34 (2, 1);
    stock p41 (2, 1);
    stock p42 (2, 2);
    stock p43 (2, 2);
    stock p44 (2, 1.20);
    stock p51 (2, 2);
    stock p52 (2, 2);
    stock p53 (2, 1.50);
    stock p54 (2, 1);
    
    int opcao;
    double total_a_pagar;
    double troco;
    double moeda;
    double valor_introduzido;
        
    do {
        moeda = 0;
        total_a_pagar = 0;
        valor_introduzido = 0;
        
        cout << " -------------------------------------------------------------------\n";
        cout << "|                                                                   |\n";
        cout << "|\t\t\t\t\t    Maquinas de Vendas \t\t\t\t\t        |\n";
        cout << "|                                                                   |\n";
        cout << "|   11 - Coca-Cola \t 12 - Pepsi \t 13 - Snickers \t 14 - Doritos   |\n";
        cout << "|                                                                   |\n";
        cout << "|   21 - KitKat \t 22 - Twix \t     23 - M&M's \t 24 - Pringles  |\n";
        cout << "|                                                                   |\n";
        cout << "|   31 - Lays \t     32 - Fanta \t 33 - Sprite \t 34 - Trident   |\n";
        cout << "|                                                                   |\n";
        cout << "|   41 - Skittles \t 42 - Oreo \t     43 - Mars \t     44 - Ruffles   |\n";
        cout << "|                                                                   |\n";
        cout << "|   51 - Nutella \t 52 - Red Bull \t 53 - Nestea \t 54 - Mentos    |\n";
        cout << "|                                                                   |\n";
        cout << "|                                                                   |\n";
        cout << " -------------------------------------------------------------------\n";
        cout << "Qual o produto: "; cin >> opcao;
    
        switch (opcao) {
            
            case 11:
                if (p11.quantity > 0) {
                    cout << "Quantidade em stock: " << p11.quantity << "\n";
                    cout << "Valor a pagar: " << p11.precio << "\n";
                    total_a_pagar = p11.precio;
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
                    p11.quantity -= 1;
                    troco = fabs(p11.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << fixed << setprecision(2) << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Coca-Cola", p11.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 12:
                if (p12.quantity > 0) {
                    cout << "Quantidade em stock: " << p12.quantity << "\n";
                    cout << "Valor a pagar: " << p12.precio << "\n";
                    total_a_pagar = p12.precio;
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
                    p12.quantity -= 1;
                    troco = fabs(p12.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Pepsi", p12.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 13:
                if (p13.quantity > 0) {
                    cout << "Quantidade em stock: " << p13.quantity << "\n";
                    cout << "Valor a pagar: " << p13.precio << "\n";
                    total_a_pagar = p13.precio;
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
                            cout << "Moeda não valida \n\n";
                        }
                    }
                    p13.quantity -= 1;
                    troco = fabs(p13.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Snickers", p13.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 14:
                if (p14.quantity > 0) {
                    cout << "Quantidade em stock: " << p14.quantity << "\n";
                    cout << "Valor a pagar: " << p14.precio << "\n";
                    total_a_pagar = p14.precio;
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
                    p14.quantity -= 1;
                    troco = fabs(p14.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Doritos", p14.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 21:
                if (p21.quantity > 0) {
                    cout << "Quantidade em stock: " << p21.quantity << "\n";
                    cout << "Valor a pagar: " << p21.precio << "\n";
                    total_a_pagar = p21.precio;
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
                    p21.quantity -= 1;
                    troco = fabs(p21.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("KitKat", p21.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 22:
                if (p22.quantity > 0) {
                    cout << "Quantidade em stock: " << p22.quantity << "\n";
                    cout << "Valor a pagar: " << p22.precio << "\n";
                    total_a_pagar = p22.precio;
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
                    p22.quantity -= 1;
                    troco = fabs(p22.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Twix", p22.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 23:
                if (p23.quantity > 0) {
                    cout << "Quantidade em stock: " << p23.quantity << "\n";
                    cout << "Valor a pagar: " << p23.precio << "\n";
                    total_a_pagar = p23.precio;
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
                    p23.quantity -= 1;
                    troco = fabs(p23.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("M&M's", p23.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 24:
                if (p24.quantity > 0) {
                    cout << "Quantidade em stock: " << p24.quantity << "\n";
                    cout << "Valor a pagar: " << p24.precio << "\n";
                    total_a_pagar = p24.precio;
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
                    p24.quantity -= 1;
                    troco = fabs(p24.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Pringles", p24.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
                
            case 31:
                if (p31.quantity > 0) {
                    cout << "Quantidade em stock: " << p31.quantity << "\n";
                    cout << "Valor a pagar: " << p31.precio << "\n";
                    total_a_pagar = p31.precio;
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
                    p31.quantity -= 1;
                    troco = fabs(p31.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Lays", p31.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 32:
                if (p32.quantity > 0) {
                    cout << "Quantidade em stock: " << p32.quantity << "\n";
                    cout << "Valor a pagar: " << p32.precio << "\n";
                    total_a_pagar = p32.precio;
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
                    p32.quantity -= 1;
                    troco = fabs(p32.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Fanta", p32.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 33:
                if (p33.quantity > 0) {
                    cout << "Quantidade em stock: " << p33.quantity << "\n";
                    cout << "Valor a pagar: " << p33.precio << "\n";
                    total_a_pagar = p33.precio;
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
                    p33.quantity -= 1;
                    troco = fabs(p33.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Sprite", p33.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 34:
                if (p34.quantity > 0) {
                    cout << "Quantidade em stock: " << p14.quantity << "\n";
                    cout << "Valor a pagar: " << p34.precio << "\n";
                    total_a_pagar = p34.precio;
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
                    p34.quantity -= 1;
                    troco = fabs(p34.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Trident", p34.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
                
            case 41:
                if (p41.quantity > 0) {
                    cout << "Quantidade em stock: " << p41.quantity << "\n";
                    cout << "Valor a pagar: " << p41.precio << "\n";
                    total_a_pagar = p41.precio;
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
                    p41.quantity -= 1;
                    troco = fabs(p41.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Skittles", p41.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                    
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 42:
                if (p42.quantity > 0) {
                    cout << "Quantidade em stock: " << p42.quantity << "\n";
                    cout << "Valor a pagar: " << p42.precio << "\n";
                    total_a_pagar = p42.precio;
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
                    p42.quantity -= 1;
                    troco = fabs(p42.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Oreo", p42.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 43:
                if (p43.quantity > 0) {
                    cout << "Quantidade em stock: " << p43.quantity << "\n";
                    cout << "Valor a pagar: " << p43.precio << "\n";
                    total_a_pagar = p43.precio;
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
                    p43.quantity -= 1;
                    troco = fabs(p43.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Mars", p43.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 44:
                if (p44.quantity > 0) {
                    cout << "Quantidade em stock: " << p44.quantity << "\n";
                    cout << "Valor a pagar: " << p44.precio << "\n";
                    total_a_pagar = p44.precio;
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
                    p44.quantity -= 1;
                    troco = fabs(p44.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Ruffles", p44.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 51:
                if (p51.quantity > 0) {
                    cout << "Quantidade em stock: " << p51.quantity << "\n";
                    cout << "Valor a pagar: " << p51.precio << "\n";
                    total_a_pagar = p51.precio;
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
                    p51.quantity -= 1;
                    troco = fabs(p51.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Nutella", p51.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 52:
                if (p52.quantity > 0) {
                    cout << "Quantidade em stock: " << p52.quantity << "\n";
                    cout << "Valor a pagar: " << p44.precio << "\n";
                    total_a_pagar = p52.precio;
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
                    p52.quantity -= 1;
                    troco = fabs(p52.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Red Bull", p52.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 53:
                if (p53.quantity > 0) {
                    cout << "Quantidade em stock: " << p53.quantity << "\n";
                    cout << "Valor a pagar: " << p53.precio << "\n";
                    total_a_pagar = p53.precio;
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
                    p53.quantity -= 1;
                    troco = fabs(p53.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Nestea", p53.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
            
            case 54:
                if (p54.quantity > 0) {
                    cout << "Quantidade em stock: " << p54.quantity << "\n";
                    cout << "Valor a pagar: " << p54.precio << "\n";
                    total_a_pagar = p54.precio;
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
                    p54.quantity -= 1;
                    troco = fabs(p54.precio - valor_introduzido);
                    
                    if (troco > 0) {
                        cout << "Troco: " << troco << "\n\n";
                        cout << "Moedas devolvidas: \n";
                        devolveMoedas(troco);
                        system("pause");
                        system("cls");
                    } else {system("cls");}
                    recibo("Mentos", p54.precio, valor_introduzido, troco);
                    system("pause");
                    system("cls");
                    break;
                } else {
                    cout << "Stock indesponivel do produto selecionado! \n";
                    system("pause");
                    system("cls");
                    break;
                }
                
            default:
                cout << " A opção escolhida não existe \n";
                break;
        }
    } while (opcao != -1);
}
