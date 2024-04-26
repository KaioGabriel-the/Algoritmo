#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    float x,y,m,d;
    
    cin >> x >> y;
    m = (x*3.5)+(y*7.5);
    d = m/11;
    cout << fixed << setprecision(5);
    cout << "MEDIA = " << d << endl;
    return 0;
}