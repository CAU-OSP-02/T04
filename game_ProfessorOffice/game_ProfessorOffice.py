import pygame
import sys

# 초기화
pygame.init()

# 화면 크기
width = 800
height = 600

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 창 크기
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("A+를 찾아서")

background = pygame.image.load('ProfessorOffice2.png')
prfs1 = pygame.image.load('professor1.png')
prfs1 = pygame.transform.scale(prfs1, (100, 100))
prfs2 = pygame.image.load('professor2.png')
prfs2 = pygame.transform.scale(prfs2, (100, 100))

def background1():
    background = pygame.image.load('ProfessorOffice2.png')
    screen.blit(background, (0, 0))
    screen.blit(prfs1, (420, 240))

class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'
        # text
        self.text_surf = font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    print('click')
                    background1()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'

font = pygame.font.Font('DXMSubtitlesM-KSCpc-EUC-H.ttf', 25)

text1 = font.render('학생, 반가워요.', True, BLACK)
text2 = font.render('이제부터 내가 말하는 거 기억할 수 있죠?', True, BLACK)
text3 = font.render('과제는 총 5개입니다. 개인과제 4개, 조별과제 하나.', True, BLACK)
text4 = font.render('첫 번째 과제는 11월 3일까지.', True, BLACK)
text5 = font.render('두 번째 과제는 11월 22일까지.', True, BLACK)
text6 = font.render('세 번째 과제는 12월 6일까지.', True, BLACK)
text7 = font.render('네 번째 과제는 12월 10일까지.', True, BLACK)
text8 = font.render('마지막으로 조별과제는 12월 21일까지입니다.', True, BLACK)
text9 = font.render('아, 그리고 개별 면담 요청하셨죠?', True, BLACK)
text10 = font.render('12월 13일 오후 1시 정각에 여기로 오시면 됩니다.', True, BLACK)

total_time = 10
start_ticks = pygame.time.get_ticks()

# 사용자가 닫기 버튼을 클릭할 때까지 반복
done = False
clock = pygame.time.Clock()

while not done:
    # 초당 프레임
    clock.tick(10)

    # 메인 이벤트 반복
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background, (0, 0))
    screen.blit(prfs1, (420, 240))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
    screen.blit(text1, (30, 30))
    if elapsed_time > 3:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text2, (30, 30))
    if elapsed_time > 6:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text3, (30, 30))
    if elapsed_time > 9:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text4, (30, 30))
    if elapsed_time > 12:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text5, (30, 30))
    if elapsed_time > 15:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text6, (30, 30))
    if elapsed_time > 18:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text7, (30, 30))
    if elapsed_time > 21:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text8, (30, 30))
    if elapsed_time > 24:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text9, (30, 30))
    if elapsed_time > 27:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text10, (30, 30))
    if elapsed_time > 30:
        screen.blit(background, (0, 0))
        screen.blit(prfs1, (420, 240))

        background1()
        font = pygame.font.Font('Hancom Gothic Regular.ttf', 25)
        question = font.render('두 번째 과제 제출일은?', True, BLACK, (200, 250, 200))
        screen.blit(question, (100, 300))
        button1 = Button('11월 20일', 200, 40, (150, 400), 5)
        button2 = Button('11월 21일', 200, 40, (400, 400), 5)
        button3 = Button('11월 22일', 200, 40, (150, 500), 5)
        button4 = Button('11월 23일', 200, 40, (400, 500), 5)
        button1.draw()
        button2.draw()
        button3.draw()
        button4.draw()

    # 업데이트
    pygame.display.flip()