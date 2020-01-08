'''
Given a list of numbers and a number k,
return whether any two numbers from the list add up to k
'''

def sumInList(list, k):
    listSet = set(list)
    for i in list:
        if (k-i) in listSet:
            return True
    return False 

print(sumInList([10, 15, 3, 7], 17))    #True
print(sumInList([10, 15, 3, 4], 17))    #False  