//
//  main.cpp
//  exe2
//
//  Created by Miguel Angel Correia Penaranda on 22/03/2023.
//

#include <iostream>

using namespace std;

int main(){
    int value1, value2, value3, maior;
    
    cout << "Introduza um valor: ";
    cin >> value1;
    
    cout << "Introduza outro valor: ";
    cin >> value2;
    
    cout << "Introduza o terceiro valor: ";
    cin >> value3;
    
    if ((value1 > value2) && (value1 > value3)) {
        maior = value1;
    }
    else if ((value2 > value1) && (value2 > value3)) {
        maior = value2;
    }
    else {
        maior = value3;
    }
    
    cout << "O maior é o numero " << maior << "\n";
}
