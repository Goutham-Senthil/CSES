import sys
input = sys.stdin.readline

def run_tests():
    x,y = map(int,input().split())

    if x > y:
        x ,y = y ,x

    if (x+y) % 3 != 0 or (y > 2*x):
        print('NO')
    else:
        print('YES')


def main():
    
    # number of test cases
    t = int(input())
    for _ in range(t):
        run_tests()

if __name__ == "__main__":
    main()