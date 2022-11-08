from processing_py import *

class Colors():
    BLUE = 0xFF0000FF

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
    def draw(self, app):
        app.fill(self.color)
        app.ellipse(self.x, self.y, self.radius, self.radius)

class Water(Entity):
    def __init__(self, x, y):
        self.radius = 25
        super().__init__(x, y, self.radius, Colors.BLUE)