# problem - https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
# tags - string, greedy, counting


from unittest import TestCase


# Solution Class
class Solution:

    def balancedStringSplit(self, s: str) -> int:
        # create a counter to store the count of the balanced strings
        __counter: int = 0

        # create a sum variable to hold the sum value
        __sum: int = 0

        # iterate over the given string
        for __c in s:
            # decrement sum by 1 if the current character is 'L',
            # else increment sum by 1
            __sum += -1 if __c == 'L' else 1

            # check if the sum value is 0
            if __sum == 0:
                # increment counter by 1
                __counter += 1

        # return the counter
        return __counter


# Test Class
class TestLeetCode1221(TestCase):

    def test_balancedStringSplit(self) -> None:
        # create instance of the Solution class
        __solution = Solution()

        # tests
        self.assertEqual(first=4, second=__solution.balancedStringSplit(s='RLRRLLRLRL'))
        self.assertEqual(first=2, second=__solution.balancedStringSplit(s='RLRRRLLRLL'))
        self.assertEqual(first=1, second=__solution.balancedStringSplit(s='LLLLRRRR'))
