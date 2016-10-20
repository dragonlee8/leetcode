import unittest
from wildcard import Solution

class TestWildCard(unittest.TestCase):
    so = Solution()
    def test1(self):
        self.assertEqual(self.so.isMatch('aa', 'aa'), True)
        self.assertEqual(self.so.isMatch('*', '*'), True)
        self.assertEqual(self.so.isMatch('', ''), True)
        self.assertEqual(self.so.isMatch('', '*'), True)
        self.assertEqual(self.so.isMatch('', '**'), True)
        self.assertEqual(self.so.isMatch('a', ''), False)
        self.assertEqual(self.so.isMatch('aa', '*'), True)
        self.assertEqual(self.so.isMatch('aa', '??'), True)
        self.assertEqual(self.so.isMatch('aa', 'a?'), True)
        self.assertEqual(self.so.isMatch('aa', 'a*'), True)
        self.assertEqual(self.so.isMatch('aa', 'a**'), True)
        self.assertEqual(self.so.isMatch('ab', 'ab'), True)
        self.assertEqual(self.so.isMatch('a', 'a'), True)
        self.assertEqual(self.so.isMatch('a', 'a*'), True)
        self.assertEqual(self.so.isMatch('a', 'a**'), True)
        self.assertEqual(self.so.isMatch('aba', 'a*a'), True)
        self.assertEqual(self.so.isMatch('aba', 'a*ba'), True)
        self.assertEqual(self.so.isMatch('abaa', 'a*a'), True)
        self.assertEqual(self.so.isMatch('a', 'a*a'), False)
        self.assertEqual(self.so.isMatch('a', 'a?'), False)
        self.assertEqual(self.so.isMatch('a', 'ba'), False)
        self.assertEqual(self.so.isMatch('a', 'ab'), False)
        self.assertEqual(self.so.isMatch('ab', '*a'), False)
        self.assertEqual(self.so.isMatch('b', 'a'), False)

unittest.main()


