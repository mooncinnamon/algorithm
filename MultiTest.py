import unittest
from validPalindrome import Solution as ValidPalindrome
from reorderDataInLogFiles import Solution as ReorderLogFiles
from mostCommonWord import Solution as MostCommonWord


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class ValidPalindromeTestCae(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = ValidPalindrome()

    def test_first_case(self):
        ans = self.sol.isPalindrome(s="A man, a plan, a canal: Panama")
        self.assertEqual(ans, True)

    def test_second_case(self):
        ans = self.sol.isPalindrome(s="race a car")
        self.assertEqual(ans, False)


class ReorderLogFilesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = ReorderLogFiles()

    def test_first_case(self):
        ans = self.sol.reorderLogFiles(
            logs=["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
        self.assertEqual(ans, ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"])

    def test_second_case(self):
        ans = self.sol.reorderLogFiles(logs=["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"])
        self.assertEqual(ans, ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"])


class MostCommonWordTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = MostCommonWord()

    def test_first_case(self):
        ans = self.sol.mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
                                      banned=["hit"])
        self.assertEqual(ans, "ball")

    def test_second_case(self):
        ans = self.sol.mostCommonWord(paragraph="a.", banned=[])
        self.assertEqual(ans, "a")


if __name__ == '__main__':
    unittest.main()
