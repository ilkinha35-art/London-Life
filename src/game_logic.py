import arcade

class Vehicle:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)

    def update(self):
        self.x += self.speed
        if self.speed > 0 and self.x > 850:
            self.x = -50
        elif self.speed < 0 and self.x < -50:
            self.x = 850


class Player:
    def __init__(self, x, y, size=30, color=arcade.color.YELLOW):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.change_x = 0
        self.change_y = 0

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, self.color)

    def update(self):
        self.x += self.change_x
        self.y += self.change_y
