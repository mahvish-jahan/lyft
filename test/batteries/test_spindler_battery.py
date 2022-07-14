import unittest
from datetime import datetime

from battries.spindler_battery import SpindlerBattery


class TestSpindler(unittest.TestCase):

    def test_needs_service_1_year(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        spindler_battery = SpindlerBattery(last_service_date=last_service_date, current_date=today)
        self.assertFalse(spindler_battery.needs_service())

    def test_needs_service_2_year(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        spindler_battery = SpindlerBattery(last_service_date=last_service_date, current_date=today)
        self.assertFalse(spindler_battery.needs_service())

    def test_needs_service_3_year(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        spindler_battery = SpindlerBattery(last_service_date=last_service_date, current_date=today)
        self.assertTrue(spindler_battery.needs_service())