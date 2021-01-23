from unittest import TestCase, main


# Given a string s, return the longest palindromic substring in s.

class Solution:

    def odd_palindrome(self, s: str, left: int, right: int) -> bool:
        if s[left] is s[right]:
            if left is 0:
                return True
            else:
                return self.odd_palindrome(s, left - 1, right + 1)
        else:
            return False

    def even_palindrome(self, s: str, left: int, right: int) -> bool:
        if s[left] is s[right]:
            if left is 0:
                return True
            else:
                return self.even_palindrome(s, left - 1, right + 1)
        else:
            return False

    def longestPalindrome(self, s: str) -> str:
        if len(s) is 1:
            return s

        answer = ''

        for index in range(len(s)):
            word = s[index]
            for char in s[index + 1:]:
                word += char
                half_num = len(word) // 2
                if len(word) % 2:
                    result = self.odd_palindrome(word, half_num, half_num)
                else:
                    result = self.even_palindrome(word, half_num - 1, half_num)
                if result and len(word) > len(answer):
                    answer = word
                elif not result and answer is '':
                    answer = s[0]
        return answer


class SolutionTest(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_case(self):
        answer = self.solution.longestPalindrome("babad")
        self.assertEqual(answer, "bab")

    def test_second_case(self):
        answer = self.solution.longestPalindrome("cbbd")
        self.assertEqual(answer, "bb")

    def test_third_case(self):
        answer = self.solution.longestPalindrome("a")
        self.assertEqual(answer, "a")

    def test_fourth_case(self):
        ans = self.solution.longestPalindrome("ac")
        self.assertEqual(ans, "a")

    def test_fifth_case(self):
        ans = self.solution.longestPalindrome("ccd")
        self.assertEqual(ans, "cc")


if __name__ == "__main__":
    main()
