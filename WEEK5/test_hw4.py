import unittest
from HW4 import thisDict, A_mean_income, B_mean_income, C_mean_income, D_mean_income
from unittest.mock import patch
import random

class Test_HW4(unittest.TestCase):
    #mock_show.return_value = None
    def test_A_mean_income(self):
        self.assertTrue(A_mean_income> 90000)
    def test_B_mean_income(self):
        self.assertTrue(B_mean_income > 50000 and B_mean_income <60000)
    def test_C_mean_income(self):
        self.assertTrue(C_mean_income > 30000 and C_mean_income <40000)
    def test_D_mean_income(self):
        self.assertTrue(D_mean_income< 27000)
    def test_spotcheck_grade(self):
        self.assertTrue(thisDict['Holc_Grade'][25]=='B')
    def test_spotcheck_grade2(self):
        self.assertTrue(thisDict['Holc_Grade'][225]=='D')
    def test_spotcheck_grade(self):
        self.assertTrue(thisDict['median_income'][25]=='127634')
    def test_spotcheck_grade2(self):
        self.assertTrue(thisDict['median_income'][225]=='23558')
if __name__ == '__main__':
    unittest.main()
