class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

            if hashmap[num] > 1:
                return True
        
        return False