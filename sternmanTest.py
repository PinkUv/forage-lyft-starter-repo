import unittest
from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def needs_service_test(self):
        warning_light= True
        engine = SternmanEngine(warning_light)
        self.assertTrue(engine.needs_service())

    def no_service_test(self):
        warning_light= False
        engine = SternmanEngine(warning_light)
        self.assertFalse(engine.needs_service())