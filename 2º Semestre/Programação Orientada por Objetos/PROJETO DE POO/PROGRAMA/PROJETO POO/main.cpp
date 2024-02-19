//
//  main.cpp
//  PROJETO POO
//
//  Created by Miguel PeÒaranda, Jackeline Camara and Cristina Santos on 24/05/2023.
//

#include <iostream>
#include <math.h>
#include <iomanip>
#include <cstdlib>

using namespace std;

class stock {
private:
    double precio;
    char* nome;
public:
    int quantity;
    stock(int x, double y, char* z) {
        quantity = x;
        precio = y;
        nome = z;
    }
    friend void shop_process(stock& p);
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
                
            default:
                if (opcao != -1){
                    cout << " A opcao escolhida nao existe \n";
                    system("pause");
                    system("cls");
                }
                break;
        }
    } while (opcao != -1);
}


