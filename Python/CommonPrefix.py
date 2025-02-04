'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""
        #Sort the strings lexicographically (alphabetically)
        strs = sorted(strs)
        #Set the smallest and largest 
        smallest, largest = strs[0], strs[-1]

        #Iterate for the shortest of the two strings
        for i in range(min(len(smallest),len(largest))):
            #compare the letters
            if smallest[i] == largest[i]:
                #Update the prefix
                prefix += smallest[i]
            else:
                #Break when they're not the same
                break
        return prefix


        
