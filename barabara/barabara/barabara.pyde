bg=0;
x=300
y=300
r=0
g=250
b=189
seze = 20
def setup():
    size(1240,820)
    frameRate(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
def draw():
    global x,y, r,g,b, seze

    fill(r, g, b)
    ellipse(mouseX,mouseY,seze,seze)
    
    rect(300,500,100,100)
    push()
    fill(255,0,0)
    rect(200,500,100,100)
    pop()
    
    push()
    fill(255,0,200)
    rect(100,500,100,100)
    pop()
    
    push()
    fill(0)
    rect(0,500,100,100)
    pop()
    
def mouseClicked():
    global x,y,r,g,b,seze
    if mouseX > 300 and mouseX < 400 and mouseY > 500 and mouseY < 600:
        r=random(0,255)
        g=random(0,255)
        b=random(0,255)
        
    if mouseX > 200 and mouseX < 300 and mouseY > 500 and mouseY < 600:
        clear()
        background(160)
    
    if mouseX > 100 and mouseX < 200 and mouseY > 500 and mouseY < 600:
        seze+=50
        
    if mouseX > 0 and mouseX < 100 and mouseY > 500 and mouseY < 600:
        seze-=50
#rgb(163, 196, 31)
