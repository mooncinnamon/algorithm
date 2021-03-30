import unittest
from validPalindrome import Solution as ValidPalindrome


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class ValidPalindromeTestCae(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = ValidPalindrome()

    def test_first_case(self):
        ans = self.sol.isPalindrome(s="A man, a plan, a canal: Panama")
        self.assertEqual(ans, True)

if __name__ == '__main__':
    unittest.main()
