//
//  main.cpp
//  exe2
//
//  Created by Miguel Angel Correia Penaranda on 03/05/2023.
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
using namespace std;

class aluno {
public:
    char nome_do_aluno[40];
    int numero_do_aluno;
    float nota_1_teste, nota_2_teste;
    float nota_final(){
        float result;
        result = (nota_1_teste + nota_2_teste) / 2;
        return result;
    }
} a1;

void soli_datos() {
    cout << "Insira o nome o seu nome: ";
    fgets(a1.nome_do_aluno, 40, stdin);
    a1.nome_do_aluno[strcspn(a1.nome_do_aluno,"\n")] = '\0';
    cout << "Insira o seu numero: ";
    cin >> a1.numero_do_aluno;
    cout << "Insira a nota do primeiro teste: ";
    cin >> a1.nota_1_teste;
    cout << "Insira a nota do segundo teste: ";
    cin >> a1.nota_2_teste;
}

int main(){
    soli_datos();
    system("clear");
    cout << "\t \t\tNota do primeiro periodo de BP.\t \t \n\nNome do aluno: " << a1.nome_do_aluno << "\t   " << "Numero do aluno: " << a1.numero_do_aluno << "\n \n" << "Nota final de BP: " << a1.nota_final() << "\n\n";
}
