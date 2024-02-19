//
//  main.cpp
//  exe4
//
//  Created by Miguel Angel Correia Penaranda on 22/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    int value;
    
    cout << "Introduza um valor entre 0 e 3: ";
    cin >> value;
    
    switch (value) {
        case 0:
            cout << "ZERO \n";
            break;
        case 1:
            cout << "ONE \n";
            break;
        case 2:
            cout << "TWO \n";
            break;
        case 3:
            cout << "THREE \n";
            break;
            
        default:
            cout << "Valor Não Aceite \n";
            break;
    }
}
