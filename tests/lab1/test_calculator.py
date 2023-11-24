import unittest

from src.lab1.calculator import solve


class CalculatorTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solve('5+5'), 10)
        self.assertEqual(solve('5/2.0'), 2.5)
        self.assertEqual(solve('51.2+44.5/5.0'), 60.1)
        self.assertEqual(solve('2+2*2'), 6)
