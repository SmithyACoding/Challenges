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
       
        suffix = prefix = 1
        #Create the answer list filled with 1s
        answer = [1]*len(nums)

        #Calculate the prefix by setting the current value in answer to the prefix and stepping forwards through the list 
        for i in range(len(nums)):
            answer[i] = prefix
            #Then update the prefix by multiplying it by the number at that position in nums
            prefix *= nums[i]
        #Calculate the suffix by multiplying the current value in answer by the suffix and stepping backwards through the list
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= suffix
            #Then update the suffix by multiplying it by the number at that position in nums
            suffix *= nums[i]
            print(suffix)
        
        return answer

            
