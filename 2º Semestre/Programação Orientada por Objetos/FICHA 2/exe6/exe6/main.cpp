//
//  main.cpp
//  exe6
//
//  Created by Miguel Angel Correia Penaranda on 22/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    int op = 1;
    
    while ((op >= 1) && (op <= 3)) {
        cout<<"\nMENU DE COMANDOS"<<"\n\n";
        cout<<" 0.Sair \n";
        cout<<" 1. Mostrar\n";
        cout<<" 2. Apresentar\n\n";
        cout<<" Escolha uma opcao: ";
        cin>>op;
    }
}
