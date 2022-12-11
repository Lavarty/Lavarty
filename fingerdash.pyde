x=100
y=400
def setup():
    size(800,800)
    frameRate(10)
    
def draw():
    global x,y
    clear()
    background(random(0,255),random(0,255),random(0,255))
    img=loadImage("images (1).jpg")
    image(img,x,100,100,100)
    textSize(35)
    text(u"туса пельменей", x,100)

    x=x+2
    
    
    if x>800:
       x=0
    
    
    
    
    
    
    
    
    
    
    
    x=x+2
    
