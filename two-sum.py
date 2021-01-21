from typing import List


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for sourceNum in range(len(nums)):
            for targetNum in range(sourceNum + 1, len(nums)):
                if nums[sourceNum] + nums[targetNum] == target:
                    return [sourceNum, targetNum]


if __name__ == '__main__':
    value = Solution().twoSum([2, 7, 11, 15], 9)
    print(value)
