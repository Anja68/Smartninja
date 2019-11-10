# create classes for social account
# they have a field for: name, friends
# they have methods to: count_friends, befriend, unfriend

class SocialAccount(object):
    def __init__(self, name):
        self.name = name
        self.friends = []

    def count_friends(self):
        return len(self.friends)

    def befriend(self, account):
        self.friends.append(account)

    def unfriend(self, account):
        self.friends.remove(account)

class Profile(SocialAccount):
    def what(self):
        return 0

p=Profile("hello")
#print(p.name)


friedrich = SocialAccount("Friedrich")
tobi = SocialAccount("Tobi")
lobi = SocialAccount("Lobi")
jobi = SocialAccount("Jobi")

print(friedrich.count_friends())
friedrich.befriend(tobi)
friedrich.befriend(lobi)
friedrich.befriend(jobi)

print(friedrich.count_friends())

for friend in friedrich.friends:
    print(friend.name)

friedrich.unfriend(jobi)
print("=" * 30)
for friend in friedrich.friends:
    print(friend.name)
