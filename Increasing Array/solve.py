import sys
input = sys.stdin.readline

def run_tets():
    n = int(input())
    lst = list(map(int, input().split()))


    mx_so_far = lst[0]
    changes = 0
    for num in lst[1:]:
        if num < mx_so_far:
            changes += mx_so_far - num
        mx_so_far = max(mx_so_far,num)
    print(changes)

def main():

    run_tets()

if __name__ == "__main__":
    main()