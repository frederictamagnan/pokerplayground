import unittest

"""
https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory/15630454

"""

class TestPlayground(unittest.TestCase):
    def test_something(self):
        # self.assertEqual(True, False)
        self.assertEqual(True,True)

if __name__ == '__main__':
    unittest.main()
