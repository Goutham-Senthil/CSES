def run_tets():
    n = int(input())
    print(n,end=' ')
    while n!=1:
        if n%2==0:
            n//=2
            print(n,end=' ')
        else:
            n*=3
            n+=1
            print(n,end=' ')


def main():
    import sys
    input = sys.stdin.readline

    # number of test cases

    run_tets()

if __name__ == "__main__":
    main()