from abc import ABC
from enum import Enum
from typing import List,Optional
from datetime import datetime
from threading import Lock

class VehicleType(Enum):
    CAR=1
    MOTORCYCLE=2
    TRUCK=3

class Vehicle(ABC):
    def __init__(self,license_plate:str,vehicle_type:VehicleType):
        self.license_plate=license_plate
        self.type=vehicle_type

    def get_type(self):
        return self.type

class Car(Vehicle):
    def __init__(self,license_plate:str):
        super().__init__(license_plate,VehicleType.CAR)


class MotorCycle(Vehicle):
    def __init__(self,license_plate:str):
        super().__init__(license_plate,VehicleType.MOTORCYCLE)


class Truck(Vehicle):
    def __init__(self,license_plate:str):
        super().__init__(license_plate,VehicleType.TRUCK)

class ParkingSpot:
    def __init__(self,spot_no:int,vehicle_type:VehicleType,hourly_rate:float):
        self.spot_no=spot_no
        self.vehicle_type=vehicle_type
        self.parked_vehicle:Optional[Vehicle]=None
        self.hourly_rate=hourly_rate

    def is_available(self):
        return self.parked_vehicle is None #none means spot is empty
    
    def park_vehicle(self,vehicle:Vehicle):
        if self.is_available() and vehicle.get_type()==self.vehicle_type:
            self.parked_vehicle=vehicle
            return True
        else:
            raise ValueError('Invalid Vehicle Type or Spot alreay taken')
        
    def unpark_vehicle(self):
        self.parked_vehicle=None

    def get_hourly_rate(self):
        return self.hourly_rate
    
class ParkingTicket:
    def __init__(self,vehicle:Vehicle,spot:ParkingSpot):
        self.vehicle=vehicle
        self.spot=spot
        self.entry_time=datetime.now()
        self.exit_time:Optional[datetime]=None

    def calculate_fee(self):
        if self.exit_time is None:
            raise ValueError('Ticket is still open')
        duration=(self.exit_time-self.entry_time).seconds/3600
        return round(duration*self.spot.get_hourly_rate(),2)
    
class PaymentProcessor:
    @staticmethod
    def process_payment(ticket:ParkingTicket):
        fee=ticket.calculate_fee()
        print(f"Processing payment of ${fee} for vehicle {ticket.vehicle.license_plate}.")


class Level:
    def __init__(self,floor:int,num_spots:int):
        self.floor=floor
        #It ensures that every level starts with a collection of spots ready for use.
        self.parking_spots:List[ParkingSpot]=[
            ParkingSpot(i,VehicleType.CAR,5.0) for i in range(num_spots)
        ]

    def park_vehicle(self,vehicle:Vehicle):
        for spot in self.parking_spots:
            if spot.is_available() and spot.vehicle_type==vehicle.get_type():
                success=spot.park_vehicle(vehicle)
                return success
        return False
    
    def unpark_vehicle(self,vehicle:Vehicle):
        for spot in self.parking_spots:
            if spot.parked_vehicle==vehicle:
                spot.unpark_vehicle()
                return True
        return False
    
    def display_availibility(self):
        print(f'Level{self.floor} Availibilty')
        for spot in self.parking_spots:
            status='Available' if spot.is_available() else 'ocuupied'
            print(f'Spot {spot.spot_no}:{status}')


class ParkingLot:
    _instance=None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception('This class is a singelton')
        else:
            ParkingLot._instance=self
            self.levels:list[Level]=[]
            self.lock=Lock()

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance

    def add_level(self,level:Level):
        self.levels.append(level)

    def park_vehicle(self,vehicle:Vehicle):
        with self.lock:
            for level in self.levels:
                if level.park_vehicle(vehicle):
                    return True
            return False
        
    def unpark_vehicle(self,vehicle:Vehicle):
        with self.lock:
            for level in self.levels:
                if level.unpark_vehicle(vehicle):
                    return True
            return False
        
    def display_availibilty(self):
        for level in self.levels:
            level.display_availibility()


class ParkingLotDemo:
    @staticmethod
    def run():
        parking_lot=ParkingLot.get_instance()
        parking_lot.add_level(Level(1,10))
        parking_lot.add_level(Level(2,8))

        car=Car('ABC124')
        motocyce=MotorCycle('9056')
        truck=Truck('09sdf')
        parking_lot.display_availibilty()

        parking_lot.park_vehicle(car)
        #parking_lot.park_vehicle(motocyce)
       # parking_lot.park_vehicle(truck)

        #display avl

        parking_lot.display_availibilty()

        #unaprk vehicle
       # parking_lot.unpark_vehicle(truck)

        #now display avl

        #parking_lot.display_availibilty()

if __name__=='__main__':
    ParkingLotDemo.run()


