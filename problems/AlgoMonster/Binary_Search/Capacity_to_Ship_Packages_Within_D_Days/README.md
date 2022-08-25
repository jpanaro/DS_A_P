# Capacity to Ship Packages Within D Days

## Problem Description

There are n packages that needs to be transported from one city to another, and you need to transport them there within d days. For the ith package, the weight of the package is weights[i]. You are required to deliver them in order with a rental truck. The rental trucks come in different sizes. The bigger trucks have greater weight capacity but cost more to rent. To minimize cost, you want to deliver the packages in one truck once per day, with a weight capacity as small as possible to save on rental cost. What is the minimum weight capacity of the truck that is required to deliver all packages within d days?

Input

- weights: A list of packages and their weights.

- d: The number of days to deliver all packages.

Output

The minimum weight capacity of the truck.

## Example

Example 1:
Input:

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = 5
Output: 15

Explanation:

The first day we deliver the first 5 package. The second day we deliver the next 2, and for each following days, we deliver 1. The maximum weight delivered on each day is 15, so we can have a truck with a capacity of 15. This value is the minimum.

## Constraints

- 1 <= len(weights) <= 5 * 10^4

- 1 <= d <= len(weights)

- 1 <= weights[i] <= 500

## Intuition

Two things immediately jumped out, 1, we wanted to always use the max days in order to minimize the truck size, and 2, the truck weight at a minimum had to be greater than the biggest individual weight in the array. Unfortunately I was unable to define the proper values for the left and right pointers as well as the function necessary to check the midpoint value so I ended up running out of time before coming up with a valid solution.

## Implementation

No valid implementation, revisit.

## Complexity

### Time

Add when I complete a valid solution.

### Space

Add when I complete a valid solution.

## Notes

- ==Do not fall victim to the "template" way of thinking too much==

- Left and right pointer values are not always 0 and len(input_array) respectively. Be very careful defining your bounds

- Don't be afaid to add helper functions or more "complex" logic in order to get proper comparison/vetting for a valid midpoint value and pointer updates
