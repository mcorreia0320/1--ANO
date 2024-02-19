//
//  main.cpp
//  exe15
//
//  Created by Miguel Angel Correia Penaranda on 20/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    char caracter;
    
    
    cout << "Escreva um caracter: ";
    cin >> caracter;
    
    if ((caracter >= '0') && (caracter <= '9')) {
        cout << "Numero \n";
    }
    
    else if ( ((caracter >= 'A') && (caracter <= 'Z')) || ((caracter >= 'a') && (caracter <= 'z'))) {
        cout << "Letra \n";
    }
    else {
        cout << "Simbolo \n";
    }
    
   
        
    
}
