# Newspapers

## Problem Description

You've begun working in the one and only Umbristan, and it is part of your job duty to organize newspapers. Every morning, your fellow coworkers will dilligently read through the newspapers to examine its contents. It is your job to organize the newspapers into piles and hand them out to your coworkers to read through.

Each newspaper is marked with the time it would take to read through its contents. The newspapers are carefully laid out in a line in a particular order that must not be broken when assigning the newspapers. You cannot pick and choose newspapers randomly from the line to assign to a co-worker. Instead, you must take newspapers from a particular subsection of the line, make a pile and give that to a co-worker.

What is the minimum amount of time it would take to have your coworkers go through all the newspapers?

Input

- weights: A list of packages and their weights.

- d: The number of days to deliver all packages.

Output

The minimum weight capacity of the truck.

## Examples

Example 1:
Input: newspapers_read_times = [7,2,5,10,8], num_coworkers = 2
Output: 18
Explanation:
Assign first 3 newspapers to one coworker then assign the rest to another. The time it takes for the first 3 newspapers is 7 + 2 + 5 = 14 and for the last 2 is 10 + 8 = 18.

Example 2:
Input: newspapers_read_times = [2,3,5,7], num_coworkers = 3
Output: 7
Explanation:
Assign [2, 3], [5], and [7] separately to workers. The minimum time is 7.

## Constraints

- 1 <= newspapers_read_times.length <= 10^5

- 1 <= newspapers_read_times[i] <= 10^5

- 1 <= num_coworkers <= 10^5

## Intuition

What immediately jumped out was some similarities between this problem and the prior problem "Capacity to Ship Packages Within D Days". Namely that the minimum time taken to read all newspapers would be the value of the longest singular newspaper in the list of given papers, and the maximum time would be the sum of all newspaper values. With this I was able to determine that we need to pick values inbetween these two pointers and in order to determine the validity, loop over the newspapers array and see if we could distribute them among the given number of coworkers. From there the pointer update logic was quite simple and similar to previous implementations.

## Implementation

Set the left and right pointers to the min and max values described above. Iterate while the left pointer is <= to the right pointer and for each chosen time limit insure you have enough coworkers to distrbute the papers too. If it is a valid time limit change the right pointer to time_limit-1 and if it is not, the left pointer to time_limit+1.

## Complexity

### Time

O(n log(n))

Binary Search is O(log(n)) but the midpoint vetting logic performed in this loop is O(n) thus the final complexity is O(n log(n))

### Space

O(n)

## Notes

- ==Do not fall victim to the "template" way of thinking too much==

- Left and right pointer values are not always 0 and len(input_array) respectively. Be very careful defining your bounds

- Don't be afaid to add helper functions or more "complex" logic in order to get proper comparison/vetting for a valid midpoint value and pointer updates
