# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = set()
        position = 0
        res = 0

        for i in range(len(s)):
            while s[i] in sub_string:
                sub_string.remove(s[position])
                position += 1
            sub_string.add(s[i])
            res = max(res, i - position + 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s="aab")
    print(result)
