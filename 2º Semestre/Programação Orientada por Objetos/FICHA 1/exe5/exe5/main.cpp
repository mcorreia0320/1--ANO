//
//  main.cpp
//  exe5
//
//  Created by Miguel Angel Correia Penaranda on 13/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    int a, b;
    
    cout << "Insira o valor de a: ";
    cin >> a;
    
    cout << "Insira o valor de b: ";
    cin >> b;
    
    (a < b)?
        cout << b << " é maior que " << a << "\n":
        cout << a << " é maior que " << b << "\n";
}
