import pygame  # 1. pygame 선언

pygame.init()  # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size = [640, 640]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    global done

    bar_x = []
    bar_y = []

    ## 게임판 크기
    screen_width = size[0]
    screen_height = size[1]

    ## 탁구채 크기 (width, height)
    bar_width = 8
    bar_height = 64

    ## 탁구채의 시작점 (x,y), 좌측 맨끝 중앙
    bar_cul_x = [0, 64, 64 ]
    bar_cul_y = [576, 512, 576]
    bar_low_x = []
    bar_low_x = []
    ## 가로와 세로 구현 !!!

    ## 탁구공 크기 (반지름)
    circle_radius = 16
    circle_diameter = circle_radius * 2

    ## 탁구공 시작점 (x, y), 우측 맨끝 중앙
    circle_x = circle_start_x = 32  ## 원의 지름 만큼 빼기
    circle_y = circle_start_y = 608

    while not done:
        time_passed = clock.tick(30)
        time_sec = time_passed / 1000.0
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
    ## 탁구채
        for i in range(0, 3):
            pygame.draw.rect(screen,
                             WHITE,
                             (bar_x[i], bar_y[i], int(bar_height), int(bar_width)))
        pygame.draw.rect(screen,
                         WHITE,
                         (bar_x[0], bar_y[0], int(bar_width), int(bar_height)))

        pygame.draw.rect(screen,
                         WHITE,
                         (0, 632, int(bar_height), int(bar_width)))
    ## 탁구공
        pygame.draw.circle(screen,
                           WHITE,
                           (int(circle_x), int(circle_y)),
                           int(circle_radius))

        pygame.display.update()

runGame()
pygame.quit()