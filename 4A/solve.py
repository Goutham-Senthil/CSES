import sys
input = sys.stdin.readline

def run_tets():
    n = int(input())
    if n%2 == 0 and n>2:
        print('YES')
    else:
        print('NO')


def main():
    

    # number of test cases
    run_tets()

if __name__ == "__main__":
    main()