import sys
from collections import Counter
import string
input = sys.stdin.readline


def run_tests():
    s = input()

    one = False
    s_count = Counter(s)
    the_one = ''

    arr = []
    

    for c in string.ascii_uppercase:
        if s_count[c] % 2 and not one:
            one = True
            the_one = c
        elif s_count[c] % 2 and one:
            print('NO SOLUTION')
            return

        arr.append(c*(s_count[c]//2))

    sting = ''.join(arr) + the_one + ''.join(reversed(arr))

    print(sting)
    return 


def main():
    
    # number of test cases
    run_tests()

if __name__ == "__main__":
    main()