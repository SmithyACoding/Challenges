/*
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
*/


public class Solution {
    public bool IsSubsequence(string s, string t) {
        //Create a pointer for each string
        int sPointer = 0, tPointer = 0;
        //While we're not at the end of each string
        while (sPointer < s.Length & tPointer < t.Length)
        {
            //if the letters match
            if (s[sPointer] == t[tPointer])
                //increment the s pointer
                sPointer += 1;
            //check the next letter in t
            tPointer += 1;
        }

        //if we got through each letter in the s string
        if (sPointer == s.Length)
            //we found the sebsequence
            return true;
        else 
            //we did not find the subsequence
            return false;
    }
}
