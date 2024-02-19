//
//  main.cpp
//  exe4
//
//  Created by Miguel Angel Correia Penaranda on 15/05/2023.
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
using namespace std;

class aluno {
private:
    float nota_1_teste, nota_2_teste;
public:
    char nome_do_aluno[40];
    int numero_do_aluno;
    float nota_final(){
        float result;
        result = (nota_1_teste + nota_2_teste) / 2;
        return result;
    }
    void set_nota_1(float i){
        nota_1_teste = i;
    }
    void set_nota_2(float i){
        nota_2_teste = i;
    }
    float get_nota_1(){
        return nota_1_teste;
    }
    float get_nota_2(){
        return nota_2_teste;
    }
    void mostraNotas();
} a1;

void soli_datos() {
    float nota1, nota2;
    cout << "Insira o nome o seu nome: ";
    fgets(a1.nome_do_aluno, 40, stdin);
    a1.nome_do_aluno[strcspn(a1.nome_do_aluno,"\n")] = '\0';
    cout << "Insira o seu numero: ";
    cin >> a1.numero_do_aluno;
    cout << "Insira a nota do primeiro teste: ";
    cin >> nota1;
    a1.set_nota_1(nota1);
    cout << "Insira a nota do segundo teste: ";
    cin >> nota2;
    a1.set_nota_2(nota2);
}

void aluno::mostraNotas(){
    cout << "Nome do aluno: " << a1.nome_do_aluno << "\t\tNumero do aluno: " << a1.numero_do_aluno << "\n\nPrimeira Nota: " << a1.get_nota_1() << "\t\t\tSegunda Nota: " << a1.get_nota_2() << "\n\nNota final: " << a1.nota_final() << "\n\n";
};

int main(){
    soli_datos();
    system("clear");
    a1.mostraNotas();
}
