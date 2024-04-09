# problem - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
# tags - array, strings, simulation


from typing import List
from unittest import TestCase


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # create variable X to store the result
        __x: int = 0

        # iterate over the given operations array
        for __operation in operations:
            # check if the operation is increment or decrement
            if __operation[1] == '+':
                # increment value of the X by 1
                __x += 1
            # else decrement value of X by 1
            else:
                __x -= 1

        # return the value of X
        return __x


# Test Class
class TestLeetCode2011(TestCase):

    def test_finalValueAfterOperations(self):
        # create instance of the Solution class
        __solution = Solution()

        # tests
        self.assertEqual(first=1,
                         second=__solution.finalValueAfterOperations(
                             operations=["--X","X++","X++"]
                        ))
        self.assertEqual(first=3,
                         second=__solution.finalValueAfterOperations(
                             operations=["++X","++X","X++"]
                        ))
        self.assertEqual(first=0,
                         second=__solution.finalValueAfterOperations(
                             operations=["X++","++X","--X","X--"]
                        ))
