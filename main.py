import pygame, sys, math, os
from Camera import Cam
from Vector import Vector3

Speed = 5
Sensitivity = math.pi

window = pygame.display.set_mode([250, 250])
clock = pygame.time.Clock()
camera = Cam(window, 90)


camera.AddTriangle((102, 255, 102), Vector3(10, -1, 10), Vector3(10, -1, -10), Vector3(-10, -1, 10))
#camera.AddTriangle((102, 255, 102), Vector3(-10, -1, -10), Vector3(10, -1, -10), Vector3(-10, -1, 10))

#camera.AddTriangle((51, 170, 255), Vector3(1, 1, 0), Vector3(-1, 1, 0), Vector3(-1, -1, 0))
#camera.AddTriangle((255, 102, 102), Vector3(1, 1, 0), Vector3(1, -1, 0), Vector3(-1, -1, 0))

camera.AddLine((255, 0, 0), Vector3(0, 0, 0), Vector3(2, 0, 0), 5)
camera.AddLine((0, 255, 0), Vector3(0, 0, 0), Vector3(0, 2, 0), 5)
camera.AddLine((0, 0, 255), Vector3(0, 0, 0), Vector3(0, 0, 2), 5)

#pygame.event.get(); pygame.mouse.get_rel()
#pygame.mouse.set_visible(0); pygame.event.set_grab(1)
while True:
    deltaTime = clock.tick()/1000
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if event.type == pygame.MOUSEMOTION:
            #camera.MouseRotate(event, sens)
    #camera.rotation.y += deltaTime
    camera.draw()
    os.system("clear")
    #camera.position.Print("Position: ")
    #camera.rotation.Print("Rotation: ")
    camera.UserControl(deltaTime, Speed, Sensitivity)