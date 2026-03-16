#include <iostream>
using namespace std;

long long climbStairs(int n) {
    if (n <= 0) return 0;
    if (n <= 1) return 1;
    if (n <= 2) return 2;
    
    long long a = 1, b = 2, c;
    for (int i = 3; i <= n; ++i){
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int main (){
    int n;
    cout << "Enter number of stairs: ";
    cin >> n;
    
    cout << "Number of distinct ways: " << climbStairs(n) << endl;
    return 0;
}