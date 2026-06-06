def solve():
    import sys
    input = sys.stdin.readline
    
    # ===== WRITE YOUR SOLUTION HERE =====
    n = int(input())
    sqaures = []

    for _ in range(n):
        sqaures.append(input().split())
    
    for sq in sqaures:
        if len(sq) != 4:
            print("NO")
        
        elif sq[0] == sq[1] == sq[2] == sq[3]:
            print("YES")
        else:
            print("NO")

    # ===================================

if __name__ == "__main__":
    solve()