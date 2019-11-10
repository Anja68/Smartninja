class Robot:
    def __init__(self, model, mission, color="None"):
        self.model = model
        self.mission = mission
        self.favfood = favfood
        self.age = age
        self.color = color

    def __str__(self):
        return f"Robot(model={self.model}, mission{self.mission}, color={self.color})"

# create 1 instance of Robot
# give it a the model "HAL9000"
# give it the mission "protect humans"
# print its model
# print its mission

my_robot = Robot("HAL9000", "protect humans", "Pizza", "100")
print(my_robot.model)
print(my_robot.mission)

my_robot = Robot("HAL9000", "protect humans")
my_robot1 = Robot("HAL9000", "protect humans", "pink")
my_robot2 = Robot("HAL9000", "protect humans", "Orange")

print(my_robot.color, my_robot1.color, my_robot2.color)


