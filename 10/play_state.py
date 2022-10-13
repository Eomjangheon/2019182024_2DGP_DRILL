from pico2d import *
import game_framework
import title_state
import item_state
import add_boy_state
import random
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,800), 90
        self.frame = random.randint(0,7)
        self.dir=1
        self.image = load_image('animation_sheet.png')
        self.ball_image=load_image('ball21x21.png')
        self.big_ball_image=load_image('ball41x41.png')
        self.item=None

    def update(self):
        
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if(self.x>800):
            self.dir=-1
        if(self.x<0):
            self.dir=1

            

    def draw(self):
        if self.item=='BigBall':
            self.big_ball_image.draw(self.x+10,self.y+50)
        elif self.item=='Ball':
            self.ball_image.draw(self.x+10,self.y+50)


        if self.dir==1:
            self.image.clip_draw(self.frame*100, 100*1, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 100*0, 100, 100, self.x, self.y)



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(add_boy_state)

#게임 초기화 : 객체들을 생성한다.
team=[]
boy=None
grass=None

def enter():
    global boy,grass
    boy = Boy()
    team.append(boy)
    grass = Grass()

#게임종료코드 - 객체를 소멸 시킨다.
def exit():
    global team,grass
    del team
    del grass


# game main loop code
def update():
    for boy in team:
        boy.update()

def draw_world():
    grass.draw()
    for boy in team:
        boy.draw()


def draw():
    #게임월드 랜더링
    clear_canvas()
    draw_world()
    update_canvas()

def test_self():
    import sys
    this_module=sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

def pause():
    pass

def resume():
    pass


if __name__=='__main__':
    test_self()
