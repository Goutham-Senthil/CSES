import sys
input = sys.stdin.readline

def run_tets():
    n = int(input())
    nums = map(int,input().split())

    currSum = 0
    maxSum = float('-inf')

    for n in nums:
        currSum +=n
        maxSum = max(maxSum,currSum)
        if currSum < 0:
            currSum = 0

    print(maxSum)


def main():
    

    # number of test cases
    run_tets()

if __name__ == "__main__":
    main()