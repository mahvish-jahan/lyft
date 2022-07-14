import unittest

from engines.capulet_engine import CapuletEngine


class TestCapulet(unittest.TestCase):

    def test_needs_service_10000(self):
        last_service_mileage = 5000
        current_mileage = 15000
        caplet_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertFalse(caplet_engine.needs_service())

    def test_needs_service_29999(self):
        last_service_mileage = 5000
        current_mileage = 34999
        capulet_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertFalse(capulet_engine.needs_service())

    def test_needs_service_30000(self):
        last_service_mileage = 5000
        current_mileage = 35000
        caplet_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertTrue(caplet_engine.needs_service())

    def test_needs_service_35000(self):
        last_service_mileage = 5000
        current_mileage = 40000
        caplet_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertTrue(caplet_engine.needs_service())