import arcade

class Player(arcade.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__("assets/images/player.png", scale=1.0)
        self.center_x = start_x
        self.center_y = start_y
        self.speed = 5
        self.jump_speed = 12
