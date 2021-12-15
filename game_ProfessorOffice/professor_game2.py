import pygame

pygame.init()

# 화면 크기
width = 800
height = 600

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 창 크기
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('A+를 찾아서')

background2 = pygame.image.load('professor_office2.jpg')
professor2 = pygame.image.load('professor2.png')
professor2 = pygame.transform.scale(professor2, (100, 100))

def office2():
    screen.blit(background2, (0, 0))
    screen.blit(professor2, (400, 300))

font1 = pygame.font.Font('DXMSubtitlesM-KSCpc-EUC-H.ttf', 25)

text1 = font1.render('학생, 우리가 배웠던 git 명령어가 궁금하다고요?', True, BLACK)
text2 = font1.render('먼저 git clone,', True, BLACK)
text3 = font1.render('git pull,', True, BLACK)
text4 = font1.render('git add .,', True, BLACK)
text5 = font1.render('git commit,', True, BLACK)
text6 = font1.render('git push,', True, BLACK)
text7 = font1.render('git checkout,', True, BLACK)
text8 = font1.render('git log,', True, BLACK)
text9 = font1.render('git gui.', True, BLACK)
text10 = font1.render('이외에도 다양한 명렁어가 있습니다.', True, BLACK)

total_time = 10
start_ticks = pygame.time.get_ticks()

font2 = pygame.font.Font('Hancom Gothic Regular.ttf', 25)
question = font2.render('언급되지 않은 git 명령어는?', True, BLACK, (200, 250, 200))

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
                if self.pressed == True:
                    print('click')
                    office2()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'

button1 = Button('git commit', 200, 40, (150, 400), 5)
button2 = Button('git log', 200, 40, (400, 400), 5)
button3 = Button('git branch', 200, 40, (150, 500), 5)
button4 = Button('git checkout', 200, 40, (400, 500), 5)

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    office2()
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
    screen.blit(text1, (30, 30))
    if elapsed_time > 3:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text2, (30, 30))
    if elapsed_time > 5:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text3, (30, 30))
    if elapsed_time > 7:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text4, (30, 30))
    if elapsed_time > 9:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text5, (30, 30))
    if elapsed_time > 11:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text6, (30, 30))
    if elapsed_time > 13:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text7, (30, 30))
    if elapsed_time > 15:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text8, (30, 30))
    if elapsed_time > 17:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text9, (30, 30))
    if elapsed_time > 19:
        pygame.draw.rect(screen, WHITE, [10, 10, 780, 150], border_radius=15)
        screen.blit(text10, (30, 30))
    if elapsed_time > 21:
        office2()

        screen.blit(question, (100, 300))
        button1.draw()
        button2.draw()
        button3.draw()
        button4.draw()

    pygame.display.flip()