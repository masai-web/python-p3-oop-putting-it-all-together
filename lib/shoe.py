#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size=0, color="Unknown"):
        self.brand = brand
        self.size = size
        self.color = color
        self.condition = "Used"
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"