from inspect import iscoroutine
from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x ,y= 600,300
theta=0
isCircleTime=False

while (True):
    #원운동끝
    if(theta==360):
        x=600
        y=300
        theta=0
        isCircleTime=False
    
    #원운동
    if(isCircleTime):
        while(theta<360):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(400+math.cos(theta/360*2*math.pi)*200, 300+math.sin(theta/360*2*math.pi)*200)
            theta+=1
            delay(0.01)

    #사각운동
    elif(isCircleTime==False):
        for i in range(800):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x,y)
            if i<100:
                y+=2
            elif i<300:
                x-=2
            elif i<500:
                y-=2
            elif i<700:
                x+=2
            elif i<800:
                y+=2
            delay(0.01)
        
        isCircleTime=True
        x=0
        y=0


            
        



close_canvas()