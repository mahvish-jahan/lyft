import unittest
from datetime import datetime

from battries.nubbin_battery import NubbinBattery


class TestNubbin(unittest.TestCase):

    def test_needs_service_3_year(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        nubbin_battery = NubbinBattery(last_service_date=last_service_date, current_date=today)
        self.assertFalse(nubbin_battery.needs_service())

    def test_needs_service_4_year(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        nubbin_battery = NubbinBattery(last_service_date=last_service_date, current_date=today)
        self.assertFalse(nubbin_battery.needs_service())

    def test_needs_service_5_year(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        nubbin_battery = NubbinBattery(last_service_date=last_service_date, current_date=today)
        self.assertTrue(nubbin_battery.needs_service())
