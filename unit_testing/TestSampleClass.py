import unittest
from python_programming.SampleTestClass  import Calculator



class TestSampleClass(unittest.TestCase):
    def test_add_functionality(self):
        calc1 = Calculator(10,20)
        result = calc1.calc_add()
        self.assertEqual(result,30)
