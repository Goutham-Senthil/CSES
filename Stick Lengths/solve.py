import sys
input = sys.stdin.readline

def run_tests():
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    median = nums[len(nums)//2]

    total = 0

    for x in nums:
        total += abs(x - median)

    print(total)


def main():
    
    # number of test cases
    run_tests()

if __name__ == "__main__":
    main()