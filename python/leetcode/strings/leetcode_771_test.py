# problem - https://leetcode.com/problems/jewels-and-stones/description/
# tags - string, hash-table


from unittest import TestCase


# Solution Class
class Solution:

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # create a set out of the list of jewels
        __jewel_set = set(jewels)

        # count how many stones are jewel and return the count
        return sum((1 if __s in __jewel_set else 0 for __s in stones), start=0)


# Test Class
class TestLeetCode771(TestCase):

    def test_numJewelsInStones(self) -> None:
        # create instance of the Solution class
        __solution = Solution()

        # tests
        self.assertEqual(first=3, second=__solution.numJewelsInStones(jewels='aA', stones='aAAbbbb'))
        self.assertEqual(first=0, second=__solution.numJewelsInStones(jewels='z', stones='ZZ'))
