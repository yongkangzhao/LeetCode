'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.


Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best_sum = inf
        nums.sort()
        L = len(nums)
        for i in range(L-2):
            # check/filter lower bound
            sums = nums[i]+nums[i+1]+nums[i+2]
            if sums >= target:
                best_sum = min(best_sum, sums, key = lambda x:abs(x-target))
                break
                
            # check/filter upper bound
            sums = nums[i]+nums[-1]+nums[-2]
            if sums <= target:
                best_sum = min(best_sum, sums, key = lambda x:abs(x-target))
                continue
                
            j, k = i+1, L-1
            while j < k:
                sums = nums[i]+nums[j]+nums[k]
                if sums > target:
                    k -= 1
                elif sums < target:
                    j += 1
                else:
                    return sums
                best_sum = min(best_sum, sums, key = lambda x:abs(x-target))
        return best_sum