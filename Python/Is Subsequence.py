'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Create a pointer for each string
        sPointer, tPointer = 0, 0

        #While we're not at the end of each string
        while sPointer < len(s) and tPointer < len(t):
            #if the letters match
            if s[sPointer] == t[tPointer]:
                #increment the s pointer
                sPointer += 1
            #check the next letter in t
            tPointer += 1

        #if we got through each letter in the s string
        if sPointer == len(s):
            #we found the sebsequence
            return True
        else: 
            #we did not find the subsequence
            return False
