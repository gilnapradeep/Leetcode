class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        max_freq = 0
        max_length = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            max_freq = max(max_freq, count[s[right]])

            window_length = right - left + 1

            while window_length - max_freq > k:
                count[s[left]] -= 1
                left += 1
                window_length = right - left + 1

            max_length = max(max_length, window_length)

        return max_length
