from unittest import TestCase, main


class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        for char in s:
            if result == "" and (char == "-" or char == "+"):
                result = "+" if char == "+" else "-"
            elif char.isdigit():
                result += char
            elif result == "" and char == " ":
                continue
            elif not char.isdigit() or char == " ":
                break

        result = int(0 if result == "" or result == "+" or result == "-" else result)

        if result < -2 ** 31:
            return -2 ** 31
        elif result > 2 ** 31:
            return 2 ** 31
        else:
            return result


class SolutionTest(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_case(self):
        ans = self.solution.myAtoi("42")
        self.assertEqual(ans, 42)

    def test_second_case(self):
        ans = self.solution.myAtoi("-42")
        self.assertEqual(ans, -42)

    def test_third_case(self):
        ans = self.solution.myAtoi("4193 with words")
        self.assertEqual(ans, 4193)

    def test_fourth_casE(self):
        ans = self.solution.myAtoi("-91283472332")
        self.assertEqual(ans, -2147483648)

    def test_fifth_case(self):
        ans = self.solution.myAtoi("words and 987")
        self.assertEqual(ans, 0)

    def test_sixth_case(self):
        ans = self.solution.myAtoi("+-12")
        self.assertEqual(ans, 0)

    def test_seventh_case(self):
        ans = self.solution.myAtoi("   -42")
        self.assertEqual(ans, 0)


if __name__ == "__main__":
    main()
