# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# class Solution(object):
def twoSum( nums, target): 
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    firstArrIdx = 0
    secArrIdx = 1
    while firstArrIdx > len(nums):
        if (nums[firstArrIdx] + nums[secArrIdx]) == target:
            print(firstArrIdx, secArrIdx)
            break
        else:                
            secArrIdx = firstArrIdx + 2
            firstArrIdx += 1
            print("1st:", firstArrIdx)
            print("2nd:", secArrIdx)
    
    return firstArrIdx, secArrIdx

# solution = Solution()
nums = [2, 7, 11, 15]
nums = [3,2,4]
target = 6
print(twoSum(nums, target))
