import sys
input = sys.stdin.readline
 
def run_tets():
    n = int(input())
 
    count = 0
    k = 1
    while 5**k <= n:
        count += n//(5**k)
        k+=1
    print(count)

def main():
    
 
    # number of test cases
 
    run_tets()
 
if __name__ == "__main__":
    main()