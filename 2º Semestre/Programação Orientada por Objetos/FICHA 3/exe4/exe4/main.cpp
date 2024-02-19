//
//  main.cpp
//  exe4
//
//  Created by Miguel Angel Correia Penaranda on 27/03/2023.
//

#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

int main() {
    char password[20] = "macaco", value[20];
    
    do {
        cout << "Introduza uma senha: ";
        fgets(value, 20, stdin);
        value[strcspn(value, "\n")] = '\0';
        
        if (strcmp(password, value) != 0) {
            cout << "PISTA: a senha tem " << strlen(password) << " letras e a primeira letra é m \n";
        }
        else {
            cout << "Felicitações!, Acertaste :) \n";
        }
    } while (strcmp(password, value) != 0);
}

