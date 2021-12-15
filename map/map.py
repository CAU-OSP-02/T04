# #표시 다음에 * 표시 붙어있는 코드들은 무시하셔도 됩니다
import pygame
import pygame as pg
import ctypes # 해상도 구하는 용
vec = pg.math.Vector2

# 초기화
pygame.init()

# 화면 크기(통일이 필요할 듯 합니다...)
width = 800
height = 600

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 창 크기
#* user32 = ctypes.windll.user32
#* screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) # 해상도 구하기
#* screen = pygame.display.set_mode(screensize, FULLSCREEN) # 전체화면
#* size = [400, 300]
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("A+를 찾아서")

# 맵 함수들
def straight(): # 직선
    screen.fill(WHITE) # 화면 바탕 하양
    pg.draw.aaline(screen, BLACK, [width/3, height], [width/3, 0], True)
    pg.draw.aaline(screen, BLACK, [width/3*2, height], [width/3*2, 0], True)

def right(): # 우회전
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [width/3, height], [width/3, 0], True)
    pg.draw.aalines(screen, BLACK, False, [[width/3*2, height], [width/3*2, height/3*2], [width, height/3*2]], True)
    pg.draw.aalines(screen, BLACK, False, [[width/3*2, 0], [width/3*2, height/3], [width, height/3]], True)

def rightDstn(): # 우측으로 직진
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [0, height/3], [width/2, height/3], True)
    pg.draw.aaline(screen, BLACK, [0, height/3*2], [width/2, height/3*2], True)

def straightCrossroad(): # 직선 갈림길
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [0, height/3], [width, height/3], True)
    pg.draw.aalines(screen, BLACK, False, [[0, height/3*2], [width/3, height/3*2], [width/3, height]], True)
    pg.draw.aalines(screen, BLACK, False, [[width, height/3*2], [width/3*2, height/3*2], [width/3*2, height]], True)

def leftDstn(): # 좌측으로 직진
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [width, height/3], [width/2, height/3], True)
    pg.draw.aaline(screen, BLACK, [width, height/3*2], [width/2, height/3*2], True)

## 대각선 이동 가능할 경우
def todorm(): # 북동쪽으로 직진
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [width/3, height], [width/3*2, 0], True)
    pg.draw.aaline(screen, BLACK, [width/3*2, height], [width, 0], True)

def dorm(): # 기숙사 갈림길
    screen.fill(WHITE)
    pg.draw.aalines(screen, BLACK, False, [[0, height], [width/3, height/3], [width/3, 0]], True)
    pg.draw.aalines(screen, BLACK, False, [[width/3, height], [width/2, height/3*2], [width, height/3*2]], True)
    pg.draw.aalines(screen, BLACK, False, [[width/3*2, 0], [width/3*2, height/3], [width, height/3]], True)

def diagonalCrossroad(): # 도서관 갈림길
    screen.fill(WHITE)
    pg.draw.aalines(screen, BLACK, False, [[0, 0], [width/3, height/3*2], [width/3, height]], True)
    pg.draw.aalines(screen, BLACK, False, [[width, 0], [width/3*2, height/3*2], [width/3*2, height]], True)
    pg.draw.aalines(screen, BLACK, False, [[width/3, 0], [width/2, height/3], [width/3*2, 0]], True)

def WH(): # 원형관
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [0, height], [width/3, height/2], True)
    pg.draw.aaline(screen, BLACK, [width/3, height], [width/3*2, height/2], True)

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


# 사용자가 닫기 버튼을 클릭할 때까지 반복
done = False
clock = pygame.time.Clock()

while not done:
    #초당 프레임
    clock.tick(10)

    # 메인 이벤트 반복
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 맵

    #rightDstn()
    #screen.blit(dorm, [425, 175])
    #* screen.blit(prfs, [425, 175])
    #* leftDstn()
    #* screen.blit(libr, [125, 175])
    
    # 캐릭터가 끝까지 가면

    # 캐릭터
    #* pos = vec(width/2, height/2)
    
    # 카메라 이동 및 그에 따른 맵 삭제
    #* if player.top <= height/4:
        #* player.pos.y += abs(player.vel.y)
        #* for plat in platforms:
            #* plat.rect.y += abs(player.vel.y)
            #* if plat.rect.top >= height:
                #* plat.kill()

    # 업데이트
    pygame.display.flip()
