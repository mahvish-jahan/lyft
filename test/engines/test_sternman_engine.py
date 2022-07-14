import unittest

from engines.sternman_engine import SternmanEngine


class TestSternman(unittest.TestCase):

    def test_needs_service_light_on(self):
        warning_light_on = True
        sternman_engine = SternmanEngine(warning_light_on)
        self.assertTrue(sternman_engine.needs_service())

    def test_needs_service_light_off(self):
        warning_light_on = False
        sternman_engine = SternmanEngine(warning_light_on)
        self.assertFalse(sternman_engine.needs_service())
