# python -m unittest tests.TestMyClass
import unittest
from src.MyClass import MyClass

class TestMyClass(unittest.TestCase):

    def setUp(self):
        self.myclass = MyClass(7,13)

    def test_do_something(self):
        self.assertEqual(self.myClass.do_something(),20)

if __name__ == "__main__":
    unittest.main()

