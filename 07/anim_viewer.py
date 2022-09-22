from time import monotonic
from pico2d import *
open_canvas()
river=load_image('river.png')
character=load_image('ragch.png')
skillImg=load_image('ragch.png')

#스프라이트 시트의 정보를 받아온다.
#모션마다 x,y,width,height의 차이가 보여서 따로 저장 
#모션이름을 키로 입력하면->(spriteY,frame,width,height)을 순서대로 받아옴
sprite_inpo={'walkFront':(2243,6,301,300) ,'walkBack':(1943,6,301,300) ,
'attackFront':(1643,4,301,300), 'attackBack':(1343,4,301,300), 'hultFront':(1013,4,301,330),
'hultBack':(683,4,301,330),'die':(340,7,260,350),'skill':(0,9,150,150) }

monsterX, monsterY=700,400
skillX,skillY=0,0

#모션이름을 매개변수로 받아 애니메이션으로 그린다.
def anim(motion):
    global monsterX,monsterY,skillX,skillY
    imageY,frame,width,height=sprite_inpo[motion]
    skillX,skillY=monsterX-150,monsterY
    #딕셔너리에서 받아온 정보로 동작에 따른 frame수만큼 이미지그리기   
    for i in range(frame):
        clear_canvas()
        river.clip_draw(0,2000,800,600,400,300)
        character.clip_draw(i*width,imageY,width,height,monsterX,monsterY)
        update_canvas()
        anim_move(motion,i)
        delay(0.1)
        get_events()

#모션마다 특수한 경우를 따로 함수로 처리
def anim_move(motion,frame):
    global monsterX,monsterY,skillX,skillY
    skillX,skillY=monsterX-150,monsterY-10
    if(motion=='walkFront'):
        monsterX-=10
        monsterY-=10
    elif(motion=='walkBack'):
        monsterX-=10
        monsterY+=10
    elif(motion=='die' and frame==6):
        delay(1)

    #공격 모션에서 스킬과 몬스터를 같이 그리기
    elif((motion=='attackFront'or motion=='attackBack') and frame==3):
        for i in range(8):
            clear_canvas()
            river.clip_draw(0,2000,800,600,400,300)
            imageY,frame,width,height=sprite_inpo['skill']
            skillImg.clip_draw(i*width,imageY,width,height,skillX,skillY)
            imageY,frame,width,height=sprite_inpo[motion]
            character.clip_draw(3*width,imageY,width,height,monsterX,monsterY)
            skillX-=10
            skillY-=10
            update_canvas()
            delay(0.05)
            get_events()

def aiFront():
    for i in range(3):
        anim('walkFront')
    for i in range(3):
        anim('attackFront')
    anim('hultFront')
    anim('die')

def aiBack():
    for i in range(3):
        anim('walkBack')
    for i in range(3):
        anim('attackBack')
    anim('hultBack')
    anim('die')



while True:
    aiFront()
    aiBack()
    monsterX, monsterY=700,400
    
        
    


close_canvas
