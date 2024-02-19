//
//  main.cpp
//  exe1
//
//  Created by Miguel Angel Correia Penaranda on 24/04/2023.
//

#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

char word[15];

void sol_datos() {
    cout << "Introduza uma palavra: ";
    fgets(word, 15, stdin);
    word[strcspn(word, "\n")] = '\0';
};

int main() {
    sol_datos();
    
    if (strlen(word) <= 4 ) {
        cout << "Palavra pequena! com um tamanho de " << strlen(word) << " letras \n";
    }
    else if (strlen(word) <= 8  ) {
        cout << "Palavra de tamanho medio! com " << strlen(word) << " letras \n";
    }
    else {
        cout << "Palavra grande! com um tamanho de " << strlen(word) << " letras \n";
    }
}


