'''
Given an array of integers, return a new array such that
each element at index i of the new array is the product
of all the numbers in the original array except the one at i
'''
def factorsOfList(nums):
    if len(nums) == 1:
        return None 
    prodList= []
    prod = 1
    for i in nums:
        prod *= i
    for _ in range(len(nums)):
        prodList.append(prod)
    for i in range(len(nums)):
        prodList[i] /= nums[i]

    return prodList

#function without division
def factorsOfList2(nums):
    if len(nums) == 1:
        return None
    temp = 1
    prod = [1] * len(nums)
    for i in range(len(nums)):
        prod[i] = temp
        temp *= nums[i]
    temp = 1
    for i in range(len(nums)-1, -1, -1):
        prod[i] *= temp
        temp *= nums[i]
    
    return prod


print(factorsOfList2([1, 2, 3, 4, 5]))  #[120, 60, 40, 30, 24]           
print(factorsOfList2([3, 2, 1]))        #[2, 3, 6]
print(factorsOfList2([10, 3, 5, 6, 2])) #[180, 600, 360, 300, 900]