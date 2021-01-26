from typing import List
from unittest import TestCase, main


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0

        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                col = height[right] if height[right] < height[left] else height[left]
                row = right - left
                val = col * row
                if max < val:
                    max = val

        return max


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_case(self):
        ans = self.solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
        self.assertEqual(ans, 49)

    def test_second_case(self):
        ans = self.solution.maxArea(height=[1, 1])
        self.assertEqual(ans, 1)

    def test_third_case(self):
        ans = self.solution.maxArea(height=[4, 3, 2, 1, 4])
        self.assertEqual(ans, 16)

    def test_fourth_case(self):
        ans = self.solution.maxArea(height=[1, 2, 1])
        self.assertEqual(ans, 2)


if __name__ == "__main__":
    main()
