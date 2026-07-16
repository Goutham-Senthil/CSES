#include<iostream>
#include<map>
#include<vector>
#include <sstream>
using namespace std;

void run_tests()
{
    // I am using C++ 20
    // old solution used int
    // can overflow
    long long x,y;

    cin>>x>>y;
    // lol forgot about this one
    long long res = 0;
    
    if (x == y)
    {
        res = (x*y) - (x-1) ;
        
    }
    else if ( x > y)
    {
        if (x%2 == 0)
        {
            res = (x*x) - (x-1) + (x-y);
        }
        else
        {
            res = (x*x) - (x-1) - (x-y);
        }
    }
    else
    {
        x = x^y;
        y = x^y;
        x = x^y;

        if (x%2 != 0)
        {
            res = (x*x) - (x-1) + (x-y);
        }
        else
        {
            res = (x*x) - (x-1) - (x-y);
        }
    }

    cout<<res<<endl;
    return ;
}

int main(){
    int t;
    cin>>t;
    for(int i = 1; i <=t; ++i)
    {
        run_tests();
    }
}