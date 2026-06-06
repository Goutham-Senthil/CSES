import sys
input = sys.stdin.readline

def run_tets():
    k = int(input())
    
    for n in range(1,k+1):
        ways =  ((n*n*((n*n-1)))//2) - 4*(n-1)*(n-2)
        print(ways)


def main():
    

    # number of test cases
    run_tets()

if __name__ == "__main__":
    main()