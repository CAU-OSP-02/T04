import pygame

pygame.init()    # pygame 초기화

# 게임에 사용되는 전역 변수 선언
size = [800, 600]          # 1. 화면 크기를 리스트 설정(size[0]은 가로, size[1]은 세로)
screen = pygame.display.set_mode(size)   # 2. 화면 설정

done = False               # 3. 게임 루프에 이용되는 변수
clock = pygame.time.Clock()    # 4. fps (프레임) 설정에 이용되는 변수

# 5. 이미지 불러오기
first = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images_suwan/1.png')
second = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images_suwan/2.png')
third = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images_suwan/3.png')
road1 = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images_suwan/road1.png')
road2 = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images_suwan/road2.png')
road3 = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images_suwan/road3.png')
dorm = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images_suwan/dormitory.png')
dorm = pygame.transform.scale(dorm, (150, 150))
professor = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images_suwan/professor.png')
professor = pygame.transform.scale(professor, (150, 150))
library = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images_suwan/library.png')
library = pygame.transform.scale(library, (150, 150))
WH = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images_suwan/WH.png')
WH = pygame.transform.scale(WH, (200, 200))
maps = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images_suwan/map.jpg')

game_font_s = pygame.font.Font(None, 40)         # 6. 작은 폰트, 큰 폰트
game_font_b = pygame.font.Font(None, 100)


# 일시정지 기능 구현 함수
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

        screen.fill((255, 255, 255))             # 화면 색 채우기 (흰 색)
        draw_text('paused', game_font_b, screen, size[0] / 2, size[1] / 2, (0, 0, 0))  # 글씨 넣기
        draw_text('resume [r]', game_font_s, screen, size[0] - 100, 30, (0, 0, 0))
        draw_text('quit [q]', game_font_s, screen, size[0] - 75, 70, (0, 0, 0))
        pygame.display.update()           # 게임 화면 업데이트
        clock.tick(30)                  # 프레임 설정


def Map():
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

        screen.fill((255, 255, 255))                   # 화면 색 채우기 (흰 색)
        screen.blit(maps, (size[0] / 2 - 200, size[1] / 2 - 517 / 2))        # 지도 이미지 출력하기
        draw_text('resume [r]', game_font_s, screen, size[0] - 100, 30, (0, 0, 0))   # 글씨 출력하기
        draw_text('quit [q]', game_font_s, screen, size[0] - 75, 70, (0, 0, 0))
        pygame.display.update()      # 게임 화면 업데이트
        clock.tick(30)             # 프레임 설정


def draw_text(text, font, surface, x, y, main_color):
    text_obj = font.render(text, True, main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)


def runMap():
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
        screen.fill((255, 255, 255))
        screen.blit(road1, (200, 0))

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
                elif event.key == pygame.K_m:        # m키 누르면 Map 함수 실행 (맵 보여주기 기능)
                    Map()

            # 키 누르기를 때면 움직임을 멈추는 과정
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    person_dx = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    person_dy = 0

        # 사람 이동정보 업데이트
        person.left = person.left + person_dx
        person.top = person.top + person_dy

        # 사람 창 밖으로 못 나가게 하는 조건문
        if person.left < 0:
            person.left = 0
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width
        elif person.top < 0:
            global x, y
            x = person.left
            y = size[1] - 100
            runMap2(1)
            done = True
        elif person.top > size[1] - person.height:
            person.top = size[1] - person.height

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, size[0] - 80, size[1] - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, size[0] - 73, size[1] - 65, (0, 0, 0))

        pygame.display.update()


def runMap2(a):
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    if a == 1:
        person.left = x  # 사람 위치 지정
        person.top = y
    elif a == 2:
        person.left = x2  # 사람 위치 지정
        person.top = y2
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.fill((255, 255, 255))
        screen.blit(road1, (200, 0))
        screen.blit(road2, (600, 225))

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
                elif event.key == pygame.K_m:        # p키 누르면 pause 함수 실행 (일시정지 기능)
                    Map()

            # 키 누르기를 때면 움직임을 멈추는 과정
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    person_dx = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    person_dy = 0

        # 사람 이동정보 업데이트
        person.left = person.left + person_dx
        person.top = person.top + person_dy

        # 사람 창 밖으로 못 나가게 하는 조건문
        if person.left < 0:
            person.left = 0
        elif person.left > size[0] - person.width:
            global x1, y1
            x1 = size[0] - person.width - size[0] + 60
            y1 = person.top
            runMap3()
            done = True
        elif person.top < 0:
            global x3, y3
            x3 = person.left
            y3 = size[1] - 100
            runMap4(1)
            done = True
        elif person.top > size[1] - person.height:
            person.top = size[1] - person.height

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, size[0] - 80, size[1] - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, size[0] - 73, size[1] - 65, (0, 0, 0))

        pygame.display.update()


def runMap3():
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = x1     # 사람 위치 지정
    person.top = y1
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.fill((255, 255, 255))
        screen.blit(road3, (0, 255))
        screen.blit(dorm, (650, 255))

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
                elif event.key == pygame.K_m:        # p키 누르면 pause 함수 실행 (일시정지 기능)
                    Map()

            # 키 누르기를 때면 움직임을 멈추는 과정
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    person_dx = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    person_dy = 0

        # 사람 이동정보 업데이트
        person.left = person.left + person_dx
        person.top = person.top + person_dy

        # 사람 창 밖으로 못 나가게 하는 조건문
        if person.left < 0:
            global x2, y2
            x2 = size[0] - 60
            y2 = person.top
            runMap2(2)
            done = True
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width
        elif person.top < 0:
            person.top = 0
        elif person.top > size[1] - person.height:
            person.top = size[1] - person.height

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, size[0] - 80, size[1] - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, size[0] - 73, size[1] - 65, (0, 0, 0))

        pygame.display.update()


def runMap4(a):
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    if a == 1:
        person.left = x3  # 사람 위치 지정
        person.top = y3
    elif a == 2:
        person.left = x5  # 사람 위치 지정
        person.top = y5
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.fill((255, 255, 255))
        screen.blit(road1, (200, 0))
        screen.blit(road2, (600, 225))

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
                elif event.key == pygame.K_m:        # p키 누르면 pause 함수 실행 (일시정지 기능)
                    Map()

            # 키 누르기를 때면 움직임을 멈추는 과정
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    person_dx = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    person_dy = 0

        # 사람 이동정보 업데이트
        person.left = person.left + person_dx
        person.top = person.top + person_dy

        # 사람 창 밖으로 못 나가게 하는 조건문
        if person.left < 0:
            person.left = 0
        elif person.left > size[0] - person.width:
            global x4, y4
            x4 = size[0] - person.width - size[0] + 60
            y4 = person.top
            runMap5()
            done = True
        elif person.top < 0:
            global x6, y6
            x6 = person.left
            y6 = size[1] - 100
            runMap6(1)
            done = True
        elif person.top > size[1] - person.height:
            person.top = size[1] - person.height

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, size[0] - 80, size[1] - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, size[0] - 73, size[1] - 65, (0, 0, 0))

        pygame.display.update()


def runMap5():
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = x4     # 사람 위치 지정
    person.top = y4
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.fill((255, 255, 255))
        screen.blit(road3, (0, 255))
        screen.blit(professor, (630, 255))

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
                elif event.key == pygame.K_m:        # p키 누르면 pause 함수 실행 (일시정지 기능)
                    Map()

            # 키 누르기를 때면 움직임을 멈추는 과정
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    person_dx = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    person_dy = 0

        # 사람 이동정보 업데이트
        person.left = person.left + person_dx
        person.top = person.top + person_dy

        # 사람 창 밖으로 못 나가게 하는 조건문
        if person.left < 0:
            global x5, y5
            x5 = size[0] - 60
            y5 = person.top
            runMap4(2)
            done = True
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width
        elif person.top < 0:
            person.top = 0
        elif person.top > size[1] - person.height:
            person.top = size[1] - person.height

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, size[0] - 80, size[1] - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, size[0] - 73, size[1] - 65, (0, 0, 0))

        pygame.display.update()


def runMap6(a):
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    if a == 1:
        person.left = x6     # 사람 위치 지정
        person.top = y6
    if a == 2:
        person.left = x8     # 사람 위치 지정
        person.top = y8
    if a == 3:
        person.left = x10     # 사람 위치 지정
        person.top = y10
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.fill((255, 255, 255))
        screen.blit(road1, (200, 0))
        screen.blit(road2, (600, 225))
        screen.blit(road2, (0, 225))

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
                elif event.key == pygame.K_m:        # p키 누르면 pause 함수 실행 (일시정지 기능)
                    Map()

            # 키 누르기를 때면 움직임을 멈추는 과정
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    person_dx = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    person_dy = 0

        # 사람 이동정보 업데이트
        person.left = person.left + person_dx
        person.top = person.top + person_dy

        # 사람 창 밖으로 못 나가게 하는 조건문
        if person.left < 0:
            global x7, y7
            x7 = size[0] - 60
            y7 = person.top
            runMap7()
            done = True
        elif person.left > size[0] - person.width:
            global x9, y9
            x9 = size[0] - person.width - size[0] + 60
            y9 = person.top
            runMap8()
            done = True
        elif person.top < 0:
            person.top = 0
        elif person.top > size[1] - person.height:
            person.top = size[1] - person.height

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, size[0] - 80, size[1] - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, size[0] - 73, size[1] - 65, (0, 0, 0))

        pygame.display.update()


def runMap7():
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = x7     # 사람 위치 지정
    person.top = y7
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.fill((255, 255, 255))
        screen.blit(road3, (200, 255))
        screen.blit(library, (30, 255))

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
                elif event.key == pygame.K_m:        # p키 누르면 pause 함수 실행 (일시정지 기능)
                    Map()

            # 키 누르기를 때면 움직임을 멈추는 과정
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    person_dx = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    person_dy = 0

        # 사람 이동정보 업데이트
        person.left = person.left + person_dx
        person.top = person.top + person_dy

        # 사람 창 밖으로 못 나가게 하는 조건문
        if person.left < 0:
            person.left = 0
        elif person.left > size[0] - person.width:
            global x8, y8
            x8 = size[0] - person.width - size[0] + 60
            y8 = person.top
            runMap6(2)
            done = True
        elif person.top < 0:
            person.top = 0
        elif person.top > size[1] - person.height:
            person.top = size[1] - person.height

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, size[0] - 80, size[1] - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, size[0] - 73, size[1] - 65, (0, 0, 0))

        pygame.display.update()


def runMap8():
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = x9     # 사람 위치 지정
    person.top = y9
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.fill((255, 255, 255))
        screen.blit(road3, (0, 255))
        screen.blit(WH, (570, 220))

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
                elif event.key == pygame.K_m:        # p키 누르면 pause 함수 실행 (일시정지 기능)
                    Map()

            # 키 누르기를 때면 움직임을 멈추는 과정
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    person_dx = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    person_dy = 0

        # 사람 이동정보 업데이트
        person.left = person.left + person_dx
        person.top = person.top + person_dy

        # 사람 창 밖으로 못 나가게 하는 조건문
        if person.left < 0:
            global x10, y10
            x10 = size[0] - 60
            y10 = person.top
            runMap6(3)
            done = True
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width
        elif person.top < 0:
            person.top = 0
        elif person.top > size[1] - person.height:
            person.top = size[1] - person.height

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, size[0] - 80, size[1] - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, size[0] - 73, size[1] - 65, (0, 0, 0))

        pygame.display.update()


runMap()
pygame.quit()
