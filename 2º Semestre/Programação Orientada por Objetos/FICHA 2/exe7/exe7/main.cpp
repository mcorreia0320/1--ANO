//
//  main.cpp
//  exe7
//
//  Created by Miguel Angel Correia Penaranda on 22/03/2023.
//

#include <iostream>

using namespace std;

int main(){
    int maior,menor,value1,value2,i;
    
    cout << "Introduza um valor: ";
    cin >> value1;
    
    cout << "Introduza outro valor: ";
    cin >> value2;
    
    if (value1 > value2) {
        maior = value1;
        menor = value2;
    }
    else {
        maior = value2;
        menor = value1;
    }
    
    for (i= menor + 1; i < maior; i++) {
        cout << i << "\n";
    }
}
