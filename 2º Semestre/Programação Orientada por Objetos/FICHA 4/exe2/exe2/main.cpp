//
//  main.cpp
//  exe2
//
//  Created by Miguel Angel Correia Penaranda on 24/04/2023.
//

#include <iostream>

using namespace std;


int cal_area(int lado);

int main(){
    int l;
    
    cout << "Introduza o comprimento: ";
    cin >> l;
    
    cout << "A area do quadrado é " << cal_area(l) << "\n";
}

int cal_area(int lado) {
    int area;
    
    area = lado * lado;
    
    return area;
}
