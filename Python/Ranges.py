'''
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 '''

class Solution:
    def summaryRanges(self, nums):
        ranges = []
        i = 0
        while i < len(nums):
            start = nums[i]
            #While the numbers are consecutive
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                #increment i
                i += 1
            #When they're no longer consecutive and there's more than one number, format it with ->
            if start != nums[i]:
                ranges.append(str(start) + "->" + str(nums[i]))
            #Otherwise append the single number
            else:
                ranges.append(str(nums[i])) 
            #increment i
            i+=1
        return ranges
