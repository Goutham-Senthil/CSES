import sys
input = sys.stdin.readline

def run_tets():
    n = int(input())
    nums = list(map(int,input().split()))

    nums.sort()
    count = 0
    i = 0
    while i < n:
        while nums[i] == nums[i-1] and i+1 < n:
            i+=1
        count+=1
        i+=1
    print(count)



def main():
    

    # number of test cases
    run_tets()

if __name__ == "__main__":
    main()