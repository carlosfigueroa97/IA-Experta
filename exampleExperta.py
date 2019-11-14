from random import choice
from experta import *

class Light(Fact):
    pass

class RobotCrossStreet(KnowledgeEngine):
    @Rule(Light(color='green'))
    def green_light(self):
        print("Walk")

    @Rule(Light(color='red'))
    def red_light(self):
        print("Don't walk")

    @Rule(AS.light << Light(color=L('yellow') | L('blinking-yellow')))
    def cautious(self, light):
        print("Be cautious because light is", light["color"])

engine = RobotCrossStreet()
engine.reset()
engine.declare(Light(color=choice(['green','yellow','blinking-yellow','red'])))
engine.run()