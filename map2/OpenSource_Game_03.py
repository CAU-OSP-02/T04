import pygame as pg
import time

pg.init()

clock = pg.time.Clock()

Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 200, 100)
Red = (200, 0, 0)

# Screen Option
size = [800, 600]
window = pg.display.set_mode(size)
window.fill(White)
pg.display.set_caption("Artech_Journey")

# Variables & Functions & class
std_address = ["Images/boy.png", "Images/girl.png"]  # 캐릭터 옵션 고려
msg_address = ["Images/frame.jpg", "Images/frame2.jpg", "Images/frame3.jpg", "Images/frame4.jpg"]  # 메시지 프레임
bd_address = ["Images/dormitory.png", "Images/library.png",
              "Images/prof_office.png", "Images/round_bd.png"]  # 건물 이미지 (기숙사, 도서관, 교수연구관, 원형관 순서)


# 모든 게임 알고리즘 구현
# def bug1():
#     dormitory_game1 = 0
# def bug2():
#     dormitory_game2 = 0
# def lib():
#     library_game = 0
# def prof():
#     profs_office_game = 0
# def round():
#     round_building_game = 0


class Student(pg.sprite.Sprite):
    def __init__(self, std_index, x=400, y=600):  # std_index : 캐릭터 이미지 인덱스
        super().__init__()
        self.img = pg.image.load(std_address[std_index])            # 향후 캐릭터 이미지 선택 옵션 생성
        self.width, self.height = self.img.get_size()
        self.x, self.y = (x - self.width/2, y - self.height)        # 캐릭터 생성시 초기 position

    def resize(self, w, h):
        self.img = pg.transform.scale(self.img, (w, h))     # 이미지 사이즈 조정 (화면구도에 따라 캐릭터 크기가 달라질수 있음)
        self.width, self.height = self.img.get_size()
        self.x, self.y = (self.x - self.width/2, self.y - self.height)

        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = (self.x, self.y)

    def show(self):  # 완성된 캐릭터와 rect를 화면에 표시
        window.blit(self.img, self.rect)

    def move(self):  # 키보드 방향키로 캐릭터 및 rect 움직이기
        if event.key == pg.K_UP:
            self.rect.move_ip(0, -15)
        elif event.key == pg.K_DOWN:
            self.rect.move_ip(0, 15)
        elif event.key == pg.K_RIGHT:
            self.rect.move_ip(15, 0)
        elif event.key == pg.K_LEFT:
            self.rect.move_ip(-15, 0)


def message():  # 건물앞에 왔을때 게임시작 여부를 확인하는 창 (or 여러 개의 미니게임 중 선택?)
    frame = pg.image.load("Images/frame2.jpg")
    font = pg.font.SysFont('Corbel', 10, True)

    msg = font.render('Do you want to start game?', True, Black)
    text1 = font.render('Yes', True, White)
    text2 = font.render('No', True, White)

    window.fill(White)
    window.blit(frame, (100, 100))
    pg.draw.rect(window, Green, [400, 450, 60, 25])  # [x, y, w, h]
    pg.draw.rect(window, Red, [500, 450, 60, 25])
    window.blit(msg, (300, 200))
    window.blit(text1, (400, 450))
    window.blit(text2, (500, 450))
    pg.display.update()

    left, middle, right = pg.mouse.get_pressed()
    if left:
        mouse = pg.mouse.get_pos()
        if 390 <= mouse[0] <= 410 and 440 <= mouse[1] <= 460:  # yes 버튼을 클릭했을 때
            wait = pg.image.load("Images/waiting.png")
            window.blit(wait, (size[0]/2, size[1]/2))
            pg.display.update()
            time.sleep(2)
            print("게임 함수 호출")
        elif 490 <= mouse[0] <= 510 and 440 <= mouse[1] <= 460:  # no 버튼을 클릭했을 때
            print("뒤돌기")


class Building(pg.sprite.Sprite):
    def __init__(self, bd_index, x, y):
        super().__init__()
        self.img = pg.image.load(bd_address[bd_index])  # 건물별 이미지 로딩
        self.width, self.height = self.img.get_size()

        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = (x - self.width/2, y - self.height)     # 건물 생성시 초기 position

    def resize(self, w, h):
        self.img = pg.transform.scale(self.img, (w, h))
        self.width, self.height = self.img.get_size()

    def show(self):                          # 건물과 rect를 화면에 표시
        window.blit(self.img, self.rect)

    # def move(self):
    #     case1 = abs(std.x - self.rect.x) > 600
    #     case2 = abs(std.y - self.rect.y) > 400
    #     # if case1:         캐릭터는 제자리걸음, 배경만 움직이도록


std = Student(0)  # 향후 캐릭터 옵션창 만들기
std.resize(30, 60)  # 사이즈 조정

dormitory = Building(0, 850, 800)
dormitory.resize(200, 120)

library = Building(1, 300, 600)
library.resize(200, 150)

profs_office = Building(2, 800, 500)
profs_office.resize(200, 170)

# round_bd = Building(3)
Facilities = pg.sprite.Group()
Facilities.add(dormitory, library, profs_office)

# Main Event
play = True
while play:

    for event in pg.event.get():
        if event.type == pg.QUIT:  # 게임 종료
            play = False
        elif event.type == pg.KEYDOWN:
            std.move()
            if event.key == pg.K_ESCAPE:  # Esc키 -> 게임 일시정지 (화면 전환)
                pause = pg.image.load("Images/pause.png")
                window.blit(pause, (400, 200))
                pg.display.update()
                if event.key == pg.K_ESCAPE:
                    continue

        if pg.sprite.spritecollideany(std, Facilities):
            message()

    window.fill(White)
    dormitory.show()
    library.show()
    profs_office.show()
    std.show()

    clock.tick(10)
    pg.display.flip()

pg.quit()
