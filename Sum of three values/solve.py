import sys
input = sys.stdin.readline

def run_tets():
    n,target = map(int,input().split())
    nums = list(map(int,input().split()))

    # found out the hard way 
    # you need to preserve the original indices
    
    vec = [[nums[i],i+1] for i in range(n)]

    vec.sort()


    i=0
    for i in range(n-2):
        l , r = i+1 , len(nums)-1


        while l < r:
            threeSum = vec[l][0] + vec[r][0] + vec[i][0]

            if threeSum > target:
                r-=1
            elif threeSum < target:
                l+=1
            else:
                print(vec[l][1],vec[r][1],vec[i][1])
                return 
    print("IMPOSSIBLE")


def main():
    

    # number of test cases
    run_tets()

if __name__ == "__main__":
    main()