import sys
input = sys.stdin.readline

def run_tets():
    y,x = map(int,input().split())

    if y == x:
        val = (y*y) - (y-1)
    
    # no of rows
    elif y > x:
        if y%2==0:
            val = (y*y) - (y-1) + (y-x)
        
        else:
            val = (y*y) - (y-1) - (y-x)
    
    else:
        x,y = y,x
        if y%2!=0:
            val = (y*y) - (y-1) + (y-x)
        
        else:
            val = (y*y) - (y-1) - (y-x)
    print(val)

def main():
    

    # number of test cases
    n = int(input())
    for _ in range(n):
        run_tets()

if __name__ == "__main__":
    main()