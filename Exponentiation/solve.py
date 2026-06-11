import sys
input = sys.stdin.readline

mod = 1000000007

# Refer to http://cp-algorithms.com/algebra/binary-exp.html


def run_tests(base,exp):
    mod = 10**9 + 7 
    if exp == 0:
        return 1
    if exp == 1:
        return base%mod
    base %= mod
    result = run_tests(base,exp//2)
    if exp%2 == 1:
        return (((result*result)%mod)*base)%mod
    else:
        return (result*result)%mod
    

def mod_pow(a, b):
    a %= mod
    res = 1

    while b:
        if b & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        b >>= 1

    return res

def main():
    
    # number of test cases
    t = int(input())
    q = []
    for _ in range(t):
        base , exp = map(int,input().split())
        q.append([base,exp]) 
    
    for base,exp in q:
        print(f"{mod_pow(base,exp)}")

if __name__ == "__main__":
    main()