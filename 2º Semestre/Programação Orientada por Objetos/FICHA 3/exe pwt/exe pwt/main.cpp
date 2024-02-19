//
//  main.cpp
//  exe pwt
//
//  Created by Miguel Angel Correia Penaranda on 28/03/2023.
//

#include <iostream>
#include <ctime>

using namespace std;

int main() {
    int array[5], i;
    
    srand((unsigned) time(NULL));
    
    for (i = 0; i < 5; i++) {
        array[i] = rand() % 30;
    }
    
    cout << "["<< array[0] << "," << array[1] << "," << array[2] << "," << array[3] << "," << array[4] << "]\n";
    
}
