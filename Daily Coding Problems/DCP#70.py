'''
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
'''
import math
def findNth1(num):
    NthNum = {
        1 : 19,
        2 : 28,
        3 : 37,
        4 : 46,
        5 : 55,
        6 : 64,
        7 : 73,
        8 : 82,
        9 : 91,
        10 : 100
    }
    
    return NthNum[num]

def findNth2(num):
    return 19 + (num - 1) * 9

if __name__ == "__main__":
    print(findNth1(3))
    print(findNth2(10))