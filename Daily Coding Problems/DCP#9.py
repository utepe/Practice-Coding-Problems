'''
Given a list of integers, write a function that
returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.
'''
def sumNonAdjacent(nums):
    num1 = max(nums)
    index = nums.index(num1)
    if index == len(nums)-1:
        num2 = max(nums[:index-1])
    else:
        num2 = max(max(nums[:index-1]), max(nums[index+1:]))
    return num1+num2

print(sumNonAdjacent([2, 4, 6, 8])) #12
print(sumNonAdjacent([5, 1, 1, 5])) #10