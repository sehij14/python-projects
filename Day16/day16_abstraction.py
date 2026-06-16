# Day 16 Project
# Smart Vehicle Management System

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car starts using key")

    def stop(self):
        print("Car stopped")

class Bike(Vehicle):

    def start(self):
        print("Bike starts using self-start")

    def stop(self):
        print("Bike stopped")

class Truck(Vehicle):

    def start(self):
        print("Truck engine started")

    def stop(self):
        print("Truck stopped")

car1 = Car()

car2 = Car()

bike1 = Bike()

truck1 = Truck()

car1.start()
car1.stop()

car2.start()
car2.stop()

bike1.start()
bike1.stop()

truck1.start()
truck1.stop()