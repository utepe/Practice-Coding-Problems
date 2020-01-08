'''
Given a multiset of integers, return whether it can be
partitioned into two subsets whose sums are the same
'''

def sameSumSubSet(multiSet):
    if len(multiSet) == 1 or len(multiSet) == 0:
        return False
    totalSum = 0
    for i in multiSet:
        totalSum += i
    if totalSum%2 is 0:
        if totalSum/2 in multiSet:
            return True
        else:
            for i in multiSet:
                if (totalSum/2 - i) in multiSet:
                    return True
            
    return False
    
print(sameSumSubSet([15, 5, 20, 10, 35, 15, 10]))   #True
print(sameSumSubSet([15, 5, 20, 10, 35]))           #False
print(sameSumSubSet([1, 2, 3, 4, 9, 1]))            #True
print(sameSumSubSet([1, 1, 1, 1, 1, 1, 6]))         #True
print(sameSumSubSet([1, 5, 11, 5]))                 #True
print(sameSumSubSet([1, 5, 3]))                     #False