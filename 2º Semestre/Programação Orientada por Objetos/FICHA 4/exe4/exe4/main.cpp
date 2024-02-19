//
//  main.cpp
//  exe4
//
//  Created by Miguel Angel Correia Penaranda on 26/04/2023.
//

#include <iostream>
using namespace std;

float diametro, raio;
#define PI 3.14
#define quadrado(r) ((r)*(r))

void datos(){
    cout << "Insira o comprimento da circunferencia: ";
    cin >> diametro;
};


float cal_raio() {
    raio = diametro/2;
    return raio;
}

float cal_area() {
    float area;
    
    area = PI * quadrado(raio);
    
    return area;
}

int main() {
    datos();
    cout << "Diametro de " << diametro << "\nraio igual a " << cal_raio() << "\narea igual a " << cal_area() << "\n";
}





