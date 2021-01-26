from typing import List
from unittest import TestCase, main


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        move = True  # True is Left, False is Right
        max = 0
        while left != right:
            col = height[left] if height[left] < height[right] else height[right]
            row = right - left
            val = col * row

            if max < val:
                max = val

            if height[left] < height[right]:
                left += 1
                move = True
            elif height[left] == height[right]:
                if move:
                    right -= 1
                else:
                    left += 1
            elif height[left] > height[right]:
                right -= 1
                move = False
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
