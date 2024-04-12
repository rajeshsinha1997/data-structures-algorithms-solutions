# problem - https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
# tags - string, array


from typing import List
from unittest import TestCase


# Solution Class
class Solution:

    def mostWordsFound(self, sentences: List[str]) -> int:
        # return the maximum number of spaces a sentence contains incremented by 1
        return max(__sen.count(' ') for __sen in sentences) + 1


# Test Class
class TestLeetCode2114(TestCase):

    def test_mostWordsFound(self) -> None:
        # create instance of the Solution class
        __solution = Solution()

        # tests
        self.assertEqual(first=6, second=__solution.mostWordsFound(sentences=[
            'alice and bob love leetcode', 'i think so too', 'this is great thanks very much'
            ]))
        self.assertEqual(first=3, second=__solution.mostWordsFound(sentences=[
            'please wait', 'continue to fight', 'continue to win'
            ]))
