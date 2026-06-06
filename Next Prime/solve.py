#### Solution 3 => 4 largest gap is 540
def solve():
    import sys
    input = sys.stdin.readline
    
    # ===== WRITE YOUR SOLUTION HERE =====
    n = int(input())
    primes_list = []
 
    def is_prime(num):
        if num%2==0:
            return False
        for i in range(3,int(num**0.5) + 1,2):
            if num%i==0:
                return False
        return True
 
 
    for _ in range(n):
        primes_list.append(int(input()))
        
    for num in primes_list:
        if num == 1 or num == 2:
            print(num+1)
            continue
        candidate = num+1
        for candidate in range(num+1,num+541):
            if is_prime(candidate):
                print(candidate)
                break
    # ===================================
 
 
if __name__ == "__main__":
    solve()