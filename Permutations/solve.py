import sys
input = sys.stdin.readline

def run_tets():
    n = int(input())
    res = []
    for i in range(2,n+1,2):
        res.append(i)
    for i in range(1,n+1,2):
        res.append(i)
    for i in range(1,len(res)):
        if abs(res[i]-res[i-1]) == 1:
            print("NO SOLUTION")
            return
    for n in res:
        print(n,end=' ')
def main():
    

    # number of test cases
    run_tets()

if __name__ == "__main__":
    main()