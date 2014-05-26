import unittest
import sys

sys.path.append("../")
from lib.supermarket import SuperMarket

class TestSuperMarket(unittest.TestCase):
    """ TestSuperMarket class """
    
    def setUp(self):
      
      self.can_of_bean_prices = 0.65
      
    def test_can_of_beans_cost(self):
      
      self.assertEqual(SuperMarket().get_can_of_bean_prices(), 0.65,
                         "Incorrect Prices")