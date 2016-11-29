import unittest


class SimplisticTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

"""
In this case, the SimplisticTest has a single test() method,
which would fail if True is ever False

"""
