import math
import Utils
import pygame
import Constants
from copy import deepcopy

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def Print(self):
        print(str(self.x) + ", " + str(self.y) + ", " + str(self.z))

def LoadModel(objectPath):
    Nodes = []
    Faces = []
    #read and close file
    with open(objectPath, 'r') as objectFile:
        data = objectFile.readlines()

    for _line in data:
        _line = _line.split(" ")
        if _line[0] == 'v':
            Nodes.append(Vector3(float(_line[1]), float(_line[2]), float(_line[3])))
        elif _line[0] == 'f':
            temp = _line[1:]
            line_indices = []
            for el in temp:
                indexList = el.split('/')
                if(indexList[0] != "\n"): line_indices.append(int(indexList[0]))
            Faces.append([line_indices[0]-1, line_indices[1]-1, line_indices[2]-1])

    return Nodes, Faces

def CenteredOrigin(pos):
    return (Constants.centerX + pos[0], Constants.centerY - pos[1])

def Rotate2d(pos, angle):
    angle = math.radians(angle)
    x = pos[0]
    y = pos[1]
    s, c = math.sin(angle), math.cos(angle)
    return x*c - y*s, y*c + x*s

def MultiplyMatrix(a, b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)

    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_b:
        for x in range(rows_a):
            for y in range(columns_b):
                sum = 0
                for k in range(columns_a):
                    sum += a[x][k] * b[k][y]
                result_matrix[x][y] = sum
        return result_matrix

    else:
        print("columns of the first matrix must be equal to the rows of the second matrix")
        return None

def ProjectPoint(pos):
    distance = 5
    z = 1 / (distance - pos.z)
    projectionMatrix = [[z, 0, 0],
                        [0, z, 0]]
    MatPos = [[pos.x], [pos.y], [pos.z]]
    MatrixPos = MultiplyMatrix(projectionMatrix, MatPos)
    x = int(MatrixPos[0][0] * Constants.scale)
    y = int(MatrixPos[1][0] * Constants.scale)
    return CenteredOrigin((x, y))

def IsVector3(vec):
    try:
        if(vec.z == 0): pass
        return True
    except:
        return False

def ProjectPolygon(window, color, polygon):
    projectedPoints = []
    for point in polygon:
        projectedPoints.append(ProjectPoint(point))
    pygame.draw.polygon(window, color, projectedPoints)

def CalculateObjectCenter(Vertices):
    Sum = Utils.Vector3(0, 0, 0)
    Total = 0
    for Vec in Vertices:
        Sum.x += Vec.x
        Sum.y += Vec.y
        Sum.z += Vec.z
        Total += 1
    return Vector3(Sum.x/Total, Sum.y/Total, Sum.z/Total)