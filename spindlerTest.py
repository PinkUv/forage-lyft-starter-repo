import unittest
from battery.spindler_battery import SpindlerBattery
from datetime import date

class TestSpindlerBattery(unittest.TestCase):
    def needs_service_test(self):
        current_date = date.fromisoformat("2023-05-1")
        last_service_date = date.fromisoformat("2018-01-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def no_service_test(self):
        current_date = date.fromisoformat("2023-01-20")
        last_service_date = date.fromisoformat("2012-01-1")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())