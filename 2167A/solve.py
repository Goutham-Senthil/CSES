import sys
input = sys.stdin.readline

# Link (https://codeforces.com/problemset/problem/2167/A)

def run_tests():
    a,b,c,d = map(int,input().split())

    if a == b == c == d:
        print("YES")
    else:
        print("NO")

def main():
    
    # number of test cases
    t = int(input())
    for _ in range(t):
        run_tests()

if __name__ == "__main__":
    main()