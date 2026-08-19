import sys
input = sys.stdin.readline

stack = []

def hanoi(n, start, end):
    if n == 1:
        stack.append([start,end])
        return 

    other = 6 - (start + end)
    hanoi(n-1, start , other)
    stack.append([start,end])
    hanoi(n-1, other, end)




def run_tests():
    n = int(input())

    hanoi(n, 1, 3)
    print(f"{len(stack)}\n")

    for src,dst in stack:
        print(f"{src} {dst}\n")


def main():
    
    # number of test cases
    
    run_tests()

if __name__ == "__main__":
    main()