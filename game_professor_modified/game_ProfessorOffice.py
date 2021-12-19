import pygame

# 초기화
pygame.init()

# 화면 크기
width = 800
height = 600

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 창 크기
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("A+를 찾아서")

office1 = pygame.image.load('ProfessorOffice.png')
office2 = pygame.image.load('ProfessorOffice2.png')
office2 = pygame.transform.scale(office2, (800, 600))
professor1 = pygame.image.load('professor1.png')
professor1 = pygame.transform.scale(professor1, (100, 100))
professor2 = pygame.image.load('professor2.png')
professor2 = pygame.transform.scale(professor2, (100, 100))

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
                    print("click")
                    background1()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'

button1 = Button('11월 20일', 200, 40, (175, 470), 5)
button2 = Button('11월 21일', 200, 40, (400, 470), 5)
button3 = Button('11월 22일', 200, 40, (175, 525), 5)
button4 = Button('11월 23일', 200, 40, (400, 525), 5)

button5 = Button('4, 3, 2, 1 / 짝수-홀수', 300, 40, (90, 475), 5)
button6 = Button('4, 2, 3, 1 / 홀수-짝수', 300, 40, (400, 475), 5)
button7 = Button('5, 6, 7, 8 / 짝수-홀수', 300, 40, (90, 525), 5)
button8 = Button('5, 7, 6, 8 / 홀수-짝수', 300, 40, (400, 525), 5)

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
    if elapsed_time1 > 30:
        background1()
        pygame.draw.rect(screen, WHITE, [10, 390, 780, 200], border_radius=15)
        question1 = font1.render('두 번째 과제 제출일은?', True, BLACK)
        remaining_time1 = font1.render(str(int(total_time - elapsed_time1 - 40)), True, RED)
        screen.blit(question1, (30, 410))
        screen.blit(remaining_time1, (280, 410))
        buttons = [button1, button2, button3, button4]
        for button in buttons:
            button.draw()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] > 175 and mouse_pos[0] < 375 and mouse_pos[1] > 470 and mouse_pos[1] < 510:
                pygame.draw.rect(screen, (255, 50, 50), [175, 465, 200, 45], border_radius=12)
                msg = font1.render('땡!', True, BLACK)
                screen.blit(msg, (260, 472))
            elif mouse_pos[0] > 400 and mouse_pos[0] < 600 and mouse_pos[1] > 470 and mouse_pos[1] < 510:
                pygame.draw.rect(screen, (255, 50, 50), [400, 465, 200, 45], border_radius=12)
                msg = font1.render('땡!', True, BLACK)
                screen.blit(msg, (485, 472))
            elif mouse_pos[0] > 400 and mouse_pos[0] < 600 and mouse_pos[1] > 525 and mouse_pos[1] < 565:
                pygame.draw.rect(screen, (255, 50, 50), [400, 520, 200, 45], border_radius=12)
                msg = font1.render('땡!', True, BLACK)
                screen.blit(msg, (485, 527))
            elif mouse_pos[0] > 175 and mouse_pos[0] < 375 and mouse_pos[1] > 525 and mouse_pos[1] < 565:
                pygame.draw.rect(screen, (0, 200, 255), [175, 520, 200, 45], border_radius=12)
                msg = font1.render('정답!', True, BLACK)
                screen.blit(msg, (250, 527))
        if total_time - elapsed_time1 < 40:
            # 두 번째 게임
            background2()
            elapsed_time1 = (pygame.time.get_ticks() - start_ticks) / 1000
            pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
            screen.blit(text11, (30, 30))
            if elapsed_time1 > 43:
                pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
                screen.blit(text12, (30, 30))
            if elapsed_time1 > 46:
                pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
                screen.blit(text13, (30, 30))
            if elapsed_time1 > 49:
                pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
                screen.blit(text14, (30, 30))
            if elapsed_time1 > 52:
                pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
                screen.blit(text15, (30, 30))
            if elapsed_time1 > 55:
                pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
                screen.blit(text16, (30, 30))
            if elapsed_time1 > 57:
                pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
                screen.blit(text17, (30, 30))
            if elapsed_time1 > 60:
                pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
                screen.blit(text18, (30, 30))
            if elapsed_time1 > 63:
                pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
                screen.blit(text19, (30, 30))
            if elapsed_time1 > 66:
                pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
                screen.blit(text20, (30, 30))
            if elapsed_time1 > 69:
                background2()
                pygame.draw.rect(screen, WHITE, [10, 390, 780, 200], border_radius=15)
                question2 = font1.render('cherry-pick 파일의 커밋 순서와 팀 프로젝트 발표일을 짝지은 것은?', True, BLACK)
                remaining_time2 = font1.render(str(int(total_time - elapsed_time1)), True, RED)
                screen.blit(question2, (30, 410))
                screen.blit(remaining_time2, (750, 410))
                buttons2 = [button5, button6, button7, button8]
                for button in buttons2:
                    button.draw()
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] > 90 and mouse_pos[0] < 390 and mouse_pos[1] > 475 and mouse_pos[1] < 515:
                        pygame.draw.rect(screen, (255, 50, 50), [90, 470, 300, 45], border_radius=12)
                        msg = font1.render('땡!', True, BLACK)
                        screen.blit(msg, (225, 477))
                    elif mouse_pos[0] > 400 and mouse_pos[0] < 700 and mouse_pos[1] > 475 and mouse_pos[1] < 515:
                        pygame.draw.rect(screen, (255, 50, 50), [400, 470, 300, 45], border_radius=12)
                        msg = font1.render('땡!', True, BLACK)
                        screen.blit(msg, (525, 477))
                    elif mouse_pos[0] > 90 and mouse_pos[0] < 390 and mouse_pos[1] > 525 and mouse_pos[1] < 565:
                        pygame.draw.rect(screen, (255, 50, 50), [90, 520, 300, 45], border_radius=12)
                        msg = font1.render('땡!', True, BLACK)
                        screen.blit(msg, (225, 527))
                    elif mouse_pos[0] > 400 and mouse_pos[0] < 700 and mouse_pos[1] > 525 and mouse_pos[1] < 565:
                        pygame.draw.rect(screen, (0, 200, 255), [400, 520, 300, 45], border_radius=12)
                        msg = font1.render('정답!', True, BLACK)
                        screen.blit(msg, (525, 527))
        # if total_time - elapsed_time1 == 0:
            # 게임 종료

    # 업데이트
    pygame.display.flip()