import random
import pygame
from drawing_text import draw_text

pygame.init()
pygame.display.set_caption('Adventure for A+')
size = [800, 600]          # 1. 화면 크기를 리스트 설정(size[0]은 가로, size[1]은 세로)
screen = pygame.display.set_mode(size)
game_font_s = pygame.font.Font("Marvel-Regular.ttf", 40)
game_font_b = pygame.font.Font("Marvel-Regular.ttf", 100)
clock = pygame.time.Clock()
background = pygame.image.load('images/library_background.png')
background = pygame.transform.scale(background, (size[0], size[1]))

total_time = 61
start_ticks = pygame.time.get_ticks()


def select_word():
    word_list = [
        'a tale of two cities', 'the lord of the rings', 'and then there were none', 'a message to garcia',
        'the da vinci code', 'the catcher in the rye', 'the eagle has landed', 'kane and abel', 'the little prince'
    ]

    num_of_elements = len(word_list)
    i = random.randint(0, num_of_elements - 1)
    return word_list[i]


def cut_head_char(word):
    return word[1:]


def is_empty_word(word):
    return not word


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


def run_game():
    pygame.init()
    font_big = pygame.font.Font("Marvel-Regular.ttf", 70)
    word = select_word()
    score = 0

    while True:
        screen.blit(background, (0, 0))
        clock.tick(30)
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # 경과된 시간을 변수로 설정

        sf_word = font_big.render(word, True, (0, 0, 0))
        center_x = size[0] / 2 - sf_word.get_rect().width / 2
        screen.blit(sf_word, (center_x, 300))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if chr(event.key) == word[0]:
                    word = cut_head_char(word)
                    if is_empty_word(word):
                        score += 1
                        pygame.display.update()
                        word = select_word()
                        if score == 15:
                            from Pause import pause_clearlib
                            pause_clearlib()
                elif event.key == pygame.K_p:        # p키 누르면 pause 함수 실행 (일시정지 기능)
                    pause()

        timer = game_font_s.render("timer : " + str(int(total_time - elapsed_time)), True, (0, 0, 0))
        if total_time - elapsed_time <= 0:
            from Pause import pause_faillib
            pause_faillib()

        screen.blit(timer, (size[0] - 150, 10))
        draw_text('score : ' + str(score), game_font_s, screen, 70, 40, (0, 0, 0))
        draw_text('pause [p]', game_font_s, screen, size[0] - 80, size[1] - 40, (0, 0, 0))
        pygame.display.update()


run_game()
pygame.quit()
