import time
import pygame

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

bg = pygame.image.load('ProfessorOffice.png')
bg2 = pygame.image.load('ProfessorOffice2.png')
bg2 = pygame.transform.scale(bg2, (800, 600))
prfs1 = pygame.image.load('professor1.png')
prfs1 = pygame.transform.scale(prfs1, (100, 100))
prfs2 = pygame.image.load('professor2.png')
prfs2 = pygame.transform.scale(prfs2, (100, 100))
background = [bg, bg2]
professor = [prfs1, prfs2]

def background1():
    screen.blit(bg, (0, 0))
    screen.blit(prfs1, (420, 240))

def background2():
    screen.blit(bg2, (0, 0))
    screen.blit(prfs2, (350, 265))

class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
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
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
            if self.pressed is True:
                print("click")
                self.result()
                self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'

    def result(self):
        msg_font = pygame.font.Font('DXMSubtitlesM-KSCpc-EUC-H.ttf', 50)
        if self == answer:
            msg = msg_font.render('정답!', True, WHITE)
        else:
            msg = msg_font.render('땡!', True, WHITE)
        pygame.draw.rect(screen, BLACK, [300, 180, 300, 100])
        screen.blit(msg, (400, 200))


# 설명, 문제 출제
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

text11 = font.render('안녕하세요~ 질문이 있으시다구요?', True, BLACK)
text12 = font.render('깃허브 과제의 커밋 순서 말씀이신가요?', True, BLACK)
text13 = font.render('한 번 정리해드릴테니 잘 듣고 제출하세요.', True, BLACK)
text14 = font.render('순서 정렬 파일은 총 2개입니다.', True, BLACK)
text15 = font.render('첫번째 파일의 커밋 순서는 4, 3, 2, 1 이고, cherry-pick을 사용하세요', True, BLACK)
text16 = font.render('두번째 파일의 커밋 순서는 5, 7, 6, 8 이고, rebase를 사용하세요', True, BLACK)
text17 = font.render('아 오픈소스 라이선스 발표와 팀 프로젝트 발표 잊지 않으셨죠?', True, BLACK)
text18 = font.render('첫 번째 발표는 홀수팀 전체 -> 짝수팀 전체,', True, BLACK)
text19 = font.render('두 번째 발표는 짝수팀 전체 -> 홀수팀 전체로 진행할 예정입니다.', True, BLACK)
text20 = font.render('마지막까지 힘내고 좋은 결과 있길 바래요!', True, BLACK)

texts_prof = [text1, text2, text3, text4, text5,
              text6, text7, text8, text9, text10,
              text11, text12, text13, text14, text15,
              text16, text17, text18, text19, text20]


total_time = 10
start_ticks = pygame.time.get_ticks()

# 사용자가 닫기 버튼을 클릭할 때까지 반복
done = False
clock = pygame.time.Clock()
ans = []
i = 0

while not done:
    # 초당 프레임
    clock.tick(10)

    if 1 in ans:
        i = 1
        if len(ans) > 1:
            pygame.time.delay(5)
            pygame.quit()

    # 메인 이벤트 반복
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if i == 0:
        background1()
    else:
        background2()

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)

    screen.blit(texts_prof[10*i], (30, 30))
    if elapsed_time > 3:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(texts_prof[10*i+1], (30, 30))
    if elapsed_time > 6:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(texts_prof[10*i+2], (30, 30))
    if elapsed_time > 9:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(texts_prof[10*i+3], (30, 30))
    if elapsed_time > 12:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(texts_prof[10*i+4], (30, 30))
    if elapsed_time > 15:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(texts_prof[10*i+5], (30, 30))
    if elapsed_time > 18:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(texts_prof[10*i+6], (30, 30))
    if elapsed_time > 21:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(texts_prof[10*i+7], (30, 30))
    if elapsed_time > 24:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(texts_prof[10*i+8], (30, 30))
    if elapsed_time > 27:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(texts_prof[10*i+9], (30, 30))
    if elapsed_time > 30:
        screen.blit(background[i], (0, 0))
        screen.blit(professor[i], (420, 240))

        font = pygame.font.Font('Hancom Gothic Regular.ttf', 25)
        if i == 0:
            background1()
            question = font.render('두 번째 과제 제출일은?', True, BLACK, (200, 250, 200))
            screen.blit(question, (100, 300))
            button1 = Button('11월 20일', 200, 40, (150, 400), 5)
            button2 = Button('11월 21일', 200, 40, (400, 400), 5)
            button3 = Button('11월 22일', 200, 40, (150, 500), 5)
            button4 = Button('11월 23일', 200, 40, (400, 500), 5)
            answer = button3
        else:
            background2()
            question = font.render('cherry-pick 파일의 커밋 순서와 팀프로젝트 발표일을 짝지은 것은?', True, BLACK, (200, 250, 200))
            screen.blit(question, (50, 100))
            button1 = Button('4, 3, 2, 1 / 짝수-홀수', 300, 40, (80, 400), 5)
            button2 = Button('4, 2, 3, 1 / 홀수-짝수', 300, 40, (450, 400), 5)
            button3 = Button('5, 6, 7, 8 / 짝수-홀수', 300, 40, (80, 500), 5)
            button4 = Button('5, 7, 6, 8 / 홀수-짝수', 300, 40, (450, 500), 5)
            answer = button4

        buttons = [button1, button2, button3, button4]
        for button in buttons:
            button.draw()

        pygame.time.delay(10)

        for event in pygame.event.get():
            if pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.check_click()
                if answer:
                    ans.append(1)
                    start_ticks = pygame.time.get_ticks()

    # 업데이트
    pygame.display.flip()

