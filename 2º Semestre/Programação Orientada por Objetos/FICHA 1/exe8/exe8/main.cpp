//
//  main.cpp
//  exe8
//
//  Created by Miguel Angel Correia Penaranda on 15/03/2023.
//

#include <iostream>

using namespace std;

int main () {
    float numero1, numero2, total;
    char operacao;
    
    cout << "Introduza o primeiro numero: ";
    cin >> numero1;
    
    cout << "Introduza o segundo numero: ";
    cin >> numero2;

    cout << "Introduza a operacao a realizar(+, -, * ou /): ";
    cin >> operacao;
    cout << "\n";
    switch (operacao) {
        case '+' :
            total = numero1 + numero2;
            cout << numero1 << " + " << numero2 << " = " << total << "\n";
            cout << "\n";
            break;
        case '-' :
            total = numero1 - numero2;
            cout << numero1 << " - " << numero2 << " = "  << total << "\n";
            cout << "\n";
            break;
        case '*' :
            total = numero1 * numero2;
            cout << numero1 << " * " << numero2 << " = " << total << "\n";
            cout << "\n";
            break;
        case '/' :
            total = numero1 / numero2;
            cout << numero1 << " / " << numero2 << " = " << total << "\n";
            cout << "\n";
            break;
        default:
            cout << "Opção não Valida \n";
            break;
    }
}
