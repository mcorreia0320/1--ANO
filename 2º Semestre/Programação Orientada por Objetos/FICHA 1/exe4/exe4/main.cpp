//
//  main.cpp
//  exe4
//
//  Created by Miguel Angel Correia Penaranda on 13/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    float nota1, nota2, nota_final;
    
    cout << "Insira a primeira nota \n";
    cin >> nota1;
    
    cout << "Insira a segunda nota \n";
    cin >> nota2;
    
    nota_final = (nota1 + nota2) / 2;
    
    /* if (nota_final > 9.5) {
        cout << "Aprovado. Com media de: " << nota_final << "\n";
    }
    else
        cout << "Reprovado. Com media de: " << nota_final << "\n";
     */
     (nota_final >= 9.5)?
        cout << "Aprovado. Com media de: " << nota_final << "\n":
        cout << "Reprovado. Com media de: " << nota_final << "\n";
}
