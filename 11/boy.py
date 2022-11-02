from pico2d import *


#이벤트 정의
RD,LD,RU,LU,TIMER,AUTO_MODE=range(6)

key_event_table={
    (SDL_KEYDOWN,SDLK_RIGHT):RD,
    (SDL_KEYDOWN,SDLK_LEFT):LD,
    (SDL_KEYUP,SDLK_RIGHT):RU,
    (SDL_KEYUP,SDLK_LEFT):LU,
    (SDL_KEYDOWN,SDLK_a):AUTO_MODE,
}
class AUTO:
    @staticmethod #객체생성이 아니라고 데코레이트로 알려준다.
    def enter(self,event):
        self.dir=self.face_dir
        print('ENTER AUTO')
    @staticmethod
    def exit(self):
        self.face_dir=self.dir
        self.dir=0
        print('EXIT AUTO')
    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x+=self.dir
        if self.x<0 or self.x>800:
            self.dir=-self.dir
    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y+25,200,200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y+25,200,200)



class SLEEP:
    @staticmethod #객체생성이 아니라고 데코레이트로 알려준다.
    def enter(self,event):
        print('ENTER SLEEP')
        self.dir=0
    @staticmethod
    def exit(self):
        print('EXIT SLEEP')
    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,3.141592/2,'', self.x-25, self.y-25,100,100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,-3.141592/2,'', self.x+25, self.y-25,100,100)

#클래스를 이용해서 상태를 만든다.
class IDLE:
    @staticmethod #객체생성이 아니라고 데코레이트로 알려준다.
    def enter(self,event):
        print('ENTER IDLE')
        self.dir=0
        self.timer=1000
    @staticmethod
    def exit(self):
        print('EXIT IDLE')
    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer-=1
        if self.timer==0:
            # self.q.insert(0,TIMER) #q를 직접 액세스하므로 객체지향 프로그래밍에 위배
            self.add_event(TIMER)
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    @staticmethod #객체생성이 아니라고 데코레이트로 알려준다.
    def enter(self,event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir
    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)


next_state={
    SLEEP:{RD:RUN, LD:RUN, RU:RUN, LU:RUN},
    IDLE:{RU:RUN,LU:RUN,RD:RUN,LD:RUN,TIMER:SLEEP,AUTO_MODE:AUTO}, #좌우를 동시에 누른 상태에서 하나라도 떼면 RUN상태
    RUN:{RU:IDLE,LU:IDLE,RD:IDLE,LD:IDLE,AUTO_MODE:AUTO},#위와 마찬가지
    AUTO:{AUTO_MODE:IDLE,RD:RUN,LD:RUN}
}


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.timer = 100

        self.q=[]
        self.cur_state=IDLE
        self.cur_state.enter(self,None)

    def add_event(self,event):
        self.q.insert(0,event)

    def handle_event(self,event): #소년이 스스로 이벤트를 처리할 수 있게
        #이벤트는 키 이벤트 이것을 내부 RD 등으로 변환
        if (event.type,event.key)in key_event_table:
            key_event=key_event_table[(event.type,event.key)]
            self.add_event(key_event) # 변환된 내부 이벤트를 큐에 추가

    def update(self):
        self.cur_state.do(self)

        if self.q:#q에 뭔가 들어있다면
            event=self.q.pop()
            
            if(event in next_state[self.cur_state]):
                self.cur_state.exit(self)#현재 상태를 나가고
                self.cur_state=next_state[self.cur_state][event] #다음 상태를 계산
                self.cur_state.enter(self,event)

    def draw(self):
        self.cur_state.draw(self)
