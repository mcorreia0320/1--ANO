//
//  main.cpp
//  EXERCICIO EURO_MILHAO
//
//  Created by Miguel Angel Correia Penaranda on 29/03/2023.
//

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <ctime>

using namespace std;

int main(){
    int win[5] = {}, i, tentativa[5] = {}, value;
    
    srand((unsigned) time(NULL));
    
    for (i= 0; i < 5; i++) {
        win[i] = rand() % 10;
    }
    cout << "       EURO MILHÃO \n";
    cout << " \n";
    for (i= 0; i < 4; i++) {
        
        if (i == 0) {
            cout << "Insira o primeiro numero: ";
            cin >> value;
            tentativa[i] = value;
        }
        else if (i == 1) {
            cout << "Insira o segundo numero: ";
            cin >> value;
            tentativa[i] = value;
        }
        else if (i == 2) {
            cout << "Insira o terceiro numero: ";
            cin >> value;
            tentativa[i] = value;
        }
        else if (i == 3) {
            cout << "Insira o quarto numero: ";
            cin >> value;
            tentativa[i] = value;
        }
    }

    cout << "Insira o valor da estrela: ";
    cin >> value;
    tentativa[4] = value;
    
    if ((win[0] == tentativa[0]) && (win[1] == tentativa[1]) && (win[2] == tentativa[2]) && (win[3] == tentativa[3]) && (win[4] == tentativa[4]))  {
        cout << "GANHASTE!!! 1.000.000 € \n";
    }
    else if (win[4] == tentativa[4]) {
        cout << "Prémio 10€ \n";
    }
    else if ((win[0] == tentativa[0]) && (win[1] == tentativa[1]) && (win[2] == tentativa[2]) && (win[3] == tentativa[3])) {
        cout << "Prémio 20€ \n";
    }
    else {
        cout << "Tente para a proxima \n";
    }
}


