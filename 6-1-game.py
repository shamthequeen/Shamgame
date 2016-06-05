#Zeynep,Sham
#Candy chaos
from pygame import *
from random import randint
from math import *


panx,pany=150,450
myClock = time.Clock()
running = True
onground=True
panvy=2 #volocity of panther/gravity
points=0
life=5
jump=False
available=1
taken=0


#Colours
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
lightblue=(92,245,255)
yellow=(248,236,7)

init()
screen = display.set_mode((1000,500))
display.set_caption("Candy Chaos")

#background
bgpic = image.load("wallpaper6.jpg")

#ground
grpic=image.load("ground2.png")#ground pic
grpic=transform.smoothscale(grpic,(550,45))

#start
stpic = image.load("start.png")
stpic=transform.smoothscale(stpic,(90,210))







"""#for messaegs on screen#work on later
font=font.SysFont(None,25)
def message_to_screen(msg,colour):
    screen_text=font.render(msg,True,colour)
    screen.blit(screen_text,[display_width/2,display_height/2])
"""

def drawBG():#Draws game at currect state
    screen.blit(bgpic,(-panx,0))#items are left behind(in negative position)
    screen.blit(stpic,(-panx+150,280))

#candies
         #x  #y  #l #w 
candylis=[(500,400,50,30),(600,310,50,30),(700,200,50,30),(800,320,50,30)]#list of ground locations and height & width
candy=[]
for i in range(len(candylis)):
    candy.append(available)

canpic=image.load("can1.png")
canpic=transform.smoothscale(canpic,(50,30))

def collectgoodies():#(item):
    #global item
    global candy, points, pic, candylis
    panrect=Rect(panx,pany-pic.get_height(),pic.get_width(),pic.get_height())
    for goodies in candylis:
        canx=goodies[0]
        cany=goodies[1]
        canl=goodies[2]
        canw=goodies[3]
        if Rect(-panx+canx,cany,canl,canw).colliderect(panrect):
            points+=1
            candy[candylis.index(goodies)]==taken
            candylis.remove(goodies)

def drawgoodies():
    for goodies in candylis:
        canx=goodies[0]
        cany=goodies[1]
        canl=goodies[2]
        canw=goodies[3]
        if candy[candylis.index(goodies)]==available:
            canDraw=Rect(-panx+canx,cany,canl,canw)
            screen.blit(canpic,canDraw)
#life
         #x  #y  #l #w 
heartlis=[(600,400,50,30),(700,310,50,30),(800,200,50,30),(820,320,50,30)]#list of ground locations and height & width
heart=[]

for i in range(len(heartlis)):
    heart.append(available)
    
heartpic=image.load("start.png")
heartpic=transform.smoothscale(heartpic,(50,30))

def collecthearts():
    global heart, life, pic, heartlis
    panrect=Rect(panx,pany-pic.get_height(),pic.get_width(),pic.get_height())
    for extralife in heartlis:
        heartx=extralife[0]
        hearty=extralife[1]
        heartl=extralife[2]
        heartw=extralife[3]
        if Rect(-panx+heartx,hearty,heartl,heartw).colliderect(panrect):
            #if life<=5:
            life+=1
            heart[heartlis.index(extralife)]==taken
            heartlis.remove(extralife)

def drawhearts():
    for extralife in heartlis:
        heartx=extralife[0]
        hearty=extralife[1]
        heartl=extralife[2]
        heartw=extralife[3]
        if heart[heartlis.index(extralife)]==available:
            heartDraw=Rect(-panx+heartx,hearty,heartl,heartw)
            screen.blit(heartpic,heartDraw)            

            
        #x  #y #l  #w 
ground=[(0,455,550,45),(560,385,60,45),(620,320,60,45),(710,265,360,45),(1000,470,60,45)]#list of ground locations and height & width


        
    
def drawground(grpic,ground): #function draws blocks at wanted locations
    for block in ground:
        grpic=transform.scale(grpic,(block[2],block[3]))    
        bl=screen.blit(grpic,(block[0]-panx,block[1]))#blits in negative
        

    display.flip()
   



       
   
#sprite    
#Move indicies
RIGHT = 0
DOWN = 1  
UP = 2
LEFT = 3

panpic=[]#pictures of panther runnnig
for pics in range(28):
    panpic.append((image.load("runpanth/runpanth"+str(pics)+".png")))#pics of panther running right
mvstart,mvend=0,6
frame=0#Current spot of movement
jump=False

def movepanth():#function causes pan to move using keys
    #jump=False
    global  frame, panx, pany, panvy, move, direct, mvstart, mvend, jump
    keys=key.get_pressed()
    
    if keys[K_RIGHT] and panx < 3000:
        move=RIGHT
        frame+=1
        panx+=5
        mvstart,mvend=0,6#the start and end pics for running forwards
        direct=RIGHT
        
    if keys[K_LEFT] and panx > 150:
        move=LEFT
        frame+=1
        panx-=5
        mvstart,mvend=7,11#the start and end pics for running backwards
        direct=LEFT#this becomes the last move

    if keys[K_UP] and panx >150 and panx <3000:
        frame+=1
        onground=False
        if keys[K_RIGHT]:
            direct=RIGHT
        if keys[K_LEFT]:
            direct=LEFT
        if direct==RIGHT:
            mvstart,mvend=12,19#the start and end pics for jumping forwards
            panx+=5
            pany-=20
        if direct==LEFT:
            mvstart,mvend=20,27#the start and end pics for jumping backwards
            panx-=5
            pany-=20
    if frame in range(12,27):
        jump=True
    if frame not in range (12,27):
        jump=False

#----------            
    pany+=panvy #can adjust speed of pan
    if pany >= 460: #where panther starts in y
        pany = 460
        panvy = 0
#        pany[ONGROUND]=True
    panvy+=.7 # 


def groundcollide(ground,panrect):
    global panvy, pany, pic
    for block in ground:
        block=Rect(block)
        if panrect.colliderect(block):
            if panvy>0 and panrect.move(0,-panvy).colliderect(block)==False:
                onground=True
                panvy=0
                pany=block.y-32   

        
def drawmove():#Draws character moving
    global frame, panx, pany, mvstart, mvend, jump, panpic#r
    keys=key.get_pressed()
    
    if frame not in range(mvstart,mvend):#if the current frame is not at the right move
        frame=mvstart
    if frame==mvend:#When the frame is at the end of the move
        frame=mvstart
    if jump==True:
        if frame!=mvend:
            myClock.tick(25)
            frame+=1
            #if frame 
        if frame==mvend:
            if direct==RIGHT:
                frame=0
                mvstart,mvend=0,6
            if direct==LEFT:
                frame=7
                mvstart,mvend=7,11
   
    pic= panpic[frame]
    r = pic.get_rect()
    screen.blit(pic,(panx,pany-r.h))#draws pic with x and y at the bottom


while running:
    for evnt in event.get():            
        if evnt.type == QUIT:
            running = False
    pic= panpic[frame]
    drawground(grpic,ground)
    drawBG()
    movepanth()
    drawmove()
    collectgoodies()#(candy)
    drawgoodies()
    collecthearts()
    drawhearts()
    panrect=Rect(panx,pany-pic.get_height(),pic.get_width(),pic.get_height())
    #groundcollide(ground,panrect)
    draw.rect(screen,red,panrect,2)
    
#    message_to_screen("go striat",red)
#    print(pany[ONGROUND])
    #print("panther",panx,pany,"points:",points,"life:",life)
    myClock.tick(20)


quit()
