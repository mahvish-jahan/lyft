from battries.nubbin_battery import NubbinBattery
from battries.splinder_battery import Battery
from car import Car
from engines.capulet_engine import CapuletEngine
from battries.splinder_battery import SpindlerBattery
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine


class CarFactory:
    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)

        car = Car(engine, battery)

        return car

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)

        car = Car(engine, battery)

        return car

    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)

        car = Car(engine, battery)

        return car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)

        car = Car(engine, battery)

        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)

        car = Car(engine, battery)

        return car