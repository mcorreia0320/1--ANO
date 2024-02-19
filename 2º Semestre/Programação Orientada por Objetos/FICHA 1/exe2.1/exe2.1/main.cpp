#include <iostream>
#include <math.h>

using namespace std;
int main()
{
    int cateto1, cateto2, hipotenusa;

    cout << "Introduza o primero cateto \n";
    cin >> cateto1;

    cout <<"Introduza o segundo cateto \n";
    cin >> cateto2;

    hipotenusa = sqrt((cateto1 * cateto1) + (cateto2 * cateto2));

    cout << "O resultado é " << hipotenusa << " \n";

    return 0;
}
