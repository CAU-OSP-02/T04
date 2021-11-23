import pygame
import pygame as pg
import time
# import ctypes  해상도 구하는 용

vec = pg.math.Vector2

# 초기화
pygame.init()


# 화면 크기 (통일이 필요할 듯 합니다...)
width = 800
height = 600


# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YES_GREEN = (0, 200, 100)   # 옵션창 버튼색
No_Red = (200, 0, 0)        # 옵션창 버튼색


# 이미지

bush_img = pygame.image.load("bush.png")
bush_img = pygame.transform.scale(bush_img, (128, 128))

pave_img = pygame.image.load("paving.png")
pave_img = pygame.transform.scale(pave_img, (128, 128))

dorm_img = pygame.image.load("dormitory.png")
dorm_img = pygame.transform.scale(dorm_img, (256, 256))

prfs_img = pygame.image.load("professor.png")
prfs_img = pygame.transform.scale(prfs_img, (256, 256))

libr_img = pygame.image.load("library.png")
libr_img = pygame.transform.scale(libr_img, (256, 256))

std_address = ["boy.png", "girl.png"]  # 캐릭터 옵션 고려
building = [bush_img, pave_img, dorm_img, prfs_img, libr_img]

# 창 크기
# * user32 = ctypes.windll.user32
# * screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) # 해상도 구하기
# * screen = pygame.display.set_mode(screensize, FULLSCREEN) # 전체화면
# * size = [400, 300]

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("A+를 찾아서")


# 맵 함수들
def straight():  # 직선
    screen.fill(WHITE)  # 화면 바탕 하양
    pg.draw.aaline(screen, BLACK, [width / 3, height], [width / 3, 0], True)
    pg.draw.aaline(screen, BLACK, [width / 3 * 2, height], [width / 3 * 2, 0], True)


def right():  # 우회전
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [width / 3, height], [width / 3, 0], True)
    pg.draw.aalines(screen, BLACK, False,
                    [[width / 3 * 2, height], [width / 3 * 2, height / 3 * 2], [width, height / 3 * 2]], True)
    pg.draw.aalines(screen, BLACK, False, [[width / 3 * 2, 0], [width / 3 * 2, height / 3], [width, height / 3]], True)


def rightDst():  # 우측으로 직진
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [0, height / 3], [width / 2, height / 3], True)
    pg.draw.aaline(screen, BLACK, [0, height / 3 * 2], [width / 2, height / 3 * 2], True)


def straightCrossroad():  # 직선 갈림길
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [0, height / 3], [width, height / 3], True)
    pg.draw.aalines(screen, BLACK, False, [[0, height / 3 * 2], [width / 3, height / 3 * 2], [width / 3, height]], True)
    pg.draw.aalines(screen, BLACK, False,
                    [[width, height / 3 * 2], [width / 3 * 2, height / 3 * 2], [width / 3 * 2, height]], True)


def leftDst():  # 좌측으로 직진
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [width, height / 3], [width / 2, height / 3], True)
    pg.draw.aaline(screen, BLACK, [width, height / 3 * 2], [width / 2, height / 3 * 2], True)


## 대각선 이동 가능할 경우
def todorm():  # 북동쪽으로 직진
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [width / 3, height], [width / 3 * 2, 0], True)
    pg.draw.aaline(screen, BLACK, [width / 3 * 2, height], [width, 0], True)


def dormCrossroad():  # 기숙사 갈림길
    screen.fill(WHITE)
    pg.draw.aalines(screen, BLACK, False, [[0, height], [width / 3, height / 3], [width / 3, 0]], True)
    pg.draw.aalines(screen, BLACK, False, [[width / 3, height], [width / 2, height / 3 * 2], [width, height / 3 * 2]],
                    True)
    pg.draw.aalines(screen, BLACK, False, [[width / 3 * 2, 0], [width / 3 * 2, height / 3], [width, height / 3]], True)


def diagonalCrossroad():  # 도서관 갈림길
    screen.fill(WHITE)
    pg.draw.aalines(screen, BLACK, False, [[0, 0], [width / 3, height / 3 * 2], [width / 3, height]], True)
    pg.draw.aalines(screen, BLACK, False, [[width, 0], [width / 3 * 2, height / 3 * 2], [width / 3 * 2, height]], True)
    pg.draw.aalines(screen, BLACK, False, [[width / 3, 0], [width / 2, height / 3], [width / 3 * 2, 0]], True)


def WH():  # 원형관
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [0, height], [width / 3, height / 2], True)
    pg.draw.aaline(screen, BLACK, [width / 3, height], [width / 3 * 2, height / 2], True)


def message():  # 건물앞에 왔을때 게임시작 여부를 확인하는 창 (or 여러 개의 미니게임 중 선택?)
    frame = pg.image.load("Images/frame2.jpg")
    font = pg.font.SysFont('Corbel', 10, True)

    msg = font.render('Do you want to start game?', True, BLACK)
    text1 = font.render('Yes', True, WHITE)
    text2 = font.render('No', True, WHITE)

    screen.blit(frame, (100, 100))
    pg.draw.rect(screen, YES_GREEN, [400, 450, 60, 25])  # [x, y, w, h]
    pg.draw.rect(screen, No_Red, [500, 450, 60, 25])
    screen.blit(msg, (300, 200))
    screen.blit(text1, (400, 450))
    screen.blit(text2, (500, 450))


# 캐릭터 클래스
class Student(pg.sprite.Sprite):
    def __init__(self, std_index, x=400, y=600):  # std_index : 캐릭터 이미지 인덱스
        super().__init__()
        self.img = pg.image.load(std_address[std_index])            # 향후 캐릭터 이미지 선택 옵션 생성
        self.img = pg.transform.scale(self.img, (80, 100))
        self.width, self.height = self.img.get_size()
        self.x, self.y = (x - self.width/2, y - self.height)        # 캐릭터 생성시 초기 position

        self.rect = self.img.get_rect()
        self.rect.center = (x - self.width/2, y - self.height)

    def show(self):  # 완성된 캐릭터와 rect를 화면에 표시
        screen.blit(self.img, self.rect)

    def move(self):  # 키보드 방향키로 캐릭터 및 rect 움직이기
        if event.key == pg.K_UP:
            straight()
            self.rect.move_ip(0, -15)
        elif event.key == pg.K_DOWN:
            # 후진....?
            self.rect.move_ip(0, 15)
        elif event.key == pg.K_RIGHT:
            rightDst()
            self.rect.move_ip(15, 0)
        elif event.key == pg.K_LEFT:
            leftDst()
            self.rect.move_ip(-15, 0)


class Building(pg.sprite.Sprite):
    def __init__(self, bd_index):
        super().__init__()
        self.img = building[bd_index]
        self.rect = self.img.get_rect()

    def show(self):                          # 건물과 rect를 화면에 표시
        screen.blit(self.img, self.rect)


# 인스턴스 및 sprite 그룹 생성
std = Student(0)

bush = Building(0)
pave = Building(1)
dormitory = Building(2)
profs_office = Building(3)
library = Building(4)

Facilities = pg.sprite.Group()
Facilities.add(bush, pave, dormitory, profs_office, library)


# 사용자가 닫기 버튼을 클릭할 때까지 반복
done = False
clock = pygame.time.Clock()
case1 = std.rect.y < 200
case2 = std.rect.y > 400


while not done:
    # 초당 프레임
    clock.tick(10)

    # 메인 이벤트 반복
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            std.move()
            if case1:
                std.y -= 400
            else:
                std.y += 400

    screen.fill(WHITE)
    dormitory.show()
    library.show()
    profs_office.show()
    std.show()

    if pg.sprite.spritecollideany(std, Facilities):
        screen.fill(WHITE)
        message()

        if pg.MOUSEBUTTONDOWN:
            mouse = pg.mouse.get_pos()
            if 390 <= mouse[0] <= 410 and 440 <= mouse[1] <= 460:  # yes 버튼을 클릭했을 때
                time.sleep(2)
                # minigame 호출
            elif 490 <= mouse[0] <= 510 and 440 <= mouse[1] <= 460:  # no 버튼을 클릭했을 때
                print("...")

    pygame.display.flip()
