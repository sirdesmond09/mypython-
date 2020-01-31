# def greet_user(name):
#     print(f'Hi {name}')
#     print ("welcome aboard")

# print ("start")
# greet_user(input("Enter your name: "))


# CLASSES
class Robot:
    def __init__(self, n, c, w):
        self.name =n
        self.color =c
        self.weight =w

    def introduce_self(self):
        print (f"My name is {self.name}")
        print (f"I have {self.color} colour")
r1 = Robot("Tom" , "Blue", 27)
r2 = Robot ("Jerry", "blue", 88)

class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i
    
    
    def sit_down(self):
        is_sitting = True
    
    
    def stand_up (self):
        is_sitting = False


p1 = Person("Alice", "Agressive", False)
p2 = Person("Becky", "Talkative", True)
#To show that p1 owns r2 and vice versa
p1.robot_owned = r2
p2.robot_owned = r1


# importing modules
import random
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

dice = Dice()
print (dice.roll())

from ecommerce import shipping

print(shipping.calc_shipping())


from pathlib import Path
path = Path()
for file in path.glob("*"):
    print (file)

    