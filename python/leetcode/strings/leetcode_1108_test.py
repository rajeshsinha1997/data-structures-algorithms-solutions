# problem - https://leetcode.com/problems/defanging-an-ip-address/description/
# tags - strings


from unittest import TestCase, main


# Solution Class
class Solution:

    def defangIPaddr(self, address: str) -> str:
        # replace the period characters in the given address and return
        return address.replace('.', '[.]')


# Test Class
class TestLeetCode1108(TestCase):

    def test_leet_code_1108(self):
        # create instance of the Solution class
        solution = Solution()

        # tests
        self.assertEqual(first='1[.]1[.]1[.]1', second=solution.defangIPaddr(address='1.1.1.1'))


# run tests
if __name__ == "__main__":
    main()
