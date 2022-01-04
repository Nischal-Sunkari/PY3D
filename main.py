from random import randint
import pygame, sys
import Constants
import Object
import Utils
pygame.init()
#Fix Rotate2D in Utils
Objects = []
window = pygame.display.set_mode((Constants.width, Constants.height))
clock = pygame.time.Clock()

Vertices, Surfaces = Utils.LoadModel("Monkey.obj")
Colors = [(randint(0, 255), randint(0, 255), randint(0, 255)) for i in Surfaces]
NewObject = Object.Object(Vertices, Surfaces, Colors)
NewObject.Translate(Utils.Vector3(0, -1, 0))
NewObject.Position.Print()
Objects.append(NewObject)

totalDeltaTime = 0
totalFrames = 0
while(True):
    deltaTime = clock.tick()/1000
    if(deltaTime != 0): totalDeltaTime += deltaTime
    totalFrames += 1
    avdT = totalDeltaTime/totalFrames
    if(avdT != 0): print(1/avdT)


    NewObject.Rotate(Utils.Vector3(0, 45 * deltaTime, 0))
    window.fill((30, 30, 30))
    for event in pygame.event.get():
        if(event.type == pygame.QUIT): pygame.quit(); sys.exit()

    for Model in Objects:
        for s in range(len(Model.Surfaces)):
            Surface = Model.Surfaces[s]
            points = []
            for p in Surface:
                points.append(Model.Vertices[p])
            Utils.ProjectPolygon(window, Model.Colors[p], points)

            
    pygame.display.flip()