import pygame
from Camera import Cam
from Vector import Vector3

window = pygame.display.set_mode([250, 250])
clock = pygame.time.Clock()
camera = Cam(window, 90)
camera.AddTriangle((51, 170, 255), Vector3(-10, 10, 10), Vector3(10, 10, 10), Vector3(10, -10, 10))
while True:
    deltaTime = clock.tick()/1000
    camera.rotation.y += deltaTime
    camera.draw()