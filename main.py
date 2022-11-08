from processing_py import *
import classes

app = App(600,600)
app.entities = []
app.entities.append(classes.Mansion(app))
app.entities.append(classes.Creature(app.width/2 + 50, app.height/2 + 50))
app.entities.append(classes.Water(app.width/2, app.height/2))
app.entities.append(classes.Diamond(app.width/2 + 50, app.height/2))
app.entities.append(classes.Fire(app.width/2, app.height/2 + 50))
app.ellipseMode('RADIUS')

def draw():
    app.background(0,0,0)
    for e in app.entities:
        e.update(app)
        e.draw(app)
    app.redraw()

while(True):
    draw()