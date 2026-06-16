import sys
input = sys.stdin.readline

def run_tests():
    n = int(input())
    mod = 10**9 + 7
    grid = []
    for i in range(n):  
        curr_grid = list(input())
        grid.append(curr_grid[:n])
    
    dp = [[0]*n for _ in range(n)]
    if grid[0][0] == '*' or grid[n-1][n-1] == '*':
        print(0)
        return 
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            if (i == 0 and j == 0) or grid[i][j] == '*':
                # we also wanna preserve value at dp (0,0)
                # grid[i][j] = 0
                # but it is already intialized so eh
                continue
            valx = 0
            valy = 0
            if i > 0:
                valx = dp[i-1][j]
            if j > 0:
                valy = dp[i][j-1]
            dp[i][j] = (valx + valy) % mod
    print(dp[n-1][n-1])
            

def main():
    
    # number of test cases
    
    run_tests()

if __name__ == "__main__":
    main()