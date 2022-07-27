import pygame
import math
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Approximation of Pi")

FPS = 60
clock = pygame.time.Clock()

width = SCREEN_WIDTH/2
height = SCREEN_HEIGHT/2
square = pygame.Rect(width-width/2, height-height/2, width, height)

x = random.randint(square.x, square.width+int(square.width/2))
y = random.randint(square.y, square.height+int(square.height/2))
within = 0
total = 0
pi = 0

def main():
    run = True
    draw_window()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
        draw_geometry()
        draw_text()
        draw_points(50)

        pygame.display.flip()

def draw_geometry():
    pygame.draw.rect(screen, (101, 146, 201), pygame.Rect(square), 1)
    pygame.draw.circle(screen, (101, 146, 201), square.center, square.width/2, 1)

def draw_text():
    font = pygame.font.SysFont('lucidasans', 20)

    fps_count = font.render('FPS: '+str(int(clock.get_fps())), False, (255,255,255))
    within_count = font.render('Within: ' + str(within), False, (255, 255, 255))
    total_count = font.render('Total: ' + str(total), False, (255, 255, 255))
    pi_count = font.render('Approx. pi: ' + str(pi), False, (255, 255, 255))

    pygame.draw.rect(screen, (40,45,55), pygame.Rect(0,0,SCREEN_WIDTH,fps_count.get_height()*2))
    screen.blit(fps_count, (SCREEN_WIDTH-fps_count.get_width(),0))
    screen.blit(within_count, (0, 0))
    screen.blit(total_count, (within_count.get_width()+SCREEN_WIDTH/10, 0))
    screen.blit(pi_count, (0, within_count.get_height()))

def draw_points(num):
    global x,y,within,total,pi
    for i in range(num):
        x = random.randint(square.x+1, square.width + int(square.width / 2)-1)
        y = random.randint(square.y+1, square.height + int(square.height / 2)-1)

        dist = math.dist((x,y), square.center)
        color = (255, 59, 219)
        total += 1
        if dist < square.width / 2:
            color = (0, 255, 162)
            within += 1

        pi = 4 * (within / total)
        print(pi)

        pygame.draw.circle(screen, color, (x, y), 2)


def draw_window():
    screen.fill((40,45,55))

if __name__ == '__main__':
    main()
