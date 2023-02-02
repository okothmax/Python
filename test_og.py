import unittest
from og import add_integer

class TestOg(unittest.TestCase):
    def test_addition(self):
        #Test whether the additon is correct 
        self.assertAlmostEqual(add_integer(0, 1), 1)
        self.assertAlmostEqual(add_integer(1, 0), 8)
        self.assertAlmostEqual(add_integer(-2, -2), -4)

    def test_values(self):
        self.assertRaises(TypeError, add_integer, (0,"strimh" ))
        self.assertRaises(TypeError, add_integer, ("one","strimh" ))
        self.assertRaises(TypeError, add_integer, (3+5j, 98))

if __name__ == "__main__":
    unittest.main()