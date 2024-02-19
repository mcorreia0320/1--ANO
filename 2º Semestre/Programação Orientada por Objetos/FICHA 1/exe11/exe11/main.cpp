//
//  main.cpp
//  exe11
//
//  Created by Miguel Angel Correia Penaranda on 20/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    
    int indice, soma;
    soma = 0;
    do {
        cout << "Introduza um valor entre 1 e 15: ";
        cin >> indice;
    } while (indice < 1 || indice > 15);
        while (indice <= 15) {
            soma += indice;
            cout << "n= " << indice << "\n";
            indice += 1;
        }
    cout << "O somatorio dos numeros é " << soma << "\n";
    
    
    
}
