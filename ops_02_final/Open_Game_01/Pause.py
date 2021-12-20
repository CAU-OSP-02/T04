import pygame
from drawing_text import draw_text

size = [800, 600]          # 1. 화면 크기를 리스트 설정(size[0]은 가로, size[1]은 세로)
screen = pygame.display.set_mode(size)
game_font_s = pygame.font.Font("Marvel-Regular.ttf", 40)         # 6. 작은 폰트, 큰 폰트
game_font_b = pygame.font.Font("Marvel-Regular.ttf", 100)
clock = pygame.time.Clock()

Howto = pygame.image.load('images/Howto.png')
background_do = pygame.image.load('images/background_st.png')
background_do = pygame.transform.scale(background_do, (800, 600))
background_pr = pygame.image.load('game_ProfessorOffice_Merge01/ProfessorOffice_st.png')
background_pr = pygame.transform.scale(background_pr, (800, 600))
background_lib = pygame.image.load('images/background_lib.png')
background_lib = pygame.transform.scale(background_lib, (800, 600))
one = pygame.image.load('images/game_explain/AvoidingBugs_exp.png')
two = pygame.image.load('images/game_explain/CatchingBugs_exp.png')
three = pygame.image.load('images/game_explain/ProfessorsQuiz_exp.png')
four = pygame.image.load('images/game_explain/BookSearching_exp.png')
five = pygame.image.load('images/game_explain/BookStacking_exp.png')
explains = [one, two, three, four, five]


def pause_main():
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

        screen.fill((255, 255, 255))             # 화면 색 채우기 (흰 색)
        draw_text('paused', game_font_b, screen, size[0] / 2, size[1] / 2, (0, 0, 0))  # 글씨 넣기
        draw_text('resume [r]', game_font_s, screen, size[0] - 100, 30, (0, 0, 0))
        draw_text('quit [q]', game_font_s, screen, size[0] - 75, 70, (0, 0, 0))
        pygame.display.update()           # 게임 화면 업데이트
        clock.tick(30)                  # 프레임 설정


def pause_Howto():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                    from main_map import runMap
                    runMap()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.fill((255, 212, 0))
        screen.blit(Howto, (0, 0))          # 화면 색 채우기 (흰 색)
        draw_text('play [p]', game_font_s, screen, size[0] - 75, 30, (0, 0, 0))
        draw_text('quit [q]', game_font_s, screen, size[0] - 75, 70, (0, 0, 0))
        pygame.display.update()           # 게임 화면 업데이트
        clock.tick(30)                  # 프레임 설정


def pause_dormavoid():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    paused = False
                    pause_explain(1)
                elif event.key == pygame.K_b:
                    paused = False
                    pause_explain(2)

        screen.blit(background_do, (0, 0))
        draw_text('avoid [press a]', game_font_s, screen, 150, 500, (0, 0, 0))
        draw_text('catch [press b]', game_font_s, screen, size[0] - 150, 500, (0, 0, 0))
        pygame.display.update()
        clock.tick(30)


def pause_professor():            # 게임 시작 전 스토리 부분 : continue 버튼만 존재 ( 공용사용 가능 )
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    pause_explain(3)

        screen.blit(background_pr, (0, 0))
        draw_text('continue [press c]', game_font_s, screen, 400, 500, (255, 255, 255))
        pygame.display.update()
        clock.tick(30)


def pause_library():            # 게임 시작 전 스토리 부분 : continue 버튼만 존재 ( 공용사용 가능 )
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    pause_explain(4)

        screen.blit(background_lib, (0, 0))
        draw_text('continue [press c]', game_font_s, screen, size[0] / 2, 500, (0, 0, 0))
        pygame.display.update()
        clock.tick(30)


def pause_cleardorm():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    from main_map import runMap3_done
                    runMap3_done()

        screen.fill((255, 255, 255))             # 화면 색 채우기 (흰 색)
        draw_text('clear!', game_font_b, screen, size[0] / 2, size[1] / 2, (0, 0, 0))  # 글씨 넣기
        draw_text('first number : 5', game_font_s, screen, size[0] - 150, 30, (139, 0, 255))
        draw_text('continue [c]', game_font_s, screen, size[0] - 130, 70, (0, 0, 0))
        pygame.display.update()           # 게임 화면 업데이트
        clock.tick(30)


def pause_faildorm():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    from main_map import runMap3_done
                    runMap3_done()

        screen.fill((0, 0, 0))             # 화면 색 채우기 (흰 색)
        draw_text('failed', game_font_b, screen, size[0] / 2, size[1] / 2, (255, 255, 255))  # 글씨 넣기
        draw_text('continue [c]', game_font_s, screen, size[0] - 130, 70, (255, 255, 255))
        pygame.display.update()           # 게임 화면 업데이트
        clock.tick(30)


def pause_clearpro():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    from main_map import runMap5_done
                    runMap5_done()

        screen.fill((255, 255, 255))             # 화면 색 채우기 (흰 색)
        draw_text('clear!', game_font_b, screen, size[0] / 2, size[1] / 2, (0, 0, 0))  # 글씨 넣기
        draw_text('second number : 2', game_font_s, screen, size[0] - 150, 30, (139, 0, 255))
        draw_text('continue [c]', game_font_s, screen, size[0] - 130, 70, (0, 0, 0))
        pygame.display.update()           # 게임 화면 업데이트
        clock.tick(30)


def pause_failpro():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    from main_map import runMap5_done
                    runMap5_done()

        screen.fill((0, 0, 0))             # 화면 색 채우기 (흰 색)
        draw_text('failed', game_font_b, screen, size[0] / 2, size[1] / 2, (255, 255, 255))  # 글씨 넣기
        draw_text('continue [c]', game_font_s, screen, size[0] - 130, 70, (255, 255, 255))
        pygame.display.update()           # 게임 화면 업데이트
        clock.tick(30)


def pause_clearlib():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    from main_map import runMap7_done
                    runMap7_done()

        screen.fill((255, 255, 255))             # 화면 색 채우기 (흰 색)
        draw_text('clear!', game_font_b, screen, size[0] / 2, size[1] / 2, (0, 0, 0))  # 글씨 넣기
        draw_text('third number : 9', game_font_s, screen, size[0] - 150, 30, (139, 0, 255))
        draw_text('continue [c]', game_font_s, screen, size[0] - 130, 70, (0, 0, 0))
        pygame.display.update()           # 게임 화면 업데이트
        clock.tick(30)


def pause_faillib():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    from main_map import runMap7_done
                    runMap7_done()

        screen.fill((0, 0, 0))             # 화면 색 채우기 (흰 색)
        draw_text('failed', game_font_b, screen, size[0] / 2, size[1] / 2, (255, 255, 255))  # 글씨 넣기
        draw_text('continue [c]', game_font_s, screen, size[0] - 130, 70, (255, 255, 255))
        pygame.display.update()           # 게임 화면 업데이트
        clock.tick(30)


def pause_explain(a):            # 게임 설명 나오고 스페이스바 누르면 시작 ( 공용사용 가능 )
    paused = True

    if a == 1:
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                        from dorm_avoidbug import runGame
                        runGame()

            screen.blit(one, (0, 0))
            draw_text('start! [press spacebar]', game_font_s, screen, 400, 560, (255, 255, 255))
            pygame.display.update()
            clock.tick(30)

    if a == 2:
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                        from Catching_Bugs import catching_bugs, loadBugs
                        loadBugs()
                        catching_bugs()

            screen.blit(two, (0, 0))
            draw_text('start! [press spacebar]', game_font_s, screen, 400, 560, (0, 0, 0))
            pygame.display.update()
            clock.tick(30)

    if a == 3:
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                        import game_ProfessorOffice    # 이상하지만 괜찮음

            screen.blit(three, (0, 0))
            draw_text('start! [press spacebar]', game_font_s, screen, 400, 560, (255, 255, 255))
            pygame.display.update()
            clock.tick(30)

    if a == 4:
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                        from typinggame import run_game
                        run_game()

            screen.blit(four, (0, 0))
            draw_text('start! [press spacebar]', game_font_s, screen, 400, 560, (0, 0, 0))
            pygame.display.update()
            clock.tick(30)

