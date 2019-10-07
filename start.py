import pygame as pg
import sys

pg.init()
size = width, height = 1080, 720
screen = pg.display.set_mode(size)
color = (0, 100, 100)
holo = pg.image.load('pic/holo.jpeg')
obj = pg.draw.circle(screen, [0, 0, 0], [100, 100], 50)
holorect = holo.get_rect()
speed = [1, 1]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        holorect = holorect.move(speed)
        if holorect.left < 0 or holorect.right > width:
            speed[0] = -speed[0]
        if holorect.top < 0 or holorect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(color)
        screen.blit(holo, holorect)

        pg.display.flip()
