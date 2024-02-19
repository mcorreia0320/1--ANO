//
//  main.cpp
//  exe14
//
//  Created by Miguel Angel Correia Penaranda on 22/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    int value, i;
    
    cout << "Introduza um valor: ";
    cin >> value;
    
    for (i = 0; i < value; i++) {
        if (i % 2 == 0) {
            cout << i << "\n";
        }
    }
    
}
