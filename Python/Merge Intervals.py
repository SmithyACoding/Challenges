'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input. 
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        #sort the list by the first item in each lsit
        intervals.sort(key=lambda x: x[0])
        #Get the first list
        previous = intervals[0]
        #start from the second list and check each previous ones
        for interval in intervals[1:]:
            #If the starting item of the current list is less than or equal to the ending item in the previous interval
            if interval[0] <= previous[1]:
                #Update prev to have the new ending time
                previous[1] = max(previous[1], interval[1])
            else:
                #Add prev to the merged list
                merged.append(previous)
                #Update prev to be the current interval
                previous = interval
        #Append the last interval
        merged.append(previous)

        return merged

