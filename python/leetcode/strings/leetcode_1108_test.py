# problem - https://leetcode.com/problems/defanging-an-ip-address/description/
# tags - string


from unittest import TestCase, main


# Solution Class
class Solution:

    def defangIPaddr(self, address: str) -> str:
        # iterate over the given string and add the alternate character
        # to the result if the current character is period, else add the
        # current character to the result, and at last return the result
        return ''.join('[.]' if __c == '.' else __c for __c in address)


# Test Class
class TestLeetCode1108(TestCase):

    def test_leet_code_1108(self) -> None:
        # create instance of the Solution class
        solution = Solution()

        # tests
        self.assertEqual(first='1[.]1[.]1[.]1', second=solution.defangIPaddr(address='1.1.1.1'))
        self.assertEqual(first='255[.]100[.]50[.]0', second=solution.defangIPaddr(address='255.100.50.0'))


# run tests
if __name__ == "__main__":
    main()
