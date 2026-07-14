class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = set()
        max_count = 0
        i = 0
        start = 0

        while i < len(s):

            if s[i] in longest:
                max_count = max(max_count, len(longest))

                # remove characters from the beginning
                while s[i] in longest:
                    longest.remove(s[start])
                    start += 1

            longest.add(s[i])
            i += 1

        max_count = max(max_count, len(longest))

        return max_count