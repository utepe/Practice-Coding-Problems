def expotent(x, y):
    if y == 0:
        return 1

    temp = expotent(x, int(y/2))
    
    if y % 2 == 0:
        return temp * temp
    else:
        if y > 0:
            return x * temp * temp
        else:
            return (temp * temp) / x
    
x = expotent(2, 10)
print(x)