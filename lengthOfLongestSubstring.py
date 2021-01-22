# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = []
        length = 0
        lengthCheck = 0
        for char in list(s):
            if str(char) in word:
                if len(word) > length:
                    length = len(word)
                word = [char]
            else:
                word.append(char)
                lengthCheck += 1
        if len(s) is lengthCheck:
            return len(s)
        return length if len(word) < length else len(word)


if __name__ == '__main__':
    solution = Solution()
    testCase1 = solution.lengthOfLongestSubstring("abcabcbb")
    print(testCase1)
    testCase2 = solution.lengthOfLongestSubstring("bbbbb")
    print(testCase2)
    testCase3 = solution.lengthOfLongestSubstring("pwwkew")
    print(testCase3)
    testCase4 = solution.lengthOfLongestSubstring(" ")
    print(testCase4)
    testCase5 = solution.lengthOfLongestSubstring("aab")
    print(testCase5)
    testCase6 = solution.lengthOfLongestSubstring("dvdf")
    print(testCase6)
