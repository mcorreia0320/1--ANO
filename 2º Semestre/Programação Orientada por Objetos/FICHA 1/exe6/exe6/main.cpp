//
//  main.cpp
//  exe6
//
//  Created by Miguel Angel Correia Penaranda on 15/03/2023.
//

#include <iostream>

using namespace std;

int main () {
    float preço, unidades, valor_a_pagar, desconto;
    
    preço = 13;
    
    cout << "Indique a quantidade que deseja comprar: ";
    cin >> unidades;
    
    if (unidades < 500){
        valor_a_pagar = (unidades * 13);
        cout << "O valor a pagar é de " << valor_a_pagar << "\n";
    }
    else if (unidades >= 500 && unidades <= 1000) {
        valor_a_pagar = (unidades * 13);
        desconto = (valor_a_pagar * 0.05);
        valor_a_pagar = valor_a_pagar - desconto;
        cout << "O valor a pagar é de " << valor_a_pagar << " com um desconto de 5% \n";
    }
    else if (unidades > 1000) {
        valor_a_pagar = (unidades * 13);
        desconto = (valor_a_pagar * 0.08);
        valor_a_pagar = valor_a_pagar - desconto;
        cout << "O valor a pagar é de " << valor_a_pagar << " com um desconto de 8% \n";
    }
}
