//
//  main.cpp
//  exe3
//
//  Created by Miguel Angel Correia Penaranda on 22/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    char value;
    
    cout << "Digite uma letra: ";
    cin >> value;
    
    if ((value >= 'A') && (value <= 'Z')) {
        cout << "Letra Maiuscula. \n";
    }
    else if ((value >= 'a') && (value <= 'z')) {
        cout << "Letra Minuscula. \n";
    }
    else {
        cout << "O valor não é uma letra \n";
    }
}
