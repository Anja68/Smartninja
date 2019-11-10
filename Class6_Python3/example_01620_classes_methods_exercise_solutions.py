# Read the 2 exercises.
# If you can develop the functionality with test driven development
#
# Part 1)
# add 2 methods to the class Car:
# a) decrease energy, this method decreases the battery status by 1
# b) increase energy, this method increases the battery status by 1
# Part 2)
# create an instance of Car
# demonstrate the functioning of the methods
# by always printing the battery status after applying the methods



class Car(object):
    def __init__(self):
        self.battery_status = 100

    def decrease_energy(self):
        self.battery_status -= 1

    def increase_energy(self):
        self.battery_status += 1


tesla = Car()
print(tesla.battery_status)
tesla.decrease_energy()
print(tesla.battery_status)
tesla.increase_energy()
print(tesla.battery_status)
