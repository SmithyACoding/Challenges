/*
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
*/


public class Solution {
    public string MergeAlternately(string word1, string word2) {
        //Output string
        string merged = "";

        //Loop for the length of the longest word
        for (int i = 0; i < Math.Max(word1.Length, word2.Length); i++) 
        {
            //Check if there's any letters left
            //Add letters to new string
            if (word1.Length > i)
                merged += word1[i];
            if (word2.Length > i)
                merged += word2[i];
        }
        return merged;
    }
}
//This could be more effecient by not having to check the length of the words each iteration (especially if one list is substantially larger than the other)
