class Spot(object):
    def __init__(self, type):
        self.type = type
        self.taken = False

    def can_fit_vehicle(self, type):
        pass

    def remove_vehicle(self):
        pass

    def park_vehicle(self, type):
        pass


class Vehicle(object):
    def __init__(self, type):
        self.type = type

    def clear_spot(self, spot):
        pass

    def can_fit_in_spot(self, spot):
        pass


class Motorcycle(Vehicle):
    def __init(self):
        Vehicle.__init__(self, 1)


class Car(Vehicle):
    def __init(self):
        Vehicle.__init__(self, 2)


class Truck(Vehicle):
    def __init(self):
        Vehicle.__init__(self, 3)


class ParkingLot(object):
    def __init(self, spots):
        self.spots = []

    def park_car(self, car):
        pass

    def remove_car(self, car):
        pass

    def available_spots(self):
        pass