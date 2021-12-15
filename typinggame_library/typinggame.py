import random
import sys
import pygame
from drawing_text import draw_text

pygame.init()

size = [800, 600]          # 1. 화면 크기를 리스트 설정(size[0]은 가로, size[1]은 세로)
screen = pygame.display.set_mode(size)
game_font_s = pygame.font.Font(None, 40)
clock = pygame.time.Clock()
background = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/library_background.png')
background = pygame.transform.scale(background, (size[0], size[1]))
count1 = pygame.image.load('C:/Users/EDWIL/PycharmProjects/pythonProject1/Open_Game_01/images/3.png')

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


def run_game():
    pygame.init()
    font_big = pygame.font.Font(None, 70)
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
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if chr(event.key) == word[0]:
                    word = cut_head_char(word)
                    if is_empty_word(word):
                        score += 1
                        pygame.display.update()
                        word = select_word()
                        if score == 15:
                            quit()

        timer = game_font_s.render("timer : " + str(int(total_time - elapsed_time)), True, (0, 0, 0))
        if total_time - elapsed_time <= 0:
            quit()
        screen.blit(timer, (size[0] - 150, 30))
        draw_text('score : ' + str(score), game_font_s, screen, size[0] - 100, 80, (0, 0, 0))
        pygame.display.update()


run_game()
pygame.quit()
