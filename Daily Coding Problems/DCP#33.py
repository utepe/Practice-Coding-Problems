'''
Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers
'''
def mergeSort(list):
    if len(list) <= 1:
        return list

    #split list into right and left
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return merge(mergeSort(left), mergeSort(right))
    
def merge(left, right):
    i, j = 0, 0
    sorted = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    
    sorted += left[i:]
    sorted += right[j:]
    return sorted
            
def findMedianForEach(aList):
    temp = []
    i = 0
    j = 0
    k = len(aList) - 1
    while i < len(aList):
        temp.append(aList[i])
        list = mergeSort(temp)
        if i == 0:
            print(list[i])
        else:
            if len(list) % 2 == 1:
                print(list[len(list)//2])
            else:
                lower, upper = len(list)//2 - 1, len(list)//2
                median = (list[lower] + list[upper]) / 2
                print(median)
        i += 1
    
findMedianForEach([2, 1, 5, 7, 2, 0, 5])
    
    