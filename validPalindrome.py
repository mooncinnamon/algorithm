import re
import collections
from typing import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]

    def isListPalindrome(self, s: str) -> bool:
        palindrome = []
        for char in s:
            if char.isalnum():
                palindrome.append(char.lower())

        while len(palindrome) > 1:
            if palindrome.pop(0) != palindrome.pop():
                return False

        return True

    def isDequePalindrome(self, s: str) -> bool:
        palindrome: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                palindrome.append(char.lower())

        while len(palindrome) > 1:
            if palindrome.popleft() != palindrome.pop():
                return False

        return True
