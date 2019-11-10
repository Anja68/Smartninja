# Read the 2 exercises.
#
# Part 1)
# add 2 methods to the class Car:
# a) decrease energy, this method decreases the battery status by 1
# b) increase energy, this method increases the battery status by 1
# Part 2)
# create an instance of Car
# demonstrate the functioning of the methods
# by always printing the battery status after applying the methods

#Part 1)

class Car(object):
    def __init__(self, energy):
        self.energy = energy


#a)
    def decrease_battery(self):
        self.energy -= 1

#b)
    def increase_battery(self):
        self.energy += 1

#Part2)

if __name__ == '__main__':
    Volkswagen = Car(100)
    print(Volkswagen.energy)

    Volkswagen.decrease_battery()
    print(Volkswagen.energy)

    Volkswagen.increase_battery()
    print(Volkswagen.energy)

    Volkswagen.increase_battery()
    print(Volkswagen.energy)

