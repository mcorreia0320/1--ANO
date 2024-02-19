//
//  main.cpp
//  exe10
//
//  Created by Miguel Angel Correia Penaranda on 20/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    int indice, result;
    
    indice = 1;
    
    while (indice <= 5) {
        result = indice * 2;
        cout << "O dobro de " << indice << " é " << result << "\n";
        indice += 1;
    }

}
