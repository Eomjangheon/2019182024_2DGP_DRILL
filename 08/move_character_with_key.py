from pico2d import *
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
#이벤트를 다루는 함수
def handle_events():
    global running
    global dx,dy,prior_dir
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False
        
        #방향키가 눌리면 dx,dy를 방향에 맞게 세팅
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                dx+=1
            elif event.key==SDLK_LEFT:
                dx-=1
            elif event.key==SDLK_UP:
                dy+=1
            elif event.key==SDLK_DOWN:
                dy-=1
            elif event.key==SDLK_ESCAPE:
                running=False
        #방향키를 떼면 이전 방향을 기억하고, 뗀곳의 dx, dy조절
        elif event.type==SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                dx-=1
                prior_dir='right'
            elif event.key==SDLK_LEFT:
                dx+=1
                prior_dir='left'
            elif event.key==SDLK_UP:
                dy-=1
            elif event.key==SDLK_DOWN:
                dy+=1
#캐릭터 애니메이션을 다루는 함수
def character_animation():
    global frame, x, y, dx, dy, prior_dir
    global TUK_HEIGHT,TUK_WIDTH
    #dx, dy가 모두 0이면 멈춘상태
    if(dx==0 and dy==0):
        if(prior_dir=='right'):
            character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
        elif(prior_dir=='left'):
            character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    
    #dx가 0이 아니라면 dx에 따라 방향 조절
    elif(dx==1):
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif(dx==-1):
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    #dx가 0이고 dy가 0이 아니라면 방향에 맞게 애니메이션
    elif(dy!=0):
        if(prior_dir=='right'):
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif(prior_dir=='left'):
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    frame = (frame + 1) % 8
    #dx, dy를 사용해 대각이동도 가능하게 구현
    x+=dx*5
    y+=dy*5
    #경계체크
    if(x<0):
        x=5
    elif(x>TUK_WIDTH):
        x=TUK_WIDTH-5

    if(y<0):
        y=5
    elif(y>TUK_HEIGHT):
        y=TUK_HEIGHT-5
    delay(0.03)

#객체들을 그리는 함수
def draw_all():
    global TUK_HEIGHT,TUK_WIDTH
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2) 
    character_animation()
    update_canvas()


open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH//2
y = TUK_HEIGHT//2
frame = 0
dx=0
dy=0
prior_dir='left'

#메인
while running:
    draw_all()
    handle_events()
    
    
close_canvas()

   

