'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''


from typing import List

# class Solution:
#     def findShortestSubArray(self, nums: List[int]) -> int:
#         degree = {}
#         max_degree = 0
#         max_length = inf
#         for i in range(len(nums)):
#             if nums[i] in degree:
#                 degree[nums[i]][2] += 1
#                 degree[nums[i]][1] = i
#             else:
#                 degree[nums[i]] = [i, i, 1]
#             if (degree[nums[i]][2] > max_degree) or ((degree[nums[i]][2] == max_degree) and ((degree[nums[i]][1] - degree[nums[i]][0]) <= max_length)):
#                 max_degree = degree[nums[i]][2]
#                 max_length = degree[nums[i]][1] - degree[nums[i]][0] + 1
#         return max_length

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = {}
        max_degree = 0
        max_degree_candidate = []
        max_length = inf
        for i in range(len(nums)):
            if nums[i] in degree:
                degree[nums[i]][2] += 1
                degree[nums[i]][1] = i
            else:
                degree[nums[i]] = [i, i, 1]
            if (degree[nums[i]][2] > max_degree):
                max_degree = degree[nums[i]][2]
                max_degree_candidate = [nums[i]]
            elif (degree[nums[i]][2] == max_degree):
                max_degree = degree[nums[i]][2]
                max_degree_candidate += [nums[i]]
        for candiate in max_degree_candidate:
            if (degree[candiate][2] > max_degree) or ((degree[candiate][2] == max_degree) and ((degree[candiate][1] - degree[candiate][0]) <= max_length)):
                max_degree = degree[candiate][2]
                max_length = degree[candiate][1] - degree[candiate][0] + 1
        return max_length