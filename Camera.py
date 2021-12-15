import pygame, math
from Vector import Vector3, Vector2

class Triangle:
    def __init__(self, color, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v2
        self.color = color

class Cam:
    Triangles = []

    def __init__(self,window,fov,pos=Vector3(0, 0, 0),rot=Vector2(0, 0),clearColor=(135, 206, 235)):
        self.fov = fov
        self.window = window
        self.centerX = window.get_width()//2
        self.centerY = window.get_height()//2
        self.position = pos
        self.rotation = rot
        self.ClearColor = clearColor

    def rotate2d(self, pos, rad):
        x, y = pos
        s,c = math.sin(rad), math.cos(rad)
        return x*c-y*s,y*c+x*s

    def events(self, event):
        if (event.type == pygame.MOUSEMOTION):
            x, y = event.rel
            x /= 200; y /= 200
            self.rotation.x += y; self.rotation.y += x
    
    def draw(self):
        self.window.fill(self.ClearColor)
        for Triangle in self.Triangles:
            pygame.draw.polygon(self.window, Triangle[0], [Triangle[1], Triangle[2], Triangle[3]])
        pygame.display.flip()

    
    def Rotate(self, x, y):
        self.rotation.x += x
        self.rotation.y += y

    """
    
    def Translate(self, x, y, z):
		_x = Math.sin(rot.z) * Math.sin(rot.x)
        _y = 0 - Math.cos(rot.x)
        _z = Math.cos(rot.z) * Math.sin(rot.x)
        self.position.x += 
        self.position.y += 
        self.position.z += 
    
    """

    def ProjectPoint(self, point):
        x, y, z = point.x, point.y, point.z
z        x, z = self.rotate2d((x, z), self.rotation.y)
        y, z = self.rotate2d((y, z), self.rotation.x)

        f = self.fov/z
        x,y = x*f, y*f
        return (self.centerX + int(x), self.centerY + int(y))
    
    def AddTriangle(self, color, v1, v2, v3):
        v1 = self.ProjectPoint(v1)
        v2 = self.ProjectPoint(v2)
        v3 = self.ProjectPoint(v3)
        self.Triangles.append([color, v1, v2, v3])