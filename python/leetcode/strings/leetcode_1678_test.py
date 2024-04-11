# problem - https://leetcode.com/problems/goal-parser-interpretation/description/
# tags - string


from unittest import TestCase


# Solution Class
class Solution:

    def interpret(self, command: str) -> str:
        # create a result string
        __result: str = ''

        # create variable to iterate over indices
        __ind: int = 0

        # iterate over the given string by index
        while __ind < len(command):
            # check if the current character is 'G'
            if command[__ind] == 'G':
                # add 'G' to the result string
                __result += 'G'

                # increment index by 1
                __ind += 1
            # else check if the next character is ')'
            elif command[__ind+1] == ')':
                # add 'o' to the result string
                __result += 'o'

                # increment index by 2
                __ind += 2
            # else add 'al' to the result string
            else:
                __result += 'al'

                # increment index by 4
                __ind += 4

        # return the result string
        return __result


# Test Class
class TestLeetCode1678(TestCase):

    def test_interpret(self) -> None:
        # create instance of the Solution class
        __solution = Solution()

        # tests
        self.assertEqual(first='Goal', second=__solution.interpret(command='G()(al)'))
        self.assertEqual(first='Gooooal', second=__solution.interpret(command='G()()()()(al)'))
        self.assertEqual(first='alGalooG', second=__solution.interpret(command='(al)G(al)()()G'))
