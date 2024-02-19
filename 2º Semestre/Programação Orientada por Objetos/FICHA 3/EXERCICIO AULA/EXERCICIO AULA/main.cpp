//
//  main.cpp
//  EXERCICIO AULA
//
//  Created by Miguel Angel Correia Penaranda on 27/03/2023.
//

#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
    char nome[6];
    cout << "Escreva o seu nome: ";
    fgets(nome,10,stdin);
    nome[strcspn(nome, "\n")] = '\0';
    cout << "Ola, " << nome << ", bem vindo! \n";
}
