//
//  main.cpp
//  exe5
//
//  Created by Miguel Angel Correia Penaranda on 27/03/2023.
//

#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
    char word1[20],word2[20];
    
    cout << "Introduza a primera palavra: ";
    fgets(word1, 20, stdin);
    word1[strcspn(word1, "\n")] = '\0';
    cout << "Introduza a segunda palavra: ";
    fgets(word2, 20, stdin);
    word2[strcspn(word2, "\n")] = '\0';
    
    if (strcmp(word1, word2) == 0) {
        cout << "As duas palavras são iguais \n";
    }
    else {
        if (strlen(word1) < strlen(word2)) {
            cout << "A segunda palavra é maior que a primeira \n";
        }
        else if (strlen(word1) == strlen(word2)) {
            cout << "São palavras distintas, mas com o mesmo comprimento \n";
        }
        else {
            cout << "A primeira palavra é maior que a segunda \n";
        }
    }
}
