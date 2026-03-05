"""
The assert keyword is used when debugging code.

The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.

You can write a message to be written if the code returns False, check the example below
"""
"""x = "hello"
assert x == "goodbye"""
"""
assertEqual() is a function from Python's unittest library used for unit testing
It checks whether two values are equal and returns a boolean result based on the condition
If both values are equal, the test passes otherwise it fails and raises an AssertionError with an optional error message
"""
import unittest

class TestNegative(unittest.TestCase):
    
    def test_fun(self):
        # Failing test: comparing different strings
        self.assertEqual("geeks", "gfg", "'geeks' is not equal to 'gfg'.")

if __name__ == '__main__':
    unittest.main()
    
