from typing import List
from unittest import TestCase, main
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneDict = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"],
            '0': [" "]
        }
        digitsList = list(digits)
        searchList = []
        for dig in digitsList:
            searchList.append(phoneDict.get(dig))

        ans = []
        for com in list(product(*searchList)):
            if len(com) != 0:
                ans.append(''.join(com))

        return ans


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_first_case(self):
        ans = self.sol.letterCombinations(digits="23")
        self.assertEqual(ans, ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    def test_second_case(self):
        ans = self.sol.letterCombinations(digits="")
        self.assertEqual(ans, [])


if __name__ == '__main__':
    main()
