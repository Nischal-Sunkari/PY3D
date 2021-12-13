class Vector3:
  def __init__(self, _x, _y, _z):
    self.x = _x
    self.y = _y
    self.z = _z

  def Reset(self):
    self.x = 0
    self.y = 0
    self.z = 0

  def Set(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

class Vector2:
  def __init__(self, _x, _y):
    self.x = _x
    self.y = _y

  def Reset(self):
    self.x = 0
    self.y = 0

  def Set(self, x, y, z):
    self.x = x
    self.y = y
