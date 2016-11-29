import unittest


class FailureMessageTest(unittest.TestCase):

    def test_fail(self):
        self.assertTrue(False, 'This is the error message')


if __name__ == '__main__':
    unittest.main()
