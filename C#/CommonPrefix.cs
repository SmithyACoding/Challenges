/*
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
*/

public class Solution {
    public string LongestCommonPrefix(string[] strs) {

        string prefix = "";
        //Sort the strings lexicographically (alphabetically)
        Array.Sort(strs);
        //Set the smallest and largest 
        string smallest = strs[0], largest = strs[strs.Length -1];

        //Iterate for the shortest of the two strings
        for (int i = 0; i < Math.Min(smallest.Length,largest.Length); i++){
            //compare the letters
            if (smallest[i] == largest[i])
                //Update the prefix
                prefix += smallest[i];
            else
                //Break when they're not the same
                break;
        }
        return prefix; 
    }
}
