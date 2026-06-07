import sys
input = sys.stdin.readline

def run_tets():
    n = int(input())
    nums = list(map(int,input().split()))

    # Set doesn't work here because
    # there is a test case that is "anti-hashing"
    # from "https://codeforces.com/blog/entry/122914"

    nums.sort()
    count = 1
    i = 0
    for i in range(1,n):
        if nums[i] == nums[i-1]:
            continue
        count+=1
    print(count)



def main():
    

    # number of test cases
    run_tets()

if __name__ == "__main__":
    main()