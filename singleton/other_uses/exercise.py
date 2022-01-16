import unittest
from copy import deepcopy

def is_singleton(factory):
    x = factory()
    y = factory()
    return x is y

class Evaluate(unittest.TestCase):
    def test_exercise(self):
        obj = [1, 2, 3]
        self.assertTrue(is_singleton(lambda: obj))
        self.assertFalse(is_singleton(lambda: deepcopy(obj)))

if __name__ == '__main__':
    unittest.main()