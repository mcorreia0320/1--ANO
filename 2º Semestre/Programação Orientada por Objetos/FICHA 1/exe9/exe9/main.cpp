//
//  main.cpp
//  exe9
//
//  Created by Miguel Angel Correia Penaranda on 15/03/2023.
//

#include <iostream>

using namespace std;

int main () {
    int opçao;
    
    cout << "       Menu de Descontos \n";
    cout << "\n";
    cout << "1. Cereais Nestum \n";
    cout << "2. Sumo Tropical \n";
    cout << "3. Geleia Morango \n";
    cout << "4. Massa Italiana \n";
    cout << "5. Arroz Amarelo \n";
    cout << "6. Leite de Soja \n";
    cout << "7. Coca Cola Zero \n";
    cout << "8. Couve de Bruxelas \n";
    cout << "\n";
    cout << "Escolha uma opção: ";
    cin >> opçao;
    cout << "\n";
    
    switch (opçao) {
        case 1:
            cout << "O Cereais Nestum fica com um desconto de 20% \n";
            cout << "\n";
            break;
        case 2:
            cout << "O Sumo Tropical fica com um desconto de 15% \n";
            cout << "\n";
            break;
        case 3:
            cout << "A Geleia Morango fica com um desconto de 20% \n";
            cout << "\n";
            break;
        case 4:
            cout << "A Massa Italiana fica com um desconto de 10% \n";
            cout << "\n";
            break;
        case 5:
            cout << "O Arroz Amarelo fica com um desconto de 10% \n";
            cout << "\n";
            break;
        case 6:
            cout << "A Leite de Soja fica com um desconto de 20% \n";
            cout << "\n";
            break;
        case 7:
            cout << "A Coca Cola Zero fica com um desconto de 15% \n";
            cout << "\n";
            break;
        case 8:
            cout << "A Couve de Bruxelas fica com um desconto de 5% \n";
            cout << "\n";
            break;
        
            
        default:
            cout << "Produto não existente \n";
            cout << "\n";
            break;
    }
}
