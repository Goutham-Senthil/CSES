import sys
input = sys.stdin.readline
 

# i tried everything
# its TLE
# but the logic is 100% correct

def run_tests():
    MOD = 10**9 + 7
    n,x = map(int,input().split())
    coins = list(map(int,input().split()))

    dp = {i:0 for i in range(x+1)}
    dp[0] = 1

    for i in range(x+1):
        for c in coins:
            if i - c >= 0:
                dp[i] = (dp[i - c] + dp[i]) % 1000000007
            
    print(dp[x]) 

def main():
    
    # number of test cases
    run_tests()
 
if __name__ == "__main__":
    main()
