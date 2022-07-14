import unittest
from datetime import datetime

from car import Car


class TestCalliope(unittest.TestCase):

    def test_calliope_1(self):
        from engines.capulet_engine import CapuletEngine
        from battries.spindler_battery import SpindlerBattery

        last_service_mileage = 5000
        current_mileage = 15000
        caplet_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)

        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        spindler_battery = SpindlerBattery(last_service_date=last_service_date, current_date=today)

        car = Car(engine=caplet_engine, battery=spindler_battery)
        self.assertTrue(car.needs_service())

    def test_calliope_2(self):
        from engines.capulet_engine import CapuletEngine
        from battries.spindler_battery import SpindlerBattery

        last_service_mileage = 5000
        current_mileage = 15000
        caplet_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)

        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        spindler_battery = SpindlerBattery(last_service_date=last_service_date, current_date=today)

        car = Car(engine=caplet_engine, battery=spindler_battery)
        self.assertFalse(car.needs_service())

    def test_calliope_3(self):
        from engines.capulet_engine import CapuletEngine
        from battries.spindler_battery import SpindlerBattery

        last_service_mileage = 5000
        current_mileage = 40000
        caplet_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)

        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        spindler_battery = SpindlerBattery(last_service_date=last_service_date, current_date=today)

        car = Car(engine=caplet_engine, battery=spindler_battery)
        self.assertTrue(car.needs_service())
