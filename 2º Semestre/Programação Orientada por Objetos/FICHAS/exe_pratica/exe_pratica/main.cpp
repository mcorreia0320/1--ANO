//
//  main.cpp
//  exe_pratica
//
//  Created by Miguel Angel Correia Penaranda on 21/05/2023.
//

#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main(){
    int v[3]= {13,31,45};
    int *p = v;
    cout << *p << "\n";
    cout << *(p+1) << "\n";
    cout << *p << "\n";
    cout << *p++ << "\n";
    cout << *p << "\n";
    
}
