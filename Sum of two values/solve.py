import sys
input = sys.stdin.readline

def run_tets():
    n,target = map(int,input().split())
    nums = list(map(int,input().split()))

    vec = [[nums[i],i+1] for i in range(n)]

    vec.sort()
    l = 0
    r = n - 1
    while l < r:
        value = vec[l][0] + vec[r][0]
        if value == target:
            print(vec[l][1],vec[r][1])
            return
        elif value > target:
            r -= 1
        else:
            l +=1
    print('IMPOSSIBLE')
        

def main():
    
    # number of test cases
    run_tets()

if __name__ == "__main__":
    main()