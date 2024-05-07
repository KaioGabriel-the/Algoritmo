#include <iostream>
using namespace std;

int main() {
    int a,i;
    cin >> a;
    for(i = 0 ; i <6;){
        if (a%2 == 0){
            i+=0;
        }else{
            cout << a << endl;
            i++;
        }
        a +=1;
    }
    return 0;
}