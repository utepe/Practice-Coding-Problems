'''
Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers
'''
def mergeSort(aList):
    if len(aList) > 1:
        mid = len(aList)//2
        leftHalf = aList[:mid]
        rightHalf = aList[mid:]
        
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i=0
        j=0
        k=0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                aList[k] = leftHalf[i]
                i += 1
            else:
                aList[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            aList[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            aList[k] = rightHalf[j]
            j += 1
            k += 1
            
    return aList
            
def findMedianForEach(aList):
    temp = []
    i = 0
    j = 0
    k = len(aList) - 1
    while i < len(aList):
        temp.append(aList[i])
        mergeSort(temp)
        if i == 0:
            print(temp[i])
        else:
            if len(temp) % 2 == 1:
                print(temp[len(temp)//2])
            else:
                lower, upper = len(temp)//2 - 1, len(temp)//2
                median = (temp[lower] + temp[upper]) / 2
                print(median)
        i += 1
    
findMedianForEach([2, 1, 5, 7, 2, 0, 5])
    
    