import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from motorbike import *

class TestMotorbike(unittest.TestCase):
    def setUp(self):
        self.motorbike = Motorbike()

    def test_motorbike_can_start_engine(self):
        self.assertEqual("Vrrmmm (I'm a motorbike), HELL YEAH!", self.motorbike.start())

if __name__ == "__main__":
    unittest.main()