import pygame
from Pause import pause_dormavoid, pause_faildorm
from Pause import pause_professor
from Pause import pause_library

pygame.init()    # pygame 초기화

# 게임에 사용되는 전역 변수 선언
size = [800, 600]          # 1. 화면 크기를 리스트 설정(size[0]은 가로, size[1]은 세로)
screen = pygame.display.set_mode(size)   # 2. 화면 설정
width = size[0]
height = size[1]

done = False               # 3. 게임 루프에 이용되는 변수
clock = pygame.time.Clock()    # 4. fps (프레임) 설정에 이용되는 변수

# 5. 이미지 불러오기
map_straight = pygame.image.load('images/map_decorated/straight.png') # 직진
map_turnright1 = pygame.image.load('images/map_decorated/right1.png') # 우회전1
map_turnright2 = pygame.image.load('images/map_decorated/right2.png') # 우회전2
map_dorm = pygame.image.load('images/map_decorated/rightDstn.png') # 기숙사
map_professor = pygame.image.load('images/map_decorated/rightDstnProfessor.png') # 교수연구관
map_crossroad = pygame.image.load('images/map_decorated/crossroad.png') # 갈림길
map_library = pygame.image.load('images/map_decorated/rightDstnLibrary.png') # 도서관
map_WH = pygame.image.load('images/map_decorated/rightDstnWH.png') # 원형관
building_dorm = pygame.image.load('images/map_decorated/dormitory.png')
building_dorm = pygame.transform.scale(building_dorm, (256, 256))
building_professor = pygame.image.load('images/map_decorated/professor.png')
building_professor = pygame.transform.scale(building_professor, (256, 256))
building_library = pygame.image.load('images/map_decorated/library.png')
building_library = pygame.transform.scale(building_library, (256, 256))
building_WH = pygame.image.load('images/map_decorated/round hall.png')
building_WH = pygame.transform.scale(building_WH, (300, 300))
maps = pygame.image.load('images/map_decorated/map.jpg')
game_font_s = pygame.font.Font("Marvel-Regular.ttf", 40)         # 6. 작은 폰트, 큰 폰트
game_font_b = pygame.font.Font("Marvel-Regular.ttf", 100)


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
        draw_text('paused', game_font_b, screen, width / 2, height / 2, (0, 0, 0))  # 글씨 넣기
        draw_text('resume [r]', game_font_s, screen, width - 100, 30, (0, 0, 0))
        draw_text('quit [q]', game_font_s, screen, width - 75, 70, (0, 0, 0))
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
        screen.blit(maps, (width / 2 - 200, height / 2 - 517 / 2))        # 지도 이미지 출력하기
        draw_text('resume [r]', game_font_s, screen, width - 100, 30, (0, 0, 0))   # 글씨 출력하기
        draw_text('quit [q]', game_font_s, screen, width - 75, 70, (0, 0, 0))
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
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/map_decorated/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = width // 2 - person.width // 2     # 사람 위치 지정
    person.top = height - person.height - 70
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.blit(map_straight, (0, 0))

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
        elif person.left > width - person.width:
            person.left = width - person.width
        elif person.top < 0:
            global x, y
            x = person.left
            y = height - 100
            runMap2(1)
            done = True
        elif person.top > height - person.height:
            person.top = height - person.height
        elif person.left < width / 3:
            person.left = width / 3
        elif person.right > width / 3 * 2:
            person.right = width / 3 * 2

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, width - 80, height - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, width - 73, height - 65, (0, 0, 0))

        pygame.display.update()


def runMap2(a):
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/map_decorated/person.png')
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
        screen.blit(map_turnright1, (0, 0))

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
        elif person.left > width - person.width:
            global x1, y1
            x1 = width - person.width - width + 60
            y1 = person.top
            runMap3()
            done = True
        elif person.top < 0:
            global x3, y3
            x3 = person.left
            y3 = height - 100
            runMap4(1)
            done = True
        elif person.top > height - person.height:
            person.top = height - person.height

        elif person.left < width / 3:
            person.left = width / 3

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, width - 80, height - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, width - 73, height - 65, (0, 0, 0))

        pygame.display.update()


def runMap3():
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/map_decorated/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = x1     # 사람 위치 지정
    person.top = y1
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.blit(map_dorm, (0, 0))
        screen.blit(building_dorm, (425, 150))

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
            x2 = width - 60
            y2 = person.top
            runMap2(2)
            done = True
        elif person.left > size[0] - person.width - 250:
            pause_dormavoid()
        elif person.top < 0:
            person.top = 0
        elif person.top > height - person.height:
            person.top = height - person.height

        elif person.bottom < height / 3:
            person.bottom = height / 3
        elif person.bottom > height / 3 * 2:
            person.bottom = height / 3 * 2

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, width - 80, height - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, width - 73, height - 65, (0, 0, 0))

        pygame.display.update()


def runMap4(a):
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/map_decorated/person.png')
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
        screen.blit(map_turnright2, (0, 0))

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
        elif person.left > width - person.width:
            global x4, y4
            x4 = width - person.width - width + 60
            y4 = person.top
            runMap5()
            done = True
        elif person.top < 0:
            global x6, y6
            x6 = person.left
            y6 = height - 100
            runMap6(1)
            done = True
        elif person.top > height - person.height:
            person.top = height - person.height

        elif person.left < width / 3:
            person.left = width / 3

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, width - 80, height - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, width - 73, height - 65, (0, 0, 0))

        pygame.display.update()


def runMap5():
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/map_decorated/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = x4     # 사람 위치 지정
    person.top = y4
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.blit(map_professor, (0, 0))
        screen.blit(building_professor, (425, 150))

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
            x5 = width - 60
            y5 = person.top
            runMap4(2)
            done = True
        elif person.left > size[0] - person.width - 250:
            pause_professor()
        elif person.top < 0:
            person.top = 0
        elif person.top > height - person.height:
            person.top = height - person.height

        elif person.bottom < height / 3:
            person.bottom = height / 3
        elif person.bottom > height / 3 * 2:
            person.bottom = height / 3 * 2

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, width - 80, height - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, width - 73, height - 65, (0, 0, 0))

        pygame.display.update()


def runMap6(a):
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/map_decorated/person.png')
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
        screen.blit(map_crossroad, (0, 0))

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
            x7 = width - 60
            y7 = person.top
            runMap7()
            done = True
        elif person.left > width - person.width:
            global x9, y9
            x9 = width - person.width - width + 60
            y9 = person.top
            runMap8()
            done = True
        elif person.top < 0:
            person.top = 0
        elif person.top > height - person.height:
            person.top = height - person.height

        elif person.bottom < height / 3:
            person.bottom = height / 3

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, width - 80, height - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, width - 73, height - 65, (0, 0, 0))

        pygame.display.update()


def runMap7():
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/map_decorated/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = x7     # 사람 위치 지정
    person.top = y7
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.blit(map_library, (0, 0))
        screen.blit(building_library, (100, 150))

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
        if person.left < 250:
            pause_library()
        elif person.left > width - person.width:
            global x8, y8
            x8 = width - person.width - width + 60
            y8 = person.top
            runMap6(2)
            done = True
        elif person.top < 0:
            person.top = 0
        elif person.top > height - person.height:
            person.top = height - person.height

        elif person.bottom < height / 3:
            person.bottom = height / 3
        elif person.bottom > height / 3 * 2:
            person.bottom = height / 3 * 2

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, width - 80, height - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, width - 73, height - 65, (0, 0, 0))

        pygame.display.update()


def runMap8():
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/map_decorated/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = x9     # 사람 위치 지정
    person.top = y9
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.blit(map_WH, (0, 0))
        screen.blit(building_WH, (400, 100))

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
            x10 = width - 60
            y10 = person.top
            runMap6(3)
            done = True
        elif person.left > width - person.width - 300:
            import WH
        elif person.top < 0:
            person.top = 0
        elif person.top > height - person.height:
            person.top = height - person.height

        elif person.bottom < height / 3:
            person.bottom = height / 3
        elif person.bottom > height / 3 * 2:
            person.bottom = height / 3 * 2

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, width - 80, height - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, width - 73, height - 65, (0, 0, 0))

        pygame.display.update()


def runMap3_done():
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/map_decorated/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = x1     # 사람 위치 지정
    person.top = y1
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.blit(map_dorm, (0, 0))
        screen.blit(building_dorm, (425, 150))

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
            x2 = width - 60
            y2 = person.top
            runMap2(2)
            done = True
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width
        elif person.top < 0:
            person.top = 0
        elif person.top > height - person.height:
            person.top = height - person.height

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, width - 80, height - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, width - 73, height - 65, (0, 0, 0))

        pygame.display.update()

def runMap5_done():
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/map_decorated/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = x4     # 사람 위치 지정
    person.top = y4
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.blit(map_professor, (0, 0))
        screen.blit(building_professor, (425, 150))

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
            x5 = width - 60
            y5 = person.top
            runMap4(2)
            done = True
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width
        elif person.top < 0:
            person.top = 0
        elif person.top > height - person.height:
            person.top = height - person.height

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, width - 80, height - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, width - 73, height - 65, (0, 0, 0))

        pygame.display.update()


def runMap7_done():
    # 사람 설정 과정
    person_image = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/map_decorated/person.png')
    person_image = pygame.transform.scale(person_image, (50, 100))
    person = pygame.Rect(person_image.get_rect())        # 사람 충돌 판정용 사각형
    person.left = x7     # 사람 위치 지정
    person.top = y7
    person_dx = 0         # 사람의 속도 변수 초기화 (x축 방향)
    person_dy = 0         # 사람의 속도 변수 초기화 (y축 방향)

    global done     # done = False 였던것 기억
    while not done:    # 무한 루프 시작
        clock.tick(30)      # 초당 프레임 30으로 설정
        screen.blit(map_library, (0, 0))
        screen.blit(building_library, (100, 150))

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
        elif person.left > width - person.width:
            global x8, y8
            x8 = width - person.width - width + 60
            y8 = person.top
            runMap6(2)
            done = True
        elif person.top < 0:
            person.top = 0
        elif person.top > height - person.height:
            person.top = height - person.height

        screen.blit(person_image, person)  # 사람 화면에 나타내기
        draw_text('pause [p]', game_font_s, screen, width - 80, height - 30, (0, 0, 0))
        draw_text('map [m]', game_font_s, screen, width - 73, height - 65, (0, 0, 0))

        pygame.display.update()



runMap()
pygame.quit()
