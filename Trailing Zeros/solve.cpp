#include<iostream>
#include<vector>
using namespace std;

int main(){

    int n = 0;
    cin >> n;
    int ans = 0;
    for (int k=5; k<=n;k*=5)
    {
        ans += n/k;
    }
    cout<< ans;
    return 0;
}