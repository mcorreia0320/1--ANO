//
//  main.cpp
//  exe7
//
//  Created by Miguel Angel Correia Penaranda on 15/03/2023.
//

#include <iostream>

using namespace std;

int main () {
    int opcao;
    
    cout << "          Menu de Opções \n";
    cout << "\n";
    cout << "1. Executar o programa Calculadora \n";
    cout << "2. Converter graus centígrados/farenheit \n";
    cout << "3. Converter metros/quilometros \n";
    cout << "4. Sair \n";
    cout << "\n";
    cout << "-> Escolha uma opção: ";
    cin >> opcao;
    cout << "\n";
    
    switch (opcao) {
        case 1:
            cout << "Calculadora: a executar... \n";
            cout << "\n";
            break;
        case 2:
            cout << "Conversão de temperaturas \n";
            cout << "\n";
            break;
        case 3:
            cout << "Conversão de distâncias \n";
            cout << "\n";
            break;
        case 4:
            cout << "A terminar o programa... \n";
            cout << "\n";
            break;
            
        default:
            cout << "Opção não valida \n";
            cout << "\n";
            break;
    }
    
}
