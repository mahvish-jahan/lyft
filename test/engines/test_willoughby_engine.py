import unittest

from engines.willoughby_engine import WilloughbyEngine


class TestWilloughby(unittest.TestCase):

    def test_needs_service_10000(self):
        last_service_mileage = 5000
        current_mileage = 15000
        caplet_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertFalse(caplet_engine.needs_service())

    def test_needs_service_29999(self):
        last_service_mileage = 5000
        current_mileage = 34999
        capulet_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertFalse(capulet_engine.needs_service())

    def test_needs_service_30000(self):
        last_service_mileage = 5000
        current_mileage = 35000
        caplet_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertFalse(caplet_engine.needs_service())

    def test_needs_service_35000(self):
        last_service_mileage = 5000
        current_mileage = 40000
        caplet_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertFalse(caplet_engine.needs_service())

    def test_needs_service_65000(self):
        last_service_mileage = 5000
        current_mileage = 70000
        caplet_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertTrue(caplet_engine.needs_service())
