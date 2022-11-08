from processing_py import *
import classes

app = App(600,600)
entities = []
entities.append(classes.Water(app.width/2, app.height/2))

def draw():
    app.background(0,0,0)
    for e in entities:
        e.update(app)
        e.draw(app)
    app.redraw()

while(True):
    draw()