class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        if sorted(word1.count(c) for c in set(word1)) != sorted(word2.count(c) for c in set(word2)):
            return False

        return True