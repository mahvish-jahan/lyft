import unittest
from datetime import datetime

from car import Car


class TestPalindrom(unittest.TestCase):

    def test_palindrome_1(self):
        from engines.sternman_engine import SternmanEngine
        from battries.spindler_battery import SpindlerBattery

        warning_light_on = True
        sternman_engine = SternmanEngine(warning_light_on=warning_light_on)

        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        spindler_battery = SpindlerBattery(last_service_date=last_service_date, current_date=today)

        car = Car(engine=sternman_engine, battery=spindler_battery)
        self.assertTrue(car.needs_service())

    def test_palindrome_2(self):
        from engines.sternman_engine import SternmanEngine
        from battries.spindler_battery import SpindlerBattery

        warning_light_on = False
        caplet_engine = SternmanEngine(warning_light_on=warning_light_on)

        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        spindler_battery = SpindlerBattery(last_service_date=last_service_date, current_date=today)

        car = Car(engine=caplet_engine, battery=spindler_battery)
        self.assertFalse(car.needs_service())

    def test_palindrome_3(self):
        from engines.sternman_engine import SternmanEngine
        from battries.spindler_battery import SpindlerBattery

        warning_light_on = False
        caplet_engine = SternmanEngine(warning_light_on=warning_light_on)

        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        spindler_battery = SpindlerBattery(last_service_date=last_service_date, current_date=today)

        car = Car(engine=caplet_engine, battery=spindler_battery)
        self.assertTrue(car.needs_service())
