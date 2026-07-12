class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = set()
        max_count = 0

        left = 0

        for right in range(len(s)):

            while s[right] in longest:
                longest.remove(s[left])
                left += 1

            longest.add(s[right])
            max_count = max(max_count, len(longest))

        return max_count