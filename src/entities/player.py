import arcade
from src import constants

class Player(arcade.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__("assets/images/player.png", scale=1.0)
        self.center_x = start_x
        self.center_y = start_y
        self.speed = constants.PLAYER_MOVEMENT_SPEED
        self.jump_speed = constants.PLAYER_JUMP_SPEED
