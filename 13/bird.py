from pico2d import *
import game_world
import game_framework
import random
PIXEL_PER_METER=10/0.3
RUN_SPEED_KPH=20
RUN_SPEED_MPM=RUN_SPEED_KPH*1000/60
RUN_SPEED_MPS=RUN_SPEED_MPM/60.0
RUN_SPEED_PPS=RUN_SPEED_MPS*PIXEL_PER_METER
class Bird:
    TIME_PER_ACTION=0.5
    ACTION_PER_TIME=1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION=8

    def __init__(self):
        self.w=183
        self.h=168
        self.x, self.y = random.randint(200,1400), random.randint(200,500)
        self.frameX = random.randint(0,4)
        self.frameY = random.randint(0,2)
        self.dir=1
        self.image = load_image('bird_animation.png')
        self.timer = 100

    def update(self):
        self.x += self.dir*RUN_SPEED_PPS*game_framework.frame_time
        self.frameX = (self.frameX + Bird.FRAMES_PER_ACTION*Bird.ACTION_PER_TIME*game_framework.frame_time)

        if(self.frameX>=4):
            self.frameY=(self.frameY+1)
            self.frameX=0
        if(self.frameY>2):
            self.frameY=0
        print(self.frameX,' ',self.frameY)
        if(self.x>=1600 or self.x<=0):
            self.dir=-self.dir

        

    def draw(self):
        if(self.dir>0):
            self.image.clip_composite_draw(int(self.frameX)*self.w,int(self.frameY)*self.h,self.w,self.h,0,'',self.x,self.y,self.w,self.h)
        else:
            self.image.clip_composite_draw(int(self.frameX)*self.w,int(self.frameY)*self.h,self.w,self.h,0,'h',self.x,self.y,self.w,self.h)
    def add_event(self, event):
        pass

    def handle_event(self, event):
        pass

