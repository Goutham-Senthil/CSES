import sys
input = sys.stdin.readline


def graycode(n):

    if n == 1:
        return ['0','1']

    # get the prevoious one
    prevGreyCode = graycode(n-1)
    reversedPrevGreyCode = prevGreyCode[::-1]

    prevLen = len(prevGreyCode)
    index = 0 

    newGrey = []
    while index < prevLen:

        addZero = '0' + prevGreyCode[index]
        newGrey.append(addZero)

        prevGreyCode[index] = '1' + reversedPrevGreyCode[index]
        prevGreyCode.append(addZero)

        index += 1
    return prevGreyCode


def run_tests():
    # recursive solution tbh

    n = int(input())

    res = graycode(n)

    for code in res:
        print(code)

    return

def main():
    
    # number of test cases
    
    run_tests()

if __name__ == "__main__":
    main()