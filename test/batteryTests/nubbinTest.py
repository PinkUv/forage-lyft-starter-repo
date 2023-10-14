import unittest
from battery.nubbin_battery import NubbinBattery
from datetime import date

class TestNubbinBattery(unittest.TestCase):
    def need_service_test(self):
        current_date = date.fromisoformat("2023-10-13")
        last_service_date = date.fromisocalendar("2018-12-30")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def no_service_test(self):
        current_date = date.fromisoformat("2023-10-13")
        last_service_date = date.fromisocalendar("2022-6-20")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
