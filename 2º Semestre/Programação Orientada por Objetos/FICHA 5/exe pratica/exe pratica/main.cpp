//
//  main.cpp
//  exe pratica
//
//  Created by Miguel Angel Correia Penaranda on 08/05/2023.
//
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <string.h>
using namespace std;

class aluno {
public:
    void setEscola(char x[25]) {
        strcpy(escola, x);
    }
    void setNome(char y[20]) {
        strcpy(nome, y);
    }
    void setNotaFinal(int z) {
        notaFinal = z;
    }
    char* getEscola() {
        return escola;
    }
    char* getNome() {
        return nome;
    }
    int getNotaFinal(){
        return notaFinal;
    }
private:
    char escola[25], nome[20];
    int notaFinal;
}a1;

int main(){
    int nota;
    char school[25], nome[20];
    
    cout << "Introduza o nome da escola: ";
    fgets(school, 25, stdin);
    school[strcspn(school,"\n")] = '\0';
    a1.setEscola(school);
    
    cout << "Introduza o nome do aluno: ";
    fgets(nome, 20, stdin);
    nome[strcspn(nome,"\n")] = '\0';
    a1.setNome(nome);
    
    cout << "Introduza a nota final: ";
    cin >> nota;
    a1.setNotaFinal(nota);
    
    system("clear");
    
    cout << "Escola: " << a1.getEscola() << "\nAluno: " << a1.getNome() << "\nNota Final: " << a1.getNotaFinal() << "\n";
}

