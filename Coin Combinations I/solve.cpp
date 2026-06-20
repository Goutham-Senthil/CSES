#include<iostream>
#include<map>
#include<vector>
#include <sstream>
using namespace std;

void run_tests()
{
    int n,x;
    cin>>n>>x;
    int mod_val = 1e9 + 7;
    vector<int> coins(n);
    for (int &x : coins) cin>>x;

    vector<int> dp(x+1,0);
    dp[0] = 1;

    for (int i = 1; i <= x; ++i)
    {
        for (int j = 0; j<n; ++j)
        {
            if (i-coins[j]>=0)
            {
                dp[i] = dp[i] + dp[i-coins[j]];
                dp[i] = dp[i] % mod_val;
            }
        }
    }

    cout<<dp[x];

    return ;
}

int main(){

    run_tests();
}