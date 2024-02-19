//
//  main.cpp
//  exe5
//
//  Created by Miguel Angel Correia Penaranda on 22/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    int value, i, j;
    
    cout << "Introduza um valor: ";
    cin >> value;
    cout << "\n";
    cout << "Decrescente: \n";
    for (i = value; i >= 0; i--) {
        cout << i << "\n";
    }
    cout << "Crescente: \n";
    for (j = 0; j <= value; j++) {
        cout << j << "\n";
    }
}
