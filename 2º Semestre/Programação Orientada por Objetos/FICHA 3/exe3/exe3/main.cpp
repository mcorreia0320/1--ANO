//
//  main.cpp
//  exe3
//
//  Created by Miguel Angel Correia Penaranda on 27/03/2023.
//

#include <iostream>
#include <stdio.h>
#include <string.h>


using namespace std;

int main() {
    char frase1[100], frase2[100];
    
    cout << "Introduza uma frase incompleta: ";
    fgets(frase1,100,stdin);
    frase1[strcspn(frase1, "\n")] = '\0';
    cout << "Introduza o restante da frase: ";
    fgets(frase2,100,stdin);
    frase2[strcspn(frase2,"\n")] = '\0';
    strcat(frase1, frase2);
    
    cout << frase1 << "\n";
    
    
    
    
    
    
    
}
