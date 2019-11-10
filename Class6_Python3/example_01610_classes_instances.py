class Human(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name


if __name__ == '__main__':
    x = Human(19, "alfred")
    print(x.age)  # access attributes with "."
    print(x.name)

    beatrix = Human(22, "beatrix")
    print(beatrix.age)
    print(beatrix.name)
