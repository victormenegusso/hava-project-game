import arcade
from src import constants

class Enemy(arcade.Sprite):
    def __init__(self, **kwargs):
        # Tiled passes properties via kwargs when using custom classes
        super().__init__("assets/images/enemy.png", scale=1.0)
        self.speed = 2
        
    def follow_player(self, player):
        """Simple AI to move towards the player horizontally"""
        if self.center_x < player.center_x:
            self.change_x = self.speed
        elif self.center_x > player.center_x:
            self.change_x = -self.speed
        else:
            self.change_x = 0
            
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
