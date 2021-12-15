import pygame, math

class Cam:
    Triangles = []

    def __init__(self, window, fov, pos=(0, 0, 0), rot=(0, 0)):
        self.fov = fov
        self.window = window
        self.centerX = window.get_width()//2
        self.centerY = window.get_height()//2
        self.position = list(pos)
        self.rotation = list(rot)

    def rotate2d(pos, rad):
        x, y = pos
        s,c = math.sin(rad), math.cos(rad)
        return x*c-y*s,y*c+x*s

    def events(self, event):
        if (event.type == pygame.MOUSEMOTION):
            x, y = event.rel
            x /= 200; y /= 200
            self.rotation[0] += y; self.rotation[1] += x
    
    def draw(self, window):
        for Triangle in self.Triangles:
            pygame.draw.polygon(window, Triangle[0], [Triangle[1], Triangle[2], Triangle[3]])

    
    def Rotate(self, x, y):
        self.rotation[0] += x
        self.rotation[1] += y

    """
    
    def Translate(self, x, y, z):
		_x = Math.sin(rot[2]) * Math.sin(rot[0])
        _y = 0 - Math.cos(rot[0])
        _z = Math.cos(rot[2]) * Math.sin(rot[0])
        self.position[0] += 
        self.position[1] += 
        self.position[2] += 
    
    """

    def ProjectPoint(self, point):
        x, y, z = point[0], point[1], point[2]
        x -= self.position[0]; y -= self.position[1]; z -= self.position[2]
        x, z = self.rotationate2d((x, z), self.rotation[1])
        y, z = self.rotationate2d((y, z), self.rotation[0])

        f = self.fov/z
        x,y = x*f, y*f
        return (self.centerX + int(x), self.centerY + int(y))
    
    def AddTriangle(self, color, v1, v2, v3):
        _v1 = (self.ProjectPoint(v1), self.ProjectPoint(v2))
        _v2 = (self.ProjectPoint(v2), self.ProjectPoint(v3))
        _v3 = (self.ProjectPoint(v3), self.ProjectPoint(v1))

        self.Triangles.append([color, _v1, _v2, _v3])