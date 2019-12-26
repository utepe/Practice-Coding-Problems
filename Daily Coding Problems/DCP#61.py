'''
Implement integer exponentiation.
That is, implement the pow(x, y) function
Where x and y are integers and returns x^y.
Do this faster than the naive method of repeated multiplicatio
'''
def expotent(x, y):
    if y == 0:
        return 1

    temp = expotent(x, int(y/2))
    temp2 = temp * temp
    if y % 2 == 0:
        return temp2
    else:
        if y > 0:
            return x * temp2
        else:
            return temp2 / x
    
x = expotent(2, 10)
print(x)