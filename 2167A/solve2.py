def run_tets():
    
    a,b,c,d = map(int, input().split())

    if a == b == c == d:
        print("YES")
    else:
        print("NO")




def main():
    import sys
    input = sys.stdin.readline

    # number of test cases
    n = int(input())
    for _ in range(n):
        run_tets()

if __name__ == "__main__":
    main()