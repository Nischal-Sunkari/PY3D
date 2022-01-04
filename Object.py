import math
import Utils
from copy import deepcopy
from math import radians, sin, cos
from Utils import Vector3
class Object:
    def __init__(self, Vertices, Surfaces, Colors, Position=Vector3(0,0,0), Rotation=Vector3(0,0,0), Scale=Vector3(1,1,1)):
        self.Vertices = Vertices
        self.Surfaces = Surfaces
        self.Colors = Colors
        self.Position = Position
        self.Rotation = Rotation
        self.LocalScale = Scale
    
    def Translate(self, Change):
        self.Position.x += Change.x
        self.Position.y += Change.y
        self.Position.z += Change.z
        for v in range(len(self.Vertices)):
            self.Vertices[v].x += Change.x
            self.Vertices[v].y += Change.y
            self.Vertices[v].z += Change.z

    def Rotate(self, Change):
        self.Rotation.x += Change.x
        self.Rotation.y += Change.y
        self.Rotation.z += Change.z
        PreviousPosition = deepcopy(self.Position)
        self.Translate(Vector3(-self.Position.x, -self.Position.y, -self.Position.z))
        for n in range(len(self.Vertices)):
            self.Vertices[n].x, self.Vertices[n].z = Utils.Rotate2d((self.Vertices[n].x, self.Vertices[n].z), Change.y)
            self.Vertices[n].y, self.Vertices[n].z = Utils.Rotate2d((self.Vertices[n].y, self.Vertices[n].z), Change.x)
            self.Vertices[n].x, self.Vertices[n].y = Utils.Rotate2d((self.Vertices[n].x, self.Vertices[n].y), Change.z)
        self.Translate(PreviousPosition)


    def Scale(self, Change):
        self.LocalScale.x += Change.x
        self.LocalScale.y += Change.y
        self.LocalScale.z += Change.z
        PreviousPosition = deepcopy(self.Position)
        self.Translate(Vector3(-self.Position.x, -self.Position.y, -self.Position.z))
        for n in range(len(self.Vertices)):
            self.Vertices[n].x *= Change.x
            self.Vertices[n].y *= Change.y
            self.Vertices[n].z *= Change.z
        self.Translate(PreviousPosition)