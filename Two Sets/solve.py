import sys
input = sys.stdin.readline

def run_tets():
    n = int(input())

    summ = n*(n+1)//2

    if summ%2 != 0:
        print('NO')
    else:
        # if n is odd its fine 
        # if n is even make the target sum = n+1
        print("YES")
        A = []
        B = []
        if n%2!=0:
            B.append(n)
        else:
            n+=1
        alternate = True

        for i in range(1,n//2 + 1):
            if alternate:
                A.append(i)
                A.append(n-i)
                alternate = False
            else:
                B.append(i)
                B.append(n-i)
                alternate = True
        # print(sorted(A))
        print(len(A))
        for n in (A):
            print(n,end=' ')
        print('\n' + str(len(B)))
        for n in (B):
            print(n,end=' ')
        
        # print(sorted(B))
        # print(sum(A) == sum(B))


def main():

    # number of test cases
    
    run_tets()

if __name__ == "__main__":
    main()