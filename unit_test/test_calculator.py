import unittest
import pythonCode.claculator as Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(10, 10), 20)
        self.assertEqual(Calculator.add(10, -6), 4)
        self.assertEqual(Calculator.add(-10, -6), -16)
    
    def test_sub(self):
        self.assertEqual(Calculator.sub(10, 10), 0)
        self.assertEqual(Calculator.sub(10, -6), 16)
        self.assertEqual(Calculator.sub(-10, -6), -4)
        self.assertEqual(Calculator.sub(-10, 6), -16)
    
    def test_mul(self):
        self.assertEqual(Calculator.mul(10, 10), 100)
        self.assertEqual(Calculator.mul(10, -6), -60)
        self.assertEqual(Calculator.mul(-10, -6), 60)
    
    def test_div(self):
        self.assertEqual(Calculator.div(10, 10), 1)
        self.assertEqual(Calculator.div(12, -6), -2)
        self.assertEqual(Calculator.div(-10, -6), 1)
        self.assertEqual(Calculator.div(10, 0), None)
        self.assertEqual(Calculator.div(0, 10), 0)
        

