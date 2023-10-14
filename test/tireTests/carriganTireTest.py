import unittest
from tires.carrigan_tires import CarriganTires

class TestCarriganTire(unittest.TestCase):
    def needs_service_test(self):
        tire_wear = [0.2, 0.2, 0.9, 0.4]
        tires  = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def no_service_test(self):
        tire_wear = [0.1, 0.1, 0.1, 0.1]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())