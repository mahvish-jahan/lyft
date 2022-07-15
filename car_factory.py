from battries.nubbin_battery import NubbinBattery
from car import Car
from engines.capulet_engine import CapuletEngine
from battries.spindler_battery import SpindlerBattery
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory:
    
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, arr):

        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(arr)

        car = Car(engine, battery, tires)

        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, arr):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(arr)

        car = Car(engine, battery, tires)

        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, arr):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(arr)

        car = Car(engine, battery, tires)

        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, arr):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(arr)

        car = Car(engine, battery, tires)

        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, arr):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(arr)

        car = Car(engine, battery, tires)

        return car
