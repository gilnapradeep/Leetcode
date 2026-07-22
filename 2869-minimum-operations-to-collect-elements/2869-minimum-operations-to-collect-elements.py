class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        collected = set()

        for operations, value in enumerate(reversed(nums), start=1):
            if value <= k:
                collected.add(value)

            if len(collected) == k:
                return operations