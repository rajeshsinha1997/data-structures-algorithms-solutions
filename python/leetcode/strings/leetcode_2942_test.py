# problem - https://leetcode.com/problems/find-words-containing-character/description/
# tags - string, array


from typing import List
from unittest import TestCase


# Solution Class
class Solution:

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # iterate over the given list of words using the indices and check if
        # the required character present in the current word, if present add
        # the current index to the result list
        return [__ind for __ind, __w in enumerate(iterable=words) if x in __w]


# Test Class
class TestLeetCode2942(TestCase):

    def test_findWordsContaining(self):
        # create instance of the Solution class
        __solution = Solution()

        # tests
        self.assertEqual(first=[0, 1], second=__solution.findWordsContaining(words=['leet', 'code'], x='e'))
        self.assertEqual(first=[0, 2], second=__solution.findWordsContaining(words=['abc', 'bcd', 'aaaa', 'cbc'], x='a'))
        self.assertEqual(first=[], second=__solution.findWordsContaining(words=['abc', 'bcd', 'aaaa', 'cbc'], x='z'))
