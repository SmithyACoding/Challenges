/*Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

 

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
*/


public class Solution {
    public int FindClosestNumber(int[] nums) {
        var closestNum = nums[0];
        for (int i=1; i < nums.Length; i++)
        {
            //Check if the current item in the list's distance is less than our current closest number
            if ((Math.Abs(nums[i])) < Math.Abs(closestNum)) 
            {
                //Update the closest num
                closestNum = nums[i];
            }
            //If they're the same distance AND the current item in the list is larger
            else if ((Math.Abs(nums[i]) == Math.Abs(closestNum)) & (nums[i] > closestNum)) 
            {
                //Make the current item in the list the new closest
                closestNum = nums[i];
                
            } 

        }
        return closestNum;
    }
}
