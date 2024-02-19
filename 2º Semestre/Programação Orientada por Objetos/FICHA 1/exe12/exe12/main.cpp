//
//  main.cpp
//  exe12
//
//  Created by Miguel Angel Correia Penaranda on 20/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    
    int value1, value2, result = 500;
    
    do {
        cout << "Digite um numero inteiro: ";
        cin >> value1;
        cout << "\n";
        cout << "Digite outro numero inteiro: ";
        cin >> value2;
        cout << "\n";
        result = value1 * value2;
        cout << value1 << " * " << value2 << " = " << result << "\n";
        cout << "\n";
    } while ((result > 10) && (result < 1000));
}
