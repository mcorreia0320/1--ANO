//
//  main.cpp
//  exe5
//
//  Created by Miguel Angel Correia Penaranda on 26/04/2023.
//

#include <iostream>
using namespace std;

int numero1, numero2;

int inteira() {
    int result;
    
    if (numero1 > numero2) {
        result = numero1 / numero2;
    }
    else
        result = numero2 / numero1;
    
    return result;
}

int resto() {
    int result;
    
    if (numero1 > numero2) {
        result = numero1 % numero2;
    }
    else
        result = numero2 % numero1;
    
    return result;
}

int main(){
    cout << "Introduza um numero: ";
    cin >> numero1;
    cout << "Introduza outro numero: ";
    cin >> numero2;
    cout<< "Divisão Inteira: " << inteira() << "\nResto da divisão: " << resto() << "\n";
}


