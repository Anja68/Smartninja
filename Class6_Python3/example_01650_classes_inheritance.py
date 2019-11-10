class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def greet(self):
        print("Im a person")

class Woman(Person):
    def sing(self):
        print("Lalalala lala")

class Man(Person):
    def greet(self):
        print("I'm a man")

    def dance(self):
        print("Trapp Trapp Trapp")

if __name__ == '__main__':
    p = Person(19,"Karen")
    print(p.age)
    print(p.name)
    p.greet()

    olivia = Woman(20, "Olivia")
    olivia.sing()

    oli = Man(20, "Oli")
    oli.dance()  # man cannot sing, this will cause an error
    oli.greet()
