#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

int main(){
    
    float x1,y1,x2,y2,somaxy,raiz;
    
    cin >> x1 >> y1;
    cin >> x2 >> y2;
    
    somaxy = pow((x2 - x1),2) + pow((y2 - y1),2);
    raiz = sqrt(somaxy);
    
    cout << fixed << setprecision(4);
    cout << raiz << endl;
    return 0;
}