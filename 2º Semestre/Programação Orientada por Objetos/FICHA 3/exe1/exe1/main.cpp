//
//  main.cpp
//  exe1
//
//  Created by Miguel Angel Correia Penaranda on 27/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    int array[5] = {}, i;
    
    cout << "Vetor com 5 elementos \n";
    
    for (i = 0; i < 5; i++) {
        cout << "Indique o valor para o vector v[" << i << "]: ";
        cin >> array[i];
    }
    for (i = 4; i >= 0; i--) {
        cout << "[" << i << "]=" << array[i] << "\n";
    }
}
