import unittest
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def needs_service_test(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def no_service_test(self):
        current_mileage = 29999
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())