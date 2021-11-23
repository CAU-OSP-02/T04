# # 다음에 * 붙어있는 코드들은 무시하셔도 됩니다
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

def library(): # 북서쪽으로(도서관)
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [width/3, height/2], [width/3*2, height], True)
    pg.draw.aaline(screen, BLACK, [width/3*2, height/2], [width, height], True)

def WH(): # 원형관
    screen.fill(WHITE)
    pg.draw.aaline(screen, BLACK, [0, height], [width/3, height/2], True)
    pg.draw.aaline(screen, BLACK, [width/3, height], [width/3*2, height/2], True)

# 이미지
bush_img = pygame.image.load("bush.png") # 덤불
bush_img = pygame.transform.scale(bush_img, (128, 128))

pave_img = pygame.image.load("paving.png") # 보도블럭
pave_img = pygame.transform.scale(pave_img, (128, 128))

dorm_img = pygame.image.load("dormitory.png") # 기숙사
dorm_img = pygame.transform.scale(dorm_img, (256, 256))

prfs_img = pygame.image.load("professor.png") # 교수연구관
prfs_img = pygame.transform.scale(prfs_img, (256, 256))

libr_img = pygame.image.load("library.png") # 도서관
libr_img = pygame.transform.scale(libr_img, (256, 256))

WH_img = pygame.image.load("WH.png") # 원형관
WH_img = pygame.transform.scale(WH_img, (280, 166))


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

    # 맵 ## 맵 함수들을 동시에 실행시킬 수 없어서 주석처리 했습니다!

    # straight()
    # 캐릭터가 북쪽으로 끝까지 가면
    # right()
    # 캐릭터가 우회전하여 끝까지 가면
    # rightDstn()
    # screen.blit(dorm_img, [425, 175]) # 기숙사 등장    
    # 캐릭터가 이미지에 닿으면 미니게임 시작    
    # 미니게임 끝난 후
    # rightDstn()
    # screen.blit(dorm_img, [425, 175])
    # 캐릭터가 서쪽으로 끝까지 가면
    # right()
    # 캐릭터가 우회전하여 끝까지 가면
    # rightDstn()
    # screen.blit(prfs_img, [425, 175]) # 교수연구관 등장
    # 캐릭터가 이미지에 닿으면 미니게임 시작    
    # 미니게임 끝난 후
    # rightDstn()
    # screen.blit(prfs_img, [425, 175])
    # 캐릭터가 서쪽으로 끝까지 가면
    # right()
    # 캐릭터가 북쪽으로 끝까지 가면
    # straightCrossroad() # 갈림길 등장
    # 캐릭터가 좌회전하여 끝까지 가면
    # leftDstn()
    # screen.blit(libr_img, [125, 175]) # 도서관 등장
    # 캐릭터가 이미지에 닿으면 미니게임 시작    
    # 미니게임 끝난 후
    # leftDstn()
    # screen.blit(libr_img, [125, 175])
    # 캐릭터가 동쪽으로 끝까지 가면
    # straightCrossroad() # 갈림길 재등장
    # 캐릭터가 동쪽으로 끝까지 가면
    # rightDstn()
    # screen.blit(WH_img, [425, 225]) # 원형관 등장
    
    
    #* 캐릭터가 끝까지 가면

    #* 캐릭터
    #* pos = vec(width/2, height/2)
    
    #* 카메라 이동 및 그에 따른 맵 삭제
    #* if player.top <= height/4:
        #* player.pos.y += abs(player.vel.y)
        #* for plat in platforms:
            #* plat.rect.y += abs(player.vel.y)
            #* if plat.rect.top >= height:
                #* plat.kill()

    # 업데이트
    pygame.display.flip()
