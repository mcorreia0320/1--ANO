//
//  main.cpp
//  exe2
//
//  Created by Miguel Angel Correia Penaranda on 27/03/2023.
//

#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
    char str1[40] = "Grande clube o Benfica, " , str2[30] = " Mas o Porto é o maior.";
    
    cout << str1 << "\n";
    strcat(str1, str2);
    cout << str1 << "\n";
}
