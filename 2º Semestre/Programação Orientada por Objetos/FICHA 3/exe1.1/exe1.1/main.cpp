//
//  main.cpp
//  exe1.1
//
//  Created by Miguel Angel Correia Penaranda on 27/03/2023.
//

#include <iostream>

using namespace std;

int main() {
    int array[2][2] = {}, i, j;
    
    cout << "Introduza os vetores de um array com dois vetores \n";
    
    for (i= 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            cout << "Introduza o valor do vetor[" << i << "][" << j << "]: ";
            cin >> array[i][j];
        }
    }
    
    for (i= 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            cout << "array[" << i << "][" << j << "]= " << array[i][j] << "\n";
        }
    }
}
