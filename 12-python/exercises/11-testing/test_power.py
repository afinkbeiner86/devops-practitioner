"""
Test module for power.py
"""

import pytest
import unittest
from power import power_num


class TestPower(unittest.TestCase):
    """
    Test the function power_num from module power.py
    """

    # def test_power_int(self):
    #     self.assertEqual(power_num(2, 3), 8)

    # def test_power_float(self):
    #     self.assertEqual(power_num(1.5, 2), 2.25)

    def test_for_list_as_number(self):
        with self.assertRaises(TypeError):
            power_num([], 2)
    
    def test_for_float_as_power(self):
        with self.assertRaises(TypeError):
            power_num(2, 2.5)
    
    def test_for_negative_numbers(self):
        with self.assertRaises(TypeError):
            power_num(-6, 2)

# pytest
def test_power_int():
    assert power_num(2, 3) == 8

def test_power_float():
    assert power_num(1.5, 2) == 2.25




if __name__ == '__main__':
    unittest.main()
