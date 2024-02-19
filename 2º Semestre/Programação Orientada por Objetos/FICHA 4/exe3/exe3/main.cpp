//
//  main.cpp
//  exe3
//
//  Created by Miguel Angel Correia Penaranda on 26/04/2023.
//

#include <iostream>
using namespace std;


float nota1, nota2;

void inserir_dados() {
    cout << "Introduza o valor da primeira nota: ";
    cin >> nota1;
    cout << "Introduza o valor da segunda nota: ";
    cin >> nota2;
}
float calcular_media() {
    float media;
    media= (nota1 + nota2) / 2;
    return media;
}

float maior() { return nota1 > nota2 ? nota1:nota2; }

int main() {
    inserir_dados();
    cout << "A media das notas é " << calcular_media() << " e a nota maior foi " << maior() << "\n";
}


