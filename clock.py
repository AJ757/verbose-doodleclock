import time,pygame
from math import *
def gethms():
    l=list(time.localtime())
    h=l[3];m=l[4];s=l[5]
    return h,m,s
def drawhands(start,coord):
    new=[]
    for k in range(3):
        x=start[0]+coord[k][0]
        y=start[1]+coord[k][1]
        new.append([x,y])
    hrect=pygame.draw.line(sc,hour[0],start,new[0],hour[2])
    mrect=pygame.draw.line(sc,minu[0],start,new[1],minu[2])
    srect=pygame.draw.line(sc,sec[0],start,new[2],sec[2])
    if hrect.collidepoint(mrect.center) or hrect.collidepoint(srect.center):
        hrect=pygame.draw.line(sc,hour1,start,new[0],hour[2])
        mrect=pygame.draw.line(sc,minu[0],start,new[1],minu[2])
        srect=pygame.draw.line(sc,sec[0],start,new[2],sec[2])
    if mrect.collidepoint(srect.center):
        mrect=pygame.draw.line(sc,minu1,start,new[1],minu[2])
        srect=pygame.draw.line(sc,sec[0],start,new[2],sec[2])
def ang(measure):
    h,m,s=measure
    if h>=12:
        h-=12
    angh=radians(h/12*360)
    angm=radians(m/60*360)
    angs=radians(s/60*360)
    return angh,angm,angs
def coord(angles):
    h,m,s=angles
    hm,mm,sm=hour[1],minu[1],sec[1]
    x1=hm*sin(h)
    y1=hm*cos(h)
    x2=mm*sin(m)
    y2=mm*cos(m)
    x3=sm*sin(s)
    y3=sm*cos(s)
    return [[x1,-y1],[x2,-y2],[x3,-y3]]
sec=((50,10,200),120,4)
minu=((10,200,50),100,6)
minu1=pygame.Color(10,200,50,150)
hour=((200,50,10),80,8)
hour1=pygame.Color(200,50,10,120)
clockclr=(5,5,20)
cent=(200,200)
sc=pygame.display.set_mode((400,400))
pygame.display.set_caption('clock')
sc.fill('light yellow')
run=1
while run:
    sc.fill('light yellow')
    pygame.draw.circle(sc,clockclr,(200,200),150,10)
    measure=gethms()
    angles=ang(measure)
    crd=coord(angles)
    drawhands(cent,crd)
    pygame.draw.circle(sc,clockclr,(200,200),5)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run=0
pygame.quit()

    
