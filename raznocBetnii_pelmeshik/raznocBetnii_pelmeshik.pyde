x=100
y=100

def setup():
    size(600,600)
    
def draw():
    global x,y
    clear()
    ellipse(300,300,x,y)
    
    if keyPressed:
        
        if key == "w" or key == "W":
            x+=2
            fill(255,0,0)
        if key == "s" or key == "S":
            y+=2
            fill(0,57,255)
        if key == "q" or key == "Q":
            x-=2
            fill(0,255,48)
        if key == "e" or key == "E":
            y-=2
            fill(246,255,0)
