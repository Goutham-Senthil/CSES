import sys
input = sys.stdin.readline

def run_tets():
    s = input().strip()
    l = 0
    mx = 0

    for r in range(1,len(s)):
        if s[r]!=s[l]:
            mx = max(mx,r-l)
            l = r
    mx = max(mx,len(s)-l)
    print(mx)


def main():
    

    # number of test cases

    run_tets()

if __name__ == "__main__":
    main()