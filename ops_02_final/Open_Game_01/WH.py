import pygame
from drawing_text import draw_text

pygame.init()    # pygame 초기화

# 게임에 사용되는 전역 변수 선언
size = [800, 600]          # 1. 화면 크기를 리스트 설정(size[0]은 가로, size[1]은 세로)
screen = pygame.display.set_mode(size)   # 2. 화면 설정

done = False               # 3. 게임 루프에 이용되는 변수
clock = pygame.time.Clock()    # 4. fps (프레임) 설정에 이용되는 변수

# 5. 게임의 배경, 클리어, 실패 했을 때의 배경 사진 불러오기
background = pygame.image.load('images/last_bg.png')
background = pygame.transform.scale(background, (800, 600))

game_font_s = pygame.font.Font("Marvel-Regular.ttf", 40)         # 6. 작은 폰트, 큰 폰트
game_font_b = pygame.font.Font("Marvel-Regular.ttf", 50)
game_font_lb = pygame.font.Font("Marvel-Regular.ttf", 80)

def pause_1():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP2:
                    global second
                    second = 2
                    pause_2()
                elif event.key == pygame.K_SPACE:
                    second = 22
                    pause_2()


        screen.blit(background, (0, 0))  # 불러온 배경이미지 넣기
        draw_text('press the second number', game_font_b, screen, size[0] / 2, size[1] / 2 - 200, (0, 0, 0))
        draw_text('(press spacebar to skip)', game_font_s, screen, size[0] / 2, size[1] / 2 - 150, (0, 0, 0))
        pygame.display.update()
        clock.tick(30)                  # 프레임 설정


def pause_2():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP9:
                    global third
                    third = 9
                    pause_3()
                elif event.key == pygame.K_SPACE:
                    third = 99
                    pause_3()

        screen.blit(background, (0, 0))  # 불러온 배경이미지 넣기
        draw_text('press the third number', game_font_b, screen, size[0] / 2, size[1] / 2 - 200, (0, 0, 0))
        draw_text('(press spacebar to skip)', game_font_s, screen, size[0] / 2, size[1] / 2 - 150, (0, 0, 0))
        pygame.display.update()
        clock.tick(30)


def pause_3():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background, (0, 0))  # 불러온 배경이미지 넣기
        if first == 5 and second == 2 and third == 9:
            draw_text('your score is A+', game_font_lb, screen, size[0] / 2, size[1] / 2 - 200, (0, 0, 0))
        elif first == 55 and second == 2 and third == 9:
            draw_text('your score is B+', game_font_lb, screen, size[0] / 2, size[1] / 2 - 200, (0, 0, 0))
        elif first == 5 and second == 22 and third == 9:
            draw_text('your score is B+', game_font_lb, screen, size[0] / 2, size[1] / 2 - 200, (0, 0, 0))
        elif first == 55 and second == 2 and third == 99:
            draw_text('your score is B+', game_font_lb, screen, size[0] / 2, size[1] / 2 - 200, (0, 0, 0))
        elif first == 55 and second == 22 and third == 99:
            draw_text('your score is F', game_font_lb, screen, size[0] / 2, size[1] / 2 - 200, (0, 0, 0))
        else :
            draw_text('your score is C+', game_font_lb, screen, size[0] / 2, size[1] / 2 - 200, (0, 0, 0))

        pygame.display.update()
        clock.tick(30)


while not done:  # 무한 루프 시작
    clock.tick(30)  # 초당 프레임 30으로 설정
    screen.blit(background, (0, 0))  # 불러온 배경이미지 넣기
    draw_text('press the first number', game_font_b, screen, size[0] / 2, size[1] / 2 - 200, (0, 0, 0))
    draw_text('(press spacebar to skip)', game_font_s, screen, size[0] / 2, size[1] / 2 - 150, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 닫으면 게임 끝
            done = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP5:
                global first
                first = 5
                pause_1()
            elif event.key == pygame.K_SPACE:
                first = 55
                pause_1()

    pygame.display.update()

pygame.quit()