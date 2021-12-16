import pygame
import random

pygame.init()    # pygame 초기화

# 게임에 사용되는 전역 변수 선언
size = [800, 600]          # 1. 화면 크기를 리스트 설정(size[0]은 가로, size[1]은 세로)
screen = pygame.display.set_mode(size)   # 2. 화면 설정

done = False               # 3. 게임 루프에 이용되는 변수
clock = pygame.time.Clock()    # 4. fps (프레임) 설정에 이용되는 변수

# 5. 게임의 배경, 클리어, 실패 했을 때의 배경 사진 불러오기
background = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/background.jpg')
clear = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/clear.png')
failed = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/failed.png')

game_font_s = pygame.font.Font(None, 40)         # 6. 작은 폰트, 큰 폰트
game_font_b = pygame.font.Font(None, 100)

total_time = 60                        # 7. 총 게임 시간
start_ticks = pygame.time.get_ticks()         # 8. 게임에서 시간 측정


# 원하는 텍스트를 작성하는 함수
def draw_text(text, font, surface, x, y, main_color):
    text_obj = font.render(text, True, main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)


# 게임 중 일시정지 기능을 구현한 함수
def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.fill((255, 255, 255))             # 화면 색 채우기 (255, 255, 255)는 rgb값
        draw_text('paused', game_font_b, screen, size[0] / 2, size[1] / 2, (0, 0, 0))
        draw_text('resume [r]', game_font_s, screen, size[0] - 100, 30, (0, 0, 0))
        draw_text('quit [q]', game_font_s, screen, size[0] - 75, 70, (0, 0, 0))
        pygame.display.update()           # 게임 화면 업데이트
        clock.tick(30)                  # fps (프레임) 설정


# 게임을 시작하는 함수(메인)
def runGame():
    germ_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/germ.png')
    germ_image = pygame.transform.scale(germ_image, (50, 50))      # 세균이미지 크기 조정

    # 충돌 판정용 사각형 제작
    germrect = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/germrect.png')
    germrect = pygame.transform.scale(germrect, (30, 30))
    germs = []     # 세균은 리스트로 작성할 예정

    # 8개의 세균을 리스트에 담기
    for i in range(8):
        rect = pygame.Rect(germrect.get_rect())     # 세균 충돌 판정용 사각형
        rect.left = random.randint(0, size[0])   # 세균의 랜덤한 위치 설정
        rect.top = -100
        dy = random.randint(3, 9)        # 세균의 랜덤한 속도 설정
        germs.append({'rect': rect, 'dy': dy})     # 이 두 조건을 포함하여 세균 리스트에 append

    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = size[0] // 2 - person.width // 2     # 사람 위치 지정
    person.top = size[1] - person.height - 70
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.blit(background, (0, 0))      # 불러온 배경이미지 넣기
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000     # 경과된 시간을 변수로 설정

        # 키를 누르면 명령어 실행시키는 과정
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # 창 닫으면 게임 끝
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:       # 왼쪽 방향키 누르면 초당 12 만큼 왼쪽으로
                    person_dx = -12
                elif event.key == pygame.K_RIGHT:    # 오른쪽 방향키 누르면 초당 12 만큼 오른쪽으로
                    person_dx = 12
                elif event.key == pygame.K_UP:       # 위쪽 방향키 누르면 초당 12 만큼 위쪽으로
                    person_dy = -12
                elif event.key == pygame.K_DOWN:     # 아래쪽 방향키 누르면 초당 12 만큼 아래쪽으로
                    person_dy = 12
                elif event.key == pygame.K_p:        # p키 누르면 pause 함수 실행 (일시정지 기능)
                    pause()

            # 키 누르기를 때면 움직임을 멈추는 과정
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    person_dx = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    person_dy = 0

        # 시간에 따라 세균이 떨어지는 속도 증가 시키는 과정
        for germ in germs:
            if 0 <= elapsed_time < 20:          # 시작한지 20초 이하는 속도 값이 3이상 9이하의 랜덤값
                germ['rect'].top += germ['dy']      # 세균 떨어뜨리기
                if germ['rect'].top > size[1]:
                    germs.remove(germ)
                    rect = pygame.Rect(germrect.get_rect())
                    rect.left = random.randint(0, size[0])
                    rect.top = -100
                    dy = random.randint(3, 9)
                    germs.append({'rect': rect, 'dy': dy})
            elif 20 <= elapsed_time < 40:        # 시작한지 20초 이상 40초 이하는 속도 값이 7이상 13이하의 랜덤값
                germ['rect'].top += germ['dy']      # 세균 떨어뜨리기
                if germ['rect'].top > size[1]:
                    germs.remove(germ)
                    rect = pygame.Rect(germrect.get_rect())
                    rect.left = random.randint(0, size[0])
                    rect.top = -100
                    dy2 = random.randint(7, 13)
                    germs.append({'rect': rect, 'dy': dy2})
            elif elapsed_time >= 40:                # 시작한지 40초 이상은 속도 값이 11이상 17이하의 랜덤값
                germ['rect'].top += germ['dy']         # 세균 떨어뜨리기
                if germ['rect'].top > size[1]:
                    germs.remove(germ)
                    rect = pygame.Rect(germrect.get_rect())
                    rect.left = random.randint(0, size[0])
                    rect.top = -100
                    dy3 = random.randint(11, 17)
                    germs.append({'rect': rect, 'dy': dy3})

        # 사람 이동정보 업데이트
        person.left = person.left + person_dx
        person.top = person.top + person_dy

        # 사람 창 밖으로 못 나가게 하는 조건문
        if person.left < 0:
            person.left = 0
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width
        elif person.top < 0:
            person.top = 0
        elif person.top > size[1] - person.height:
            person.top = size[1] - person.height

        screen.blit(person_image, person)  # 사람 화면에 나타내기

        # 충돌 처리 (충돌하면 게임 패배)
        for germ in germs:
            if germ['rect'].colliderect(person):
                done = True
            screen.blit(germ_image, germ['rect'])

        # 타이머 설정, 화면에 출력
        timer = game_font_s.render("timer : " + str(int(total_time - elapsed_time)), True, (255, 255, 255))
        screen.blit(timer, (size[0] - 150, 30))
        draw_text('pause [p]', game_font_s, screen, size[0] - 80, size[1] - 30, (255, 255, 255))

        # 속도가 증가될때 마다 문구 출력
        if 40 <= total_time - elapsed_time <= 41:
            draw_text('speed up!',
                      pygame.font.Font(None, 150), screen, size[0] / 2, size[1] / 2, (0, 0, 0))
        elif 20 <= total_time - elapsed_time <= 21:
            draw_text('speed up!',
                      pygame.font.Font(None, 150), screen, size[0] / 2, size[1] / 2, (0, 0, 0))

        # 죽지 않고 60초를 버틸 경우 clear 화면 출력
        if total_time - elapsed_time <= 0:
            screen.blit(clear, (0, 0))
            draw_text('continue [c]', game_font_s, screen, size[0] - 100, 30, (0, 0, 0))
            pygame.display.update()

        pygame.display.update()


runGame()
pygame.quit()

