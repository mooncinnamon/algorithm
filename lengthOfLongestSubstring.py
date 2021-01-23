# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = ''
        word_list = []
        if s is ' ':
            return 1
        for index in range(len(s)):
            same_pos = word.find(s[index])
            word += s[index]
            if same_pos is not -1:
                word_list.append(len(word) - 1)
                word = word[same_pos + 1:]
            else:
                word_list.append(len(word))
        return max(word_list) if len(word_list) else 0


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
    testCase7 = solution.lengthOfLongestSubstring("aabaab!bb")
    print(testCase7)
    testCase8 = solution.lengthOfLongestSubstring("")
    print(testCase8)
