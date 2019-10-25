import pygame


class Env:
    def __init__(self, gravitational_constance, screen, fps):
        self.G = gravitational_constance
        self.screen = screen
        self.fps = fps
        self.dt = 1 / self.fps

    def speed_update(self, speed):
        speed[1] = speed[1] + self.G * self.dt
        return speed

    def bound(self, bullet, speed, width, height):
        if bullet.obj.left < 0 or bullet.obj.right > width:
            speed[0] = -speed[0]
        if bullet.obj.top < 0 or bullet.obj.bottom > height:
            speed[1] = -speed[1]

