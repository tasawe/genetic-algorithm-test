from processing_py import *
import classes

def addEntity(e):
    app.entities[e.type].append(e)

def draw():
    app.background(0,0,0)
    for type in app.entities:
        for e in app.entities[type]:
            e.update(app)
            e.draw(app)
    app.redraw()

app = App(600,600)
app.Mansion = classes.Mansion(app)
app.entities = {classes.Types.MANSION: [app.Mansion], classes.Types.CREATURE: [], classes.Types.WATER: [], classes.Types.DIAMOND: [], classes.Types.FIRE: []}
addEntity(classes.Creature(app.width/2 + 50, app.height/2 + 50))
addEntity(classes.Water(app.width/2, app.height/2))
addEntity(classes.Diamond(app.width/2 + 50, app.height/2))
addEntity(classes.Fire(app.width/2, app.height/2 + 50))
app.ellipseMode('RADIUS')

while(True):
    draw()