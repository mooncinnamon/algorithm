from unittest import TestCase, main


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ''
        head_gap = (numRows - 1) * 2
        for row_num in range(numRows):
            word_index = row_num + 1
            while len(s) >= word_index:
                if row_num == 0 or row_num == numRows - 1:
                    result += s[word_index - 1]
                else:
                    next_index = word_index - 1 + head_gap - row_num * 2
                    if next_index < len(s):
                        result += s[word_index - 1] + s[next_index]
                    else:
                        result += s[word_index - 1]
                word_index += head_gap

        return result


class SolutionTest(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_case(self):
        ans = self.solution.convert(s="PAYPALISHIRING", numRows=3)
        self.assertEqual(ans, "PAHNAPLSIIGYIR")

    def test_second_case(self):
        ans = self.solution.convert(s="PAYPALISHIRING", numRows=4)
        self.assertEqual(ans, "PINALSIGYAHRPI")

    def test_third_case(self):
        ans = self.solution.convert(s="A", numRows=1)
        self.assertEqual(ans, 'A')


if __name__ == "__main__":
    main()
