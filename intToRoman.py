from unittest import TestCase, main


class Solution:
    def intToRomanOneNumber(self, a: str, b: str, c: str, num: int) -> str:
        if num == 1:
            return a
        elif num == 2:
            return a + a
        elif num == 3:
            return a + a + a
        elif num == 4:
            return a + b
        elif num == 5:
            return b
        elif num == 6:
            return b + a
        elif num == 7:
            return b + a + a
        elif num == 8:
            return b + a + a + a
        elif num == 9:
            return a + c
        elif num == 0:
            return a + c

    def intToRoman(self, num: int) -> str:
        roman = ""
        n = num
        a = 1
        while n:
            if a == 1:
                roman = self.intToRomanOneNumber('I', 'V', 'X', n % 10) + roman
            elif a == 10:
                roman = self.intToRomanOneNumber('X', 'L', 'C', n % 10) + roman
            elif a == 100:
                roman = self.intToRomanOneNumber('C', 'D', 'M', n % 10) + roman
            elif a == 1000:
                roman = self.intToRomanOneNumber('M', '', '', n % 10) + roman
            n = n // 10
            a *= 10
        return roman


class SolutionTest(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_case(self):
        ans = self.solution.intToRoman(num=3)
        self.assertEqual(ans, "III")

    def test_second_case(self):
        ans = self.solution.intToRoman(num=4)
        self.assertEqual(ans, "IV")

    def test_third_case(self):
        ans = self.solution.intToRoman(num=9)
        self.assertEqual(ans, "IX")

    def test_fifth_case(self):
        ans = self.solution.intToRoman(num=58)
        self.assertEqual(ans, "LVIII")

    def test_sixth_case(self):
        ans = self.solution.intToRoman(num=1994)
        self.assertEqual(ans, "MCMXCIV")


if __name__ == '__main__':
    main()