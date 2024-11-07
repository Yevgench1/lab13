import math
import random

class VECTOR:
    def __init__(self, name, x1, y1, x2, y2):
        self.name = name 
        self.x1 = x1 
        self.y1 = y1 
        self.x2 = x2 
        self.y2 = y2 
    def GetLen(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

    def Plus(self, other):
        return VECTOR(
            f"{self.name}+{other.name}",
            self.x1 + other.x1, 
            self.y1 + other.y1,
            self.x2 + other.x2, 
            self.y2 + other.y2
        )

    def ShowName(self):
        print(f"Назва вектора: {self.name}")

    def SetCoord(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_in_third_quadrant(self):
        return self.x1 < 0 and self.y1 < 0 and self.x2 < 0 and self.y2 < 0
