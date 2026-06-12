import sys
input = sys.stdin.readline
import math

def run_tests():
    num_machines,products = map(int,input().split())

    times = list(map(int,input().split()))

    l = 1
    r = 10**18
    best = float('inf')

    while l <= r:
        mid = (l+r)//2

        sum_ = 0
        for t in times:
            sum_ += mid//t
        
        if sum_ >= products:
            best = min(best,mid)
            r = mid - 1
        else:
            l = mid + 1
    print(best)

def main():
    
    # number of test cases
    run_tests()

if __name__ == "__main__":
    main()