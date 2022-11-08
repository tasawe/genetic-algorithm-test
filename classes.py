from processing_py import *
from math import sqrt
import random

class Colors():
    RED = 0xFFFF0000
    GREEN = 0xFF00FF00
    BLUE = 0xFF0000FF
    BLACK = 0xFF000000
    WHITE = 0xFFFFFFFF # creature
    YELLOW = 0xFFFFFF00 # creature carries diamond
    DIAMOND = 0xFF00CCFF
    WATER = 0xFF4D4DFF
    FIRE = 0xFFFF6600
    MANSION = 0xFFCC0099

class Types():
    CREATURE = 0
    WATER = 1
    DIAMOND = 2
    FIRE = 3
    MANSION = 4

class Neuron():
    def __init__(self, inputs):
        self.inputs = inputs
    def getOutput(self):
        r = 0
        for input in self.inputs:
            r += input() * self.inputs[input]
        return r
    def genRandomInputWeights(creature, layer):
        if layer == 1:
            return {creature.getWater: random.randrange(10), creature.getFire: random.randrange(10), creature.getMansion: random.randrange(10), creature.getDiamond: random.randrange(10), creature.getHasDiamond: random.randrange(10)}
        elif layer == 2:
            r = {}
            for n in creature.neuronsLayer1:
                r[n.getOutput] = random.randrange(10)
            return r

class Entity():
    def __init__(self, x, y, radius, color, type):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.type = type
    def update(self, app):
        pass
    def inside(self, x, y):
        return sqrt((x-self.x)*(x-self.x) + (y-self.y)*(y-self.y)) <= self.radius
    def collide():
        pass
    def draw(self, app):
        app.fill(self.color)
        app.ellipse(self.x, self.y, self.radius, self.radius)

class Water(Entity):
    def __init__(self, x, y):
        self.radius = 20
        self.color = Colors.WATER
        super().__init__(x, y, self.radius, self.color, Types.WATER)

class Diamond(Entity):
    def __init__(self, x, y):
        self.radius = 15
        self.color = Colors.DIAMOND
        super().__init__(x, y, self.radius, self.color, Types.DIAMOND)

class Fire(Entity):
    def __init__(self, x, y):
        self.radius = 20
        self.color = Colors.FIRE
        super().__init__(x, y, self.radius, self.color, Types.FIRE)

class Mansion(Entity):
    def __init__(self, app):
        self.x = app.width/2
        self.y = app.height/2
        self.color = Colors.MANSION
        self.type = Types.MANSION
        self.radius = 90
        self.stroke = 5
        self.innerRadius = self.radius - self.stroke
    def draw(self, app):
        app.fill(self.color)
        app.ellipse(self.x, self.y, self.radius, self.radius)
        app.fill(Colors.BLACK)
        app.ellipse(self.x, self.y, self.innerRadius, self.innerRadius)

class Creature(Entity):
    def __init__(self, x, y):
        self.radius = 15
        self.caughtDiamonds = 0
        self.carriesDiamond = False
        self.color = Colors.WHITE
        super().__init__(x, y, self.radius, self.color, Types.CREATURE)
        self.neuronsLayer1 = []
        self.neuronsLayer2 = []
        for i in range(4):
            self.neuronsLayer1.append(Neuron(Neuron.genRandomInputWeights(self, 1)))
        for i in range(3):
            self.neuronsLayer2.append(Neuron(Neuron.genRandomInputWeights(self, 2)))
    def getWater():
        pass
    def getFire():
        pass
    def getMansion():
        pass
    def getDiamond():
        pass
    def getHasDiamond(self):
        return int(self.carriesDiamond)
    def update(self, app):
        self.color = Colors.YELLOW if self.carriesDiamond else Colors.WHITE
        if (app.Mansion.inside(self.x, self.y)):
            self.carriesDiamond = False
            self.caughtDiamonds += 1