import random
from pico2d import *
import game_world
import server
import play_state
import game_framework

class Ball:
    image = None

    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = 21
        self.h = 21
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y= random.randint(50, 1600), random.randint(50, 1000)

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if(server.boy.x>500 and server.boy.x<1337):
            self.x=self.x-server.boy.x_velocity * game_framework.frame_time
        if(server.boy.y>500 and server.boy.y<609):
            self.y=self.y-server.boy.y_velocity * game_framework.frame_time

    def get_bb(self):
        return self.x-10,self.y-10,self.x+10,self.y+10

    def handle_collision(self,other,group):
        print("ball del")
        if group=='boy:ball':
            game_world.remove_object(self)
        
