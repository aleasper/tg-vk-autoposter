import unittest
import os
import sys

from enities.post import Post

class TestPost(unittest.TestCase):

    def test_spam(self):
        post = Post('aboba')
        self.assertEqual(post.spam, False, "Should be not spam")

if __name__ == '__main__':
    unittest.main()