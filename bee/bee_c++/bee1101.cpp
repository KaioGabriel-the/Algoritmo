#include <iostream>
using namespace std;

int main() {
    int a,b,soma,x,i;
    
    while (true){
        cin >> a >> b;
        
        if(a <= 0 || b <= 0){
            break;
        }else{
            if (a > b){
                i = b;
                x = a;
            }else{
                i = a;
                x = b;
            }
            soma = 0;
            for(i ; i <= x ; i++){
                soma += i;
                cout << i << " ";
            }
        cout << "Sum=" << soma << endl;
        }
    }
    return 0;
}