# Challenges
All the challenges I have completed

Closest Value to Zero:[C#](https://github.com/SmithyACoding/Challenges/blob/3d53138cfe4ceb369f43f98fb79dba85333ad1fe/C%23/ClosestToZero.CS) [Python](https://github.com/SmithyACoding/Challenges/blob/3d53138cfe4ceb369f43f98fb79dba85333ad1fe/Python/ClosestToZero.py)
The challenge of this was that some values were negative. I decided to use Math.Abs but I am aware that I could have created a variable to store the difference, check if each element is less than 0, multiply it by -1 if it is and then either way, store it in that difference variable to use for the checks later on. For the sake of shorter code and because the data sets were quite small, I chose the Math.Abs but I appreciate it does have a minor impact on the speed of the algorithm.

Merging strings alternatively: [C#](https://github.com/SmithyACoding/Challenges/blob/3d53138cfe4ceb369f43f98fb79dba85333ad1fe/C%23/AlternateMergeString.CS) [Python](https://github.com/SmithyACoding/Challenges/blob/3d53138cfe4ceb369f43f98fb79dba85333ad1fe/Python/AlternateMergeString.py)
The challenge of this was that one string could be longer than the other. In this case, you only want to keep concatenating values from the longer string. However, I know there could be a more efficient solution than checking the length of each word every iteration of the for loop but I'm not sure how I would do this without adding much more complexity and if it would drastically affect the readability. 

Two Sum: [C#](https://github.com/SmithyACoding/Challenges/blob/b317dc5ed087dad771acc5551962baccf0da6728/C%23/TwoSum.cs) [Python](https://github.com/SmithyACoding/Challenges/blob/b317dc5ed087dad771acc5551962baccf0da6728/Python/TwoSum.py)
The challenge of this was not just trying to make do with the array/list and use loops/nested loops to search through ineffeciently. Inserting items into a dictionary and checking them as we go was a much more efficient solution, although I did originally just add items first and then check the dicitonary before I realised it was more optimal to just do the checks as we go. 

Is Subsequence: [C#](https://github.com/SmithyACoding/Challenges/blob/0687b41f3d3dc5193937291ea62159677a5065cf/C%23/IsSubsequence.cs) [Python](https://github.com/SmithyACoding/Challenges/blob/0687b41f3d3dc5193937291ea62159677a5065cf/Python/IsSubsequence.py)
The challenge of this was figuring out how to go through and compare the letters efficiently. The first thought might be to use nested loops, but obviously this is not optimal. By using pointers, we can iterate through the input list, incrementing the subsequence string pointer whenever we get a match and then check if we got to the end of the subsequence string at the end. 

Best Time to Buy and Sell: [C#](https://github.com/SmithyACoding/Challenges/blob/41c85fc0b90d9823a9e4784657dc0d200a14edf3/C%23/Stock.cs) [Python](https://github.com/SmithyACoding/Challenges/blob/41c85fc0b90d9823a9e4784657dc0d200a14edf3/Python/Stock.py)
The challenge of this was trying to figure out how to calculate the profit without comparing all the items. I did this in Python by keeping track of the best price and then the best profit and updating each if needed. In C# this is a little easier as I could use the Min and Max to just compare but they are not efficient enough to warrant their use in Python which added some extra logic required to figure out how to do it without using these.

Longest Common Prefix: [C#](https://github.com/SmithyACoding/Challenges/blob/22b43fa5bfb5d3dc22ee67d7a90508c2888f84e3/C%23/CommonPrefix.cs) [Python](https://github.com/SmithyACoding/Challenges/blob/22b43fa5bfb5d3dc22ee67d7a90508c2888f84e3/Python/CommonPrefix.py)
The challenge of this was thinking of a way to check and compare each letter in each string until they're no longer the same. I did consider using a Trie for this as the prefix would be stored as the first letters in the trie but I feel this is a bit overcomplicated and unnecessary. Alternatively, I decided to sort the string lexicographically which will give us the two most different strings as the first and last of the array. We can then just iterate through the shortest of these two and compare letters until they no longer match, returning those letters which did. 

Summary of Ranges: [C#](https://github.com/SmithyACoding/Challenges/blob/1ac8ba338469a1e6b9fa231ec4cd1733fa80efbd/C%23/Ranges.cs) [Python](https://github.com/SmithyACoding/Challenges/blob/cab026980d1bf219c146be704af8d25dadf4da65/Python/Ranges.py)
The challenge of this was trying to figure out how to keep track of the valid ranges. I decided to use two loops, one to iterate each over each number in nums and then another to increment i while the numbers are consecutive to each other. I could then format the string with the starting num and the num at the index that we finished incrementing to or just add the single number.
