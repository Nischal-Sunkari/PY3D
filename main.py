import math
import pygame
from Vector import Vector3

pygame.init()
ClearColor = (135, 206, 235)
fov = 90

Resolution = (533, 300)
window = pygame.display.set_mode(Resolution)

def Convert2D(p):
    x_angle = math.atan2(p.x, p.z)
    y_angle = math.atan2(p.y, p.z)
    x = x_angle / math.radians(fov) * Resolution[0] + Resolution[0] // 2
    y = Resolution[1] // 2 - (y_angle / math.radians(fov) * Resolution[0])
    return (x, y)

def Triangle3D(color, p1, p2, p3):
    points = [
        Convert2D(p1),
        Convert2D(p2),
        Convert2D(p3)
    ]
    pygame.draw.polygon(window, color, points)

def Plane3D(color, pos, w, l):
  x1 = pos.x + (w/2) 
  z1 = pos.z + (l/2)
  x2 = pos.x - (w/2)
  z2 = pos.z - (l/2)
  Triangle3D(color, Vector3(x1, pos.y, z1), Vector3(x2, pos.y, z1), Vector3(x2, pos.y, z2))
  Triangle3D(color, Vector3(x1, pos.y, z1), Vector3(x1, pos.y, z2), Vector3(x2, pos.y, z2))


running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(ClearColor)

    Plane3D((102, 235, 102), Vector3(1, -0.1, -3), 20, 20)
    Triangle3D((102, 255, 102), Vector3(-1, 1, 3), Vector3(1, 1, 3), Vector3(-1, -1, 3))
    Triangle3D((255, 102, 102), Vector3(1, -1, 3), Vector3(1, 1, 3), Vector3(-1, -1, 3))

    pygame.display.flip()