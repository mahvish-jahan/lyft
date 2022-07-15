import unittest

from tires.carrigan_tires import CarriganTires


class TestCarriageTires(unittest.TestCase):

    def test_needs_service_true(self):
        arr = [0.1, 0.5, 0.8, 0.9]
        carriage_tires = CarriganTires(arr)
        self.assertTrue(carriage_tires.needs_service())

    def test_needs_service_false(self):
        arr = [0.1, 0.5, 0.8, 0.8]
        carriage_tires = CarriganTires(arr)
        self.assertFalse(carriage_tires.needs_service())
