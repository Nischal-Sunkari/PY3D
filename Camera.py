import pygame, math
from Vector import Vector3

class Triangle:
    def __init__(self, color, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v2
        self.color = color

class Cam:
    Triangles = []
    Lines = []

    def __init__(self,window,fov,pos=Vector3(0, 0, 0),rot=Vector3(0, 0, 0),clearColor=(135, 206, 235)):
        self.fov = fov
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.centerX = self.width//2
        self.centerY = self.height//2
        self.position = pos
        self.rotation = rot
        self.ClearColor = clearColor

    def MouseRotate(self, event, sens):
        if (event.type == pygame.MOUSEMOTION):
            x, y = event.rel
            x /= 200; y /= 200
            x *= sens; y *= sens
            self.rotation.x += y; self.rotation.y += x
    
    def UserControl(self, dt, speed, sens):
        MoveSpeed = dt*speed
        RotSpeed = dt*sens
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LSHIFT]): self.position.y -= MoveSpeed
        if (keys[pygame.K_SPACE]): self.position.y += MoveSpeed

        x, y = MoveSpeed * math.sin(self.rotation.y), MoveSpeed * math.cos(self.rotation.y)

        if (keys[pygame.K_w]): self.position.x += x; self.position.z += y
        if (keys[pygame.K_s]): self.position.x -= x; self.position.z -= y
        if (keys[pygame.K_a]): self.position.x -= y; self.position.z += x
        if (keys[pygame.K_d]): self.position.x += y; self.position.z -= x

        if (keys[pygame.K_UP]): self.rotation.x += RotSpeed
        if (keys[pygame.K_DOWN]): self.rotation.x -= RotSpeed
        if (keys[pygame.K_RIGHT]): self.rotation.y += RotSpeed
        if (keys[pygame.K_LEFT]): self.rotation.y -= RotSpeed

    def rotate2d(self, pos, rad):
        x, y = pos
        s,c = math.sin(rad), math.cos(rad)
        return x*c-y*s,y*c+x*s

    def events(self, event):
        if (event.type == pygame.MOUSEMOTION):
            x, y = event.rel
            x /= 200; y /= 200
            self.rotation.x += y; self.rotation.y += x

    def LoadModel(self, objectPath, color=(255, 255, 255)):
        vert_data = []
        triangle_indices = []
        data = None

        #read and close file
        with open(objectPath, 'r') as objectFile:
            data = objectFile.readlines()

        # get data
        for _line in data:
            _line = _line.split(" ")
            if _line[0] == 'v':
                vert_data.append(Vector3(float(_line[1]), float(_line[2]), float(_line[3])))
            elif _line[0] == 'f':
                temp = _line[1:]
                line_indices = []
                for el in temp:
                    indexList = el.split('/')
                    line_indices.append(int(indexList[0]) )

                triangle_indices.append(line_indices)

        for t in triangle_indices:
            self.AddTriangle(color, vert_data[t[0]-1], vert_data[t[1]-1],vert_data[t[2]-1])
    
    def draw(self):
        self.window.fill(self.ClearColor)
        for Triangle in self.Triangles:
            p1 = self.TransformPoint(Triangle[1])
            p2 = self.TransformPoint(Triangle[2])
            p3 = self.TransformPoint(Triangle[3])

            v1 = self.ProjectPoint2(p1)
            v2 = self.ProjectPoint2(p2)
            v3 = self.ProjectPoint2(p3)

            p2.Print("")
            print(v2)

            pygame.draw.polygon(self.window, Triangle[0], [v1, v2, v3])
            #pygame.draw.aaline(self.window, (0, 0, 0), v1, v2, 5)
            #pygame.draw.aaline(self.window, (0, 0, 0), v2, v3, 5)
            #pygame.draw.aaline(self.window, (0, 0, 0), v3, v1, 5)
            
        for Line in self.Lines:
            p1 = self.TransformPoint(Line[1])
            p2 = self.TransformPoint(Line[2])
            if(p1.z > 0 and p2.z > 0):
                v1 = self.ProjectPoint2(p1)
                v2 = self.ProjectPoint2(p2)
                pygame.draw.line(self.window, Line[0], v1, v2, Line[3])

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

    def TransformPoint(self, point):
        x, y, z = point.x, point.y, point.z
        x -= self.position.x; y -= self.position.y; z -= self.position.z
        x, z = self.rotate2d((x, z), self.rotation.y)
        y, z = self.rotate2d((y, z), self.rotation.x)
        x, y = self.rotate2d((x, y), self.rotation.z)
        return Vector3(x, y, z)

    def ProjectPoint(self, point):
        f = self.fov / point.z
        x,y = point.x*f, point.y*f

        return (self.centerX + int(x), self.centerY - int(y))
    
    def ProjectPoint2(self, point):
        x_angle = math.atan2(point.x, point.z)
        y_angle = math.atan2(point.y, point.z)
        self.width
        x = self.centerX + (x_angle / math.radians(self.fov) * self.width)
        y = self.centerY - (y_angle / math.radians(self.fov) * self.width)
        return (point.x*40, point.y*40)
        return (int(x), int(y))
    
    def AddTriangle(self, color, v1, v2, v3):
        self.Triangles.append([color, v1, v2, v3])
    
    def AddLine(self, color, v1, v2, t):
        self.Lines.append([color, v1, v2, t])