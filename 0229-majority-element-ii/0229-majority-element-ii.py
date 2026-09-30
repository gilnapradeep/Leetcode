class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        result = []
        n = len(nums)

        for num in count:
            if count[num] > n // 3:
                result.append(num)

        return result