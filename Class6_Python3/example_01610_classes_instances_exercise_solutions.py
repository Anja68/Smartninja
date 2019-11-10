class Robot(object):
    def __init__(self, model, mission):
        self.model = model
        self.mission = mission

# create 1 instance of Robot
# give it a the model "HAL9000"
# give it the mission "protect humans"
# print its model
# print its mission


if __name__ == '__main__':
    iRobot=Robot("HAL9000", "protect humans")
    print(iRobot.model)
    print(iRobot.mission)
