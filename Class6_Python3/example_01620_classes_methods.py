class Human(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def get_older(self):
        self.age += 1  # the same as: self.age = self.age + 1

    def get_younger(self):
        self.age -= 1

    def greet(self):
        return "Hello my name is " + self.name + " and i am " + str(self.age) + "."

if __name__ == '__main__':
    alfred = Human(19, "alfred")
    print(alfred.age)  # access attributes with "."
    print(alfred.name)

    alfred.get_older()
    print(alfred.age)
    print(alfred.name)

    print(alfred.greet())

