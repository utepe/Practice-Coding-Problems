'''
Given integers N and X, write a function that returns
the number of times X appears as a value in
 an N by N multiplication table
'''
#brute force? thought I was being slick by not using 2 loops but :/
def xInMultiTable(N, X):
    multiplicationTable = {}
    x = 1
    i = 1
    count = 0
    while count < N:
        if i <= N:
            if i == 1:
                multiplicationTable[x] = []
            multiplicationTable[x].append(x * i)
            i += 1
        else:
            i = 1
            count += 1
            x += 1
    appearance = 0
    for multiples in multiplicationTable.values():
        if X in multiples:
            appearance += 1
    
    return appearance

#doesn't work for all cases but for some cases
def getMultipleCount(N, X):
    if N == 1: return N
    
    appearance = 0
    for i in range(1, (X+1)//2):
        if X%i == 0:
            appearance += 1
    return 1
    
print(getMultipleCount(6, 4))
print(xInMultiTable(6, 4))
print(xInMultiTable(2, 4))
print(xInMultiTable(3, 6))