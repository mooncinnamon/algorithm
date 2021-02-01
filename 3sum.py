from typing import List
from unittest import TestCase, main

from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sort_nums = nums.sort()
        zero_point = list(filter(lambda x: x <= 0, sort_nums))
        minus_zeo_nums = sort_nums[:]


        return []


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_first_case(self):
        ans = self.sol.threeSum(nums=[-1, 0, 1, 2, -1, -4])
        self.assertEqual(ans, [[-1, -1, 2], [-1, 0, 1]])

    def test_second_case(self):
        ans = self.sol.threeSum(nums=[])
        self.assertEqual(ans, [])

    def test_third_case(self):
        ans = self.sol.threeSum(nums=[0])
        self.assertEqual(ans, [])


if __name__ == '__main__':
    main()
