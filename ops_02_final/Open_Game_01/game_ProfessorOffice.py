import pygame
from drawing_text import draw_text

# 초기화
pygame.init()
pygame.display.set_caption('Adventure for A+')
# 화면 크기
width = 800
height = 600
size = [width, height]

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

game_font_s = pygame.font.Font("Marvel-Regular.ttf", 40)         # 6. 작은 폰트, 큰 폰트
game_font_b = pygame.font.Font("Marvel-Regular.ttf", 100)

# 창 크기
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("A+를 찾아서")

office1 = pygame.image.load('game_ProfessorOffice_Merge01/ProfessorOffice.png')
office2 = pygame.image.load('game_ProfessorOffice_Merge01/ProfessorOffice2.png')
office2 = pygame.transform.scale(office2, (800, 600))
professor1 = pygame.image.load('game_ProfessorOffice_Merge01/professor1.png')
professor1 = pygame.transform.scale(professor1, (100, 100))
professor2 = pygame.image.load('game_ProfessorOffice_Merge01/professor2.png')
professor2 = pygame.transform.scale(professor2, (100, 100))


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
        clock.tick(30)


def background1():
    screen.blit(office1, (0, 0))
    screen.blit(professor1, (420, 240))


def background2():
    screen.blit(office2, (0, 0))
    screen.blit(professor2, (350, 265))

# 설명, 문제 출제
font1 = pygame.font.Font('DXMSubtitlesM-KSCpc-EUC-H.ttf', 25)

text1 = font1.render('학생, 반가워요.', True, BLACK)
text2 = font1.render('이제부터 내가 말하는 거 기억할 수 있죠?', True, BLACK)
text3 = font1.render('과제는 총 5개입니다. 개인과제 4개, 조별과제 하나.', True, BLACK)
text4 = font1.render('첫 번째 과제는 11월 3일까지.', True, BLACK)
text5 = font1.render('두 번째 과제는 11월 22일까지.', True, BLACK)
text6 = font1.render('세 번째 과제는 12월 6일까지.', True, BLACK)
text7 = font1.render('네 번째 과제는 12월 10일까지.', True, BLACK)
text8 = font1.render('마지막으로 조별과제는 12월 21일까지입니다.', True, BLACK)
text9 = font1.render('아, 그리고 개별 면담 요청하셨죠?', True, BLACK)
text10 = font1.render('12월 13일 오후 1시 정각에 여기로 오시면 됩니다.', True, BLACK)

text11 = font1.render('안녕하세요~ 질문이 있으시다고요?', True, BLACK)
text12 = font1.render('깃허브 과제의 커밋 순서 말씀이신가요?', True, BLACK)
text13 = font1.render('한 번 정리해드릴 테니 잘 듣고 제출하세요.', True, BLACK)
text14 = font1.render('순서 정렬 파일은 총 2개입니다.', True, BLACK)
text15 = font1.render('첫 번째 파일의 커밋 순서는 4, 3, 2, 1이고, cherry-pick을 사용하세요.', True, BLACK)
text16 = font1.render('두 번째 파일의 커밋 순서는 5, 7, 6, 8이고, rebase를 사용하세요.', True, BLACK)
text17 = font1.render('아, 오픈소스 라이선스 발표와 팀 프로젝트 발표 잊지 않으셨죠?', True, BLACK)
text18 = font1.render('첫 번째 발표는 홀수팀 전체 → 짝수팀 전체,', True, BLACK)
text19 = font1.render('두 번째 발표는 짝수팀 전체 → 홀수팀 전체로 진행할 예정입니다.', True, BLACK)
text20 = font1.render('마지막까지 힘내고 좋은 결과 있길 바라요!', True, BLACK)

total_time = 80
start_ticks = pygame.time.get_ticks()


class Button_fail:
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
        self.text_surf = font1.render(text, True, '#FFFFFF')
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
                if self.pressed is True:
                    from Pause import pause_failpro
                    pause_failpro()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'


class Button_continue:
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
        self.text_surf = font1.render(text, True, '#FFFFFF')
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
                if self.pressed is True:
                    import game_ProfessorOffice02
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'


button1 = Button_fail('11월 20일', 200, 40, (175, 470), 5)
button2 = Button_fail('11월 21일', 200, 40, (400, 470), 5)
button3 = Button_continue('11월 22일', 200, 40, (175, 525), 5)
button4 = Button_fail('11월 23일', 200, 40, (400, 525), 5)


# 게임 시작
done = False
clock = pygame.time.Clock()

while not done:
    # 초당 프레임
    clock.tick(10)

    # 메인 이벤트 반복
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # 왼쪽 방향키 누르면 초당 12 만큼 왼쪽으로
                pause()

    background1()
    elapsed_time1 = (pygame.time.get_ticks() - start_ticks) / 1000
    pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
    screen.blit(text1, (30, 30))

    if elapsed_time1 > 3:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text2, (30, 30))
    if elapsed_time1 > 6:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text3, (30, 30))
    if elapsed_time1 > 9:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text4, (30, 30))
    if elapsed_time1 > 12:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text5, (30, 30))
    if elapsed_time1 > 15:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text6, (30, 30))
    if elapsed_time1 > 18:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text7, (30, 30))
    if elapsed_time1 > 21:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text8, (30, 30))
    if elapsed_time1 > 24:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text9, (30, 30))
    if elapsed_time1 > 27:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text10, (30, 30))
    pygame.display.update()

    if elapsed_time1 > 30:
        background1()
        pygame.draw.rect(screen, WHITE, [10, 390, 780, 200], border_radius=15)
        question1 = font1.render('두 번째 과제 제출일은?', True, BLACK)
        remaining_time1 = font1.render(str(int(total_time - elapsed_time1 - 40)), True, RED)
        screen.blit(question1, (30, 410))
        buttons = [button1, button2, button3, button4]
        for button in buttons:
            button.draw()
        pygame.display.update()

pygame.quit()


