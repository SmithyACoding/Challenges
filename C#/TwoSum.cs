/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
*/


public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        //Convert array to dictionary
        Dictionary<int, int> dict = new Dictionary<int, int>();
            for (int i = 0; i < nums.Length; i++){
                //Get the difference
                int difference = target - nums[i];
                //If the difference already exists in the dict
                if (dict.ContainsKey(difference)){
                    //We have found the solution and can return the index of the difference and current num 
                    return new int[]{dict[difference], i};
                }
                //otherwise insert element into dictionary and move on
                dict[nums[i]] = i;
            }
            //Just in case there are no pairs
            return [];
        }
    }
