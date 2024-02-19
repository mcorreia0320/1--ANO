//
//  main.cpp
//  prueba
//
//  Created by Miguel Angel Correia Penaranda on 14/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    int nota;
    
    cout << "Introduza uma nota: ";
    cin >> nota;
    
    if (nota < 9.5) {
        cout << "Insificiente \n";
    }
    else if (nota < 13) {
        cout << "Suficiente \n";
    }
    else if (nota < 17) {
        cout << "Bom \n";
    }
    else if (nota < 20) {
        cout << "Muito Bom \n";
    }
}


