from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def calculate_travel_time(self, distance):
        pass

    @abstractmethod
    def calculate_travel_cost(self, distance):
        pass


class Car(Vehicle):
    def __init__(self, speed, fuel_consumption, fuel_price):
        self.speed = speed
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price

    def calculate_travel_time(self, distance):
        return distance / self.speed

    def calculate_travel_cost(self, distance):
        return (distance / 100) * self.fuel_consumption * self.fuel_price


class Bicycle(Vehicle):
    def __init__(self, speed, maintenance_cost_per_hour):
        self.speed = speed
        self.maintenance_cost_per_hour = maintenance_cost_per_hour

    def calculate_travel_time(self, distance):
        return distance / self.speed

    def calculate_travel_cost(self, distance):
        return self.calculate_travel_time(distance) * self.maintenance_cost_per_hour


# Пример использования
car = Car(50, 20, 40)
distance = 500
print(f"Время движения на автомобиле: {car.calculate_travel_time(distance)} часов, цена: {car.calculate_travel_cost(distance)}")

bicycle = Bicycle(24, 1)
print(f"Время движения на велосипеде: {bicycle.calculate_travel_time(distance)} часов, цена: {bicycle.calculate_travel_cost(distance)}")