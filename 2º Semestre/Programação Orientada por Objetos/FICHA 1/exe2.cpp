#include <iostream>
#include <math.h>

using namespace std;
int main()
{
    int cateto1, cateto2, hipotenusa;

    cout << "Introduza o primero cateto";
    cin >> cateto1;

    cout << "Introduza o segundo cateto";
    cin >> cateto2;

    hipotenusa = sqrt((cateto1 * cateto1) + (cateto2 * cateto2));

    cout << "O resultado é" << hipotenusa;

    return 0;
}
