# problem - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
# tags - array, string, simulation


from typing import List
from unittest import TestCase


class Solution:

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # iterate over the list of operations and add 1 to the starting value
        # if the current operation is increment, else subtract 1 from the starting
        # value, and return the final result when all operations are completed
        return sum((1 if __op[1] == '+' else -1 for __op in operations), start=0)


# Test Class
class TestLeetCode2011(TestCase):

    def test_finalValueAfterOperations(self) -> None:
        # create instance of the Solution class
        __solution = Solution()

        # tests
        self.assertEqual(first=1, second=__solution.finalValueAfterOperations(operations=["--X","X++","X++"]))
        self.assertEqual(first=3, second=__solution.finalValueAfterOperations( operations=["++X","++X","X++"]))
        self.assertEqual(first=0, second=__solution.finalValueAfterOperations( operations=["X++","++X","--X","X--"]))
