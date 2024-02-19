//
//  main.cpp
//  exe13
//
//  Created by Miguel Angel Correia Penaranda on 22/03/2023.
//

#include <iostream>

using namespace std;

int main(){
    int value, somatorio = 0, times = 0;
    do {
        cout << "Introduza um valor inferior a 100: ";
        cin >> value;
        cout << "\n";
        if (value > 100) {
            cout << "Valor Invalido \n";
            cout << "\n";
        }
        else {
            somatorio += value;
            times += 1;
        }
    } while (somatorio < 500);
    
    cout << "A media dos valores introduzidos é " << somatorio / times << "\n";
}
