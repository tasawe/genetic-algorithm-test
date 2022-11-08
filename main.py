from processing_py import *
import classes
import random

CREATURES_N = 10
WATER_N = 30
FIRE_N = 10
DIAMOND_N = 30
app = App(700,700)
app.Mansion = classes.Mansion(app)
app.entities = {classes.Types.MANSION: [app.Mansion], classes.Types.CREATURE: [], classes.Types.WATER: [], classes.Types.DIAMOND: [], classes.Types.FIRE: []}

def addEntity(e):
    app.entities[e.type].append(e)

def genEntity(type, r, x, y, q = 1):
    a = [classes.Creature, classes.Water, classes.Diamond, classes.Fire]
    for i in range(q):
        if r == True:
            x = random.randrange(app.width)
            y = random.randrange(app.height)
        if type == classes.Mansion:
            addEntity(classes.Mansion(app))
        else:
            asd = a[type](x, y)
            addEntity(asd)

def genMap():
    genEntity(classes.Types.CREATURE, True, 0, 0, CREATURES_N)
    genEntity(classes.Types.DIAMOND, True, 0, 0, DIAMOND_N)
    genEntity(classes.Types.FIRE, True, 0, 0, FIRE_N)
    genEntity(classes.Types.WATER, True, 0, 0, WATER_N)

def draw():
    app.background(0,0,0)
    app.ellipseMode('RADIUS')
    for type in app.entities:
        for e in app.entities[type]:
            e.update(app)
            e.draw(app)
    app.redraw()

genMap()

while(True):
    draw()