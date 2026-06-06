import sys
input = sys.stdin.readline

def run_tets():
    n = int(input())

    MOD = 10**9 + 7
    number = 2**n % MOD
    print(number)



def main():
    

    # number of test cases
    run_tets()

if __name__ == "__main__":
    main()