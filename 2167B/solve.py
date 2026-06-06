def run_tets():
    n = int(input())
    text = input()

    s,t  = text.split()
    print("YES") if sorted(s) == sorted(t) else print("NO")



def main():
    import sys
    input = sys.stdin.readline

    # number of test cases
    n = int(input())
    for _ in range(n):
        run_tets()

if __name__ == "__main__":
    main()