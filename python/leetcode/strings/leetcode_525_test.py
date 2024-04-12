# problem - https://leetcode.com/problems/encode-and-decode-tinyurl/description/
# tags - string, hash-table, hash-function, design


from unittest import TestCase


# Codec Class
class Codec:

    # define constructor
    def __init__(self) -> None:
        # create a counter to count the number of long URL has been shorten
        self.__counter: int = 0

        # define a map to store the mapping of short URLs
        self.__short_urls: dict[str, int] = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        # check if a mapping for the given long URl does not exists
        if longUrl not in self.__short_urls:
            # increment the counter by 1
            self.__counter += 1

            # map the counter to the given long URL
            self.__short_urls[longUrl] = self.__counter

        # return the existing short URL
        return str(object=self.__short_urls[longUrl])

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        # iterate over the mapping and return the long URL corresponding to the short URL given
        return next(
            (__key for __key, __value in self.__short_urls.items() if __value == int(shortUrl)),
              '')


# Test Class
class TestLeetCode535(TestCase):

    def test_encode_decode(self) -> None:
        # create instance of the Codec class
        __codec = Codec()

        # tests
        self.assertEqual(first='https://leetcode.com/problems/design-tinyurl',
                         second=__codec.decode(shortUrl=__codec.encode(
                             longUrl='https://leetcode.com/problems/design-tinyurl'))
                        )
        self.assertEqual(first='http://www.leetcode.com/faq/?id=10',
                         second=__codec.decode(shortUrl=__codec.encode(
                             longUrl='http://www.leetcode.com/faq/?id=10'))
                        )
