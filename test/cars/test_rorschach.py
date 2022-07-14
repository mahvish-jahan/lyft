import unittest
from datetime import datetime

from car import Car


class TestRorschach(unittest.TestCase):

    def test_rorschach_1(self):
        from engines.willoughby_engine import WilloughbyEngine
        from battries.nubbin_battery import NubbinBattery

        last_service_mileage = 5000
        current_mileage = 15000
        caplet_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)

        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        nubbin_battery = NubbinBattery(last_service_date=last_service_date, current_date=today)

        car = Car(engine=caplet_engine, battery=nubbin_battery)
        self.assertTrue(car.needs_service())

    def test_rorschach_2(self):
        from engines.willoughby_engine import WilloughbyEngine
        from battries.nubbin_battery import NubbinBattery

        last_service_mileage = 5000
        current_mileage = 15000
        caplet_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)

        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        nubbin_battery = NubbinBattery(last_service_date=last_service_date, current_date=today)

        car = Car(engine=caplet_engine, battery=nubbin_battery)
        self.assertFalse(car.needs_service())
    def test_rorschach_3(self):
        from engines.willoughby_engine import WilloughbyEngine
        from battries.nubbin_battery import NubbinBattery

        last_service_mileage = 5000
        current_mileage = 15000
        caplet_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)

        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        nubbin_battery = NubbinBattery(last_service_date=last_service_date, current_date=today)

        car = Car(engine=caplet_engine, battery=nubbin_battery)
        self.assertTrue(car.needs_service())