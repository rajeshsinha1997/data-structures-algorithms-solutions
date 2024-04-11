# problem - https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/
# tags - string, greedy


from unittest import TestCase


# Solution Class
class Solution:

    def minPartitions(self, n: str) -> int:
        # return the maximum value present in the given string
        # as an integer
        return int(max(n))


# Test Class
class TestLeetCode1689(TestCase):

    def test_minPartitions(self) -> None:
        # create instance of the Solution class
        __solution = Solution()

        # tests
        self.assertEqual(first=3, second=__solution.minPartitions(n='32'))
        self.assertEqual(first=8, second=__solution.minPartitions(n='8273482734'))
        self.assertEqual(first=9, second=__solution.minPartitions(n='2734620983070918234627346209830709182346'))