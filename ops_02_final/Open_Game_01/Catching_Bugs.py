import pygame
import random
import time
from drawing_text import draw_text

pygame.init()
pygame.display.set_caption('Adventure for A+')
#변수 선언
black=(0,0,0)
red=(255,0,0)
yellow=(255,255,0)
bug_n = 3 #벌레 개수
large_font=pygame.font.Font("Marvel-Regular.ttf",72)
small_font=pygame.font.Font("Marvel-Regular.ttf",36)
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
size = [800, 600]
game_font_s = pygame.font.Font("Marvel-Regular.ttf", 40)         # 6. 작은 폰트, 큰 폰트
game_font_b = pygame.font.Font("Marvel-Regular.ttf", 100)

done=False
clock=pygame.time.Clock()
bug_list = []
bugimg_list = []


#pygame 무한작동
def catching_bugs():
    global done
    score=0
    start_time=int(time.time())
    pause_time=None
    game_over=0
    pause = False
    bugs=[]

    for i in range(3):
        bug_num = random.randint(0,bug_n-1)
        bug=pygame.Rect(0,0,60,60)
        print(bug, 1)
        bug.left=random.randint(0,screen_width)
        bug.top=random.randint(0,screen_height)
        dx=random.randint(-9,9)
        dy=random.randint(-9,9)
        bugs.append([bug_num,bug,dx,dy])

    while not done:
        clock.tick(30)
        screen.fill(black)

        for event in pygame.event.get():            #버튼 ESC, 마우스 좌클릭 상호작용
            if event.type==pygame.QUIT:
                done=True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and game_over == 0:
                    if pause:
                        start_time += time.time()-pause_time
                    else:
                        pause_time = time.time()
                    pause = not pause
                    print("asdf")
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and game_over==0 and pause == False:
                print(event.pos[0],event.pos[1])
                for [bug_num,bug,dx,dy] in bugs:
                    if bug.collidepoint(event.pos):
                        bugs.remove([bug_num,bug,dx,dy])
                        bug=pygame.Rect(0,0,60,60)
                        bug.left=random.randint(0,screen_width)
                        bug.top=random.randint(0,screen_height)
                        dx=random.randint(-9,9)
                        dy=random.randint(-9,9)
                        bugs.append([random.randint(0,bug_n-1),bug,dx,dy])
                        score+=1
                        if score == 50 :
                            from Pause import pause_cleardorm
                            pause_cleardorm()

        if pause == True:
            screen.fill((255, 255, 255))  # 화면 색 채우기 (흰 색)
            draw_text('paused', game_font_b, screen, size[0] / 2, size[1] / 2, (0, 0, 0))  # 글씨 넣기
            draw_text('resume [r]', game_font_s, screen, size[0] - 100, 30, (0, 0, 0))
            draw_text('quit [q]', game_font_s, screen, size[0] - 75, 70, (0, 0, 0))
            pygame.display.update()  # 게임 화면 업데이트
            clock.tick(30)

        elif game_over==0:      #게임 배경화면
            bg_image = pygame.image.load('Catching_Bugs/images/background.jpg')
            bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))
            screen.blit(bg_image,(0,0))

            for [bug_num,bug,dx,dy] in bugs:
                bug.left+=dx
                bug.top+=dy

            remain_time=60-(int(time.time())-start_time)

            if remain_time<=0:
                game_over=1

            for [bug_num,bug,dx,dy] in bugs:
                screen.blit(bug_image(bug_num),bug)

            for [bug_num,bug,dx,dy] in bugs:        #벌레가 벽에 닿으면 삭제 후 새 벌레 재생성
                if not bug.colliderect(screen.get_rect()):
                    bugs.remove([bug_num,bug,dx,dy])
                    bug=pygame.Rect(0,0,60,60)
                    bug.left=random.randint(0,screen_width)
                    bug.top=random.randint(0,screen_height)
                    dx=random.randint(-9,9)
                    dy=random.randint(-9,9)
                    bugs.append([random.randint(0,bug_n-1),bug,dx,dy])

            score_image=small_font.render('Score : {}'.format(score),True,yellow)
            screen.blit(score_image,(10,10))

            remain_time_image=small_font.render('timer : {}'.format(int(remain_time)),True, (0, 0, 0))
            screen.blit(remain_time_image,(screen_width-10-remain_time_image.get_width(),10))
        if game_over==1:
            from Pause import pause_faildorm
            pause_faildorm()

        pygame.display.update()


def loadBugs():
    global bugimg_list
    for i in range(bug_n):
        bug_image = pygame.image.load('Catching_Bugs/bug_images/bug_{}.png'.format(i)).convert_alpha()
        bug_image = pygame.transform.scale(bug_image, (60, 60))
        bugimg_list.append(bug_image)

def bug_image(n):
    global bugimg_list
    return bugimg_list[n-1]

loadBugs()
catching_bugs()
pygame.quit()