class VehicleManager(object):
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def print_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle.print_description())


class Vehicle(object):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def print_description(self):
        return f"Vehicle(brand={self.brand}, model={self.model})"

if __name__ == '__main__':
    manager = VehicleManager()
    ferrari = Vehicle("Ferrari", "Spider")
    manager.add_vehicle(ferrari)
    manager.add_vehicle(Vehicle("Mazda", "KA"))
    manager.print_vehicles()
