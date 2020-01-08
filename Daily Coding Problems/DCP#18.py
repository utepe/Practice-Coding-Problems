'''
Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length 
'''
#Try to impliment in O(n) time
def maxOfSubList(nums, k):
    size = len(nums)
    maxSubList = []
    for i in range(size+1-k):
        maxSubList.append(max(nums[i:k+i]))
    return maxSubList

print(maxOfSubList([10, 5, 2, 7, 8, 7], 3))
print(maxOfSubList([5, 2, 1], 2))