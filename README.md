# Challenges
All the challenges I have completed

Closest Value to Zero:[C#](https://github.com/SmithyACoding/Challenges/blob/3d53138cfe4ceb369f43f98fb79dba85333ad1fe/C%23/ClosestToZero.CS) [Python](https://github.com/SmithyACoding/Challenges/blob/3d53138cfe4ceb369f43f98fb79dba85333ad1fe/Python/ClosestToZero.py)
The challenge of this was that some values were negative. I decided to use Math.Abs but I am aware that I could have created a variable to store the difference, check if each element is less than 0, multiply it by -1 if it is and then either way, store it in that difference variable to use for the checks later on. For the sake of shorter code and because the data sets were quite small, I chose the Math.Abs but I appreciate it does have a minor impact on the speed of the algorithm.

Merging strings alternatively: [C#](https://github.com/SmithyACoding/Challenges/blob/3d53138cfe4ceb369f43f98fb79dba85333ad1fe/C%23/AlternateMergeString.CS) [Python](https://github.com/SmithyACoding/Challenges/blob/3d53138cfe4ceb369f43f98fb79dba85333ad1fe/Python/AlternateMergeString.py)
The challenge of this was that one string could be longer than the other. In this case, you only want to keep concatenating values from the longer string. However, I know there could be a more efficient solution than checking the length of each word every iteration of the for loop but I'm not sure how I would do this without adding much more complexity and if it would drastically affect the readability. 

Two Sum: [C#](https://github.com/SmithyACoding/Challenges/blob/b317dc5ed087dad771acc5551962baccf0da6728/C%23/TwoSum.cs) [Python](https://github.com/SmithyACoding/Challenges/blob/b317dc5ed087dad771acc5551962baccf0da6728/Python/TwoSum.py)
The challenge of this was not just trying to make do with the array/list and use loops/nested loops to search through ineffeciently. Inserting items into a dictionary and checking them as we go was a much more efficient solution, although I did originally just add items first and then check the dicitonary before I realised it was more optimal to just do the checks as we go. 

Is Subsequence: [C#](https://github.com/SmithyACoding/Challenges/blob/0687b41f3d3dc5193937291ea62159677a5065cf/C%23/IsSubsequence.cs) [Python](https://github.com/SmithyACoding/Challenges/blob/0687b41f3d3dc5193937291ea62159677a5065cf/Python/IsSubsequence.py)
The challenge of this was figuring out how to go through and compare the letters. The first thought might be to use nested loops, but obviously these are not efficient. By using pointers, we can iterate through the input list, incrementing the subsequence string pointer whenever we get a match and then check if we got to the end of the subsequence string at the end. 
