import sys
input = sys.stdin.readline
 
def run_tets():
    word1 = input()
    word2 = input()
    m, n = len(word1), len(word2)
    if m < n:
        m, n = n, m
        word1, word2 = word2, word1
 
    dp = [n - i for i in range(n + 1)]
 
    for i in range(m - 1, -1, -1):
        nextDp = dp[n]
        dp[n] = m - i
        for j in range(n - 1, -1, -1):
            temp = dp[j]
            if word1[i] == word2[j]:
                dp[j] = nextDp
            else:
                dp[j] = 1 + min(dp[j], dp[j + 1], nextDp)
            nextDp = temp
    print(dp[0])
 
 
def main():
    
 
    # number of test cases
    run_tets()
 
if __name__ == "__main__":
    main()