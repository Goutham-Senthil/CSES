import sys
input = sys.stdin.readline

def run_tests():
    n,target = map(int,input().split())
    coins = list(map(int,input().split()))

    dp = [float('inf')]*(target+1)
    dp[0] = 0
    coins.sort()
    for i in range(1,target+1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i],1+dp[i-coin])
            else:
                break

    print(dp[target] if dp[target] < float('inf') else -1)


def main():
    
    run_tests()

if __name__ == "__main__":
    main()