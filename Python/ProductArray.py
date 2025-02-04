'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
 
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        suffix = 1
        #Create the answer list filled with 1s
        answer = [1]*len(nums)

        #Calculate the prefix by multiplying previous values in nums and answer into the answer list 
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1] #E.G [1,2,3,4] = [1,1,2,6] (1*1, 2*1, 2*3)
        #Calculate the suffix by multiplying the current value in answer by the suffix and stepping backwards through the list
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= suffix #E.G 6*1, 2*4, 1*12, 1*24 
            #Then update the suffix by multiplying it by the number at that position in nums
            suffix *= nums[i] #E.G 1*4, 4*3, 12*2, 24*1
        
        return answer
