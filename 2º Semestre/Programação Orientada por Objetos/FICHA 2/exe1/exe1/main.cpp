//
//  main.cpp
//  exe1
//
//  Created by Miguel Angel Correia Penaranda on 22/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    int value;
    
    do {
        cout << "Introduza um numero entre 1 e 10: ";
        cin >> value;
        
        if ((value >= 1) && (value <= 10)) {
            cout << "Numero Valido \n";
        }
        else {
            cout << "Numero Invalido \n";
        }
    } while (true);
}
