//
//  main.cpp
//  exe1
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
    float nota_esperada;
} a1;

void soli_datos() {
    cout << "Insira o nome o seu nome: ";
    fgets(a1.nome_do_aluno, 40, stdin);
    a1.nome_do_aluno[strcspn(a1.nome_do_aluno,"\n")] = '\0';
    cout << "Insira o seu numero: ";
    cin >> a1.numero_do_aluno;
    cout << "Insira a nota esperada: ";
    cin >> a1.nota_esperada;
}

int main(){
    soli_datos();
    system("clear");
    cout << "\t \t\tPrognosticos de BP.\t \t \n\nNome do aluno: " << a1.nome_do_aluno << "\t   " << "Numero do aluno: " << a1.numero_do_aluno << "\n \n" << "Nota esperada na disciplina de BP: " << a1.nota_esperada << "\n\n";
}
