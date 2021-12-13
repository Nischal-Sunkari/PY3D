import math
import time
from Vector import Vector3

cameraPosition = Vector3(0, 0, 0)
Resolution = (1280, 720)
temp = Vector3(0, 0, 0)

def CenterOrigin(x, y):
    return ((x+(Resolution[0]/2)),((Resolution[1])-y))

def Translate(p, t):
    temp.x = p.x + t.x
    temp.y = p.y + t.y
    temp.z = p.z + t.z
    return p

def Scale(p, t):
    temp.x = p.x * t.x
    temp.x = p.y * t.x
    temp.x = p.z * t.z
    return p

def RotateAroundX(p, a):
    temp.x = (p.y * math.cos(a)) - (p.z * math.sin(a))
    temp.z = (p.y * math.sin(a)) + (p.z * math.cos(a))
    return p

def RotateAroundY(p, a):
    temp.x = (p.z * math.sin(a)) + (p.x * math.cos(a))
    temp.z = (p.z * math.cos(a)) - (p.x * math.sin(a))
    return p

def RotateAroundZ(p, a):
    temp.x = (p.x * math.cos(a)) - (p.y * math.sin(a))
    temp.y = (p.x * math.sin(a)) + (p.y * math.cos(a))
    return p


def Projection(p, _focalLength):
    temp.Set(p.x - cameraPosition.x, p.y - cameraPosition.y, p.z - cameraPosition.z)
    RotateAroundY(temp, time.time()*1)
    return CenterOrigin(_focalLength * (temp.x/temp.z), _focalLength * (temp.y/temp.z))