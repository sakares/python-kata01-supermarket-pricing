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

    def test_promotion_three_for_dollar(self):

        self.assertEqual(SuperMarket().cost(3), 1.0,
                         "Expected to have promotion three for a dollar")

    def test_non_promotion(self):

        self.assertEqual(SuperMarket().cost(2), 1.3,
                         "Expected to have promotion three for a dollar")
