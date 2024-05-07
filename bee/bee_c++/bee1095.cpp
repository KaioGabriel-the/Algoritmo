#include <iostream>
using namespace std;

int main() {
    int j = 60;
    int I =  1;
    while (j >= 0){
        cout << "I="<< I <<" J="<< j<< endl;
        j -= 5;
        I+=3;
    }
    return 0;
}