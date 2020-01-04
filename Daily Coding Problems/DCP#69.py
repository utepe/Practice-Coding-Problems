'''
Given a list of integers, return the largest product
that can be made by multiplying any three integers
'''
def maxProduct(list, n):    #O(nlogn) - due to .sort()
    if len(list) < 3:
        return "Not enough values in list"
    elif len(list) == 3:
        return list[0] * list[1] * list[2]
    else:
        list.sort()
        return max(list[0]*list[1]*list[n-1], list[n-3]*list[n-2]*list[n-1])

if __name__ == '__main__':
    list = [-10, -10, 5, 2]
    n = len(list)
    maxProd = maxProduct(list, n)
    print(maxProd)