class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        if len(s)<3:
            return max(s)
        arr=sorted(s)
        return arr[-3]