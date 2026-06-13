#include<iostream>
#include<map>
using namespace std;

// Link (https://codeforces.com/problemset/problem/2167/A)

void run_tests()
{
    int a,b,c,d;
    cin>>a>>b>>c>>d;

    if (a==b && b==c && c==d)
    {
        cout<<"YES\n";
    }
    else
    {
        cout<<"NO\n";
    }
}

int main(){
    int t;
    cin>>t;
    for(int i = 1; i <=t; ++i)
    {
        run_tests();
    }
}