def run_tets():
    # code to print all numbers from 1 to n
    n = int(input())
    a = list(map(int, input().split()))
    
    b = [False,False]
    
    for x in a:
        b[x&1] = True

    if b[0] and b[1]:
        print(*sorted(a))
    else:
        print(*a)

def main():
    import sys
    input = sys.stdin.readline

    # number of test cases
    n = int(input())
    for _ in range(n):
        run_tets()

if __name__ == "__main__":
    main()