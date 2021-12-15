class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def Set(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def Reset(self):
        self.x = 0
        self.y = 0
        self.z = 0

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def Set(self, x, y):
        self.x = x
        self.y = y
    
    def Reset(self):
        self.x = 0
        self.y = 0