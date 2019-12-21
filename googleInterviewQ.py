#Example From this Link
#https://www.youtube.com/watch?v=XKu_SEDAykw

#Assumes List is already Sorted
def findMatchingPair(list, sum):
    while(len(list) > 1):
        j = len(list) - 1
        if((list[0] + list[j]) == sum):
            return True, list[0], list[len(list) - 1]
        elif((list[0] + list[j]) > sum):
            list.pop()
        else:
            list.pop(0)
    
    return False, "No Pair with Sum"

#Assumes list is not sorted
def findMatchingPair2(list, sum):
    values = set([])            #create a set
    for i in list:
        values.add(i)           #add list elements to set
    
    for i in values:
        if((sum-i) in values):  #if the difference of sum-element is in set return True
            return True
    
    return False

print(findMatchingPair2([1, 2, 3, 9], 8))
print(findMatchingPair2([1, 2, 4, 4], 8))
print(findMatchingPair2([6, 4, 3, 2, 1, 7], 9))