from processing_py import *
from math import sqrt

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

class Neuron():
    def __init__(self, inputs):
        self.inputs = inputs
    def getOutput(self):
        r = 0
        for (input, weight) in self.inputs:
            r += input * weight
        return r

class Entity():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
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
        self.radius = 25
        self.color = Colors.WATER
        super().__init__(x, y, self.radius, self.color)

class Diamond(Entity):
    def __init__(self, x, y):
        self.radius = 20
        self.color = Colors.DIAMOND
        super().__init__(x, y, self.radius, self.color)

class Fire(Entity):
    def __init__(self, x, y):
        self.radius = 25
        self.color = Colors.FIRE
        super().__init__(x, y, self.radius, self.color)

class Mansion(Entity):
    def __init__(self, app):
        self.x = app.width/2
        self.y = app.height/2
        self.color = Colors.MANSION
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
        self.radius = 30
        self.carriesDiamond = False
        self.color = Colors.WHITE
        super().__init__(x, y, self.radius, self.color)
    def update(self, app):
        self.color = Colors.YELLOW if self.carriesDiamond else Colors.WHITE
        if (self.inside(app.mouseX, app.mouseY)):
            self.carriesDiamond = True
        else:
            self.carriesDiamond = False